# C++ Linked List

### 코드 설명

- 삽입

```C++
void linkedlist<T>::PushBack(T && data)
{
	Insert(GetTailPos(), std::move(data));
}
    
template<class T>
void linkedlist<T>::PushBack(const T & data)
{
	Insert(GetTailPos(), data);
}
    
template<class T>
void linkedlist<T>::PushFront(T && data)
{
	Insert(GetHeadPos(), std::move(data));
}

template<class T>
void linkedlist<T>::PushFront(const T & data)
{
   	Insert(GetHeadPos(), data);
}
```

함수의 오버로딩을 이용하여 rvalue reference, lvalue reference를 각각 받는 함수를 만들어 Insert를 호출하게 한다. T&&를 인자로 받는 함수들은 rvalue를 참조하고 있지만 rvalue reference그 자체는 lvalue이기때문에 std::move()를 이용해 rvalue으로 캐스팅한다.

```C++
template<class T> template<typename Param>
position linkedlist<T>::Insert(position pos, Param data)
{
	node* p = static_cast<node*>(pos);
	auto* left = p;
	auto* right = p->next;
	auto* newNode = new node;
	newNode->data = std::forward<Param>(data);

	left->next = newNode;
	newNode->prev = left;
	newNode->next = right;
	right->prev = newNode;
	m_nSize++;
	return newNode;
}
```

Insert 함수이다. 파라미터로 넘어오는 pos, pos→next 사이에 새 원소를 끼워넣는 작업이다. 이 때 Param은 const T& 또는 T&& 이다. 완벽한 전달(perfect forwarding)을 위해 std:forward() 함수를 사용한다.



- 탐색

```C++
template<class T>
position linkedlist<T>::Find(T && data, position _begin, position _end)
{
	node *cur = static_cast<node*>(_begin), *end = static_cast<node*>(_end);
	while (cur != end)
	{
		if (cur->data == data)
			return cur;
		cur = (node*)GetNext(cur);
	}
	return nullptr;
}
```

_begin ~ _end→prev 까지의 범위를 탐색해 그 위치의 position을 리턴한다. 찾지 못하면 nullptr 리턴.



- 삭제

```C++
template<class T>
position linkedlist<T>::Erase(position pos)
{
	node* p = static_cast<node*>(pos), *current;
	p->prev->next = p->next;
	p->next->prev = p->prev;
	current = p->next;
	delete p;
	m_nSize--;
	return current;
}
```

pos→prev 와 pos→next를 연결시키고 pos는 삭제한다.



- 메모리 정리

```C++
template<class T>
linkedlist<T>::~linkedlist()
{
	position pos = GetHeadPos(), next;
	while (pos != nullptr)
	{
		next = GetNext(pos);
		delete pos;
		pos = next;
	}
}
```

파괴자에서는 동적할당 했었던 모든 원소들을 삭제한다.



- std::list와 비교

```C++
#include "pch.h"
#include <iostream>
#include "linkedlist.h"
#include <list>
#include <chrono>
#include <string>
using namespace std;

int main()
{
	chrono::system_clock::time_point start, end;

	start = chrono::system_clock::now();
	linkedlist<string> my;
	my.PushBack("햄버거");
	my.PushBack("치킨");
	my.PushBack("초밥");
	my.PushBack("샤브샤브");
	my.PushBack("육회");
	my.PushBack("연어회");
	my.Erase(my.GetHeadPos());

	for (auto itr = my.GetHeadPos(); itr; itr = my.GetNext(itr))
		cout << my.GetAt(itr) << endl;
	cout << my.GetAt(my.Find("샤브샤브", my.GetHeadPos(), my.GetEnd())) << endl;
	end = chrono::system_clock::now();
	cout << "my linkedlist: " << (end - start).count() << endl << endl;


	start = chrono::system_clock::now();
	list<string> ls;
	ls.push_back("햄버거");
	ls.push_back("치킨");
	ls.push_back("초밥");
	ls.push_back("샤브샤브");
	ls.push_back("육회");
	ls.push_back("연어회");
	ls.erase(ls.begin());
	for (auto itr = ls.begin(); itr != ls.end(); itr++)
		cout << *itr << endl;
	cout << *find(ls.begin(), ls.end(), "샤브샤브") << endl;
	end = chrono::system_clock::now();
	cout << "std:list: " << (end - start).count() << endl;
}
```

같은 조건으로 비교해보았다.



출력 결과..

```
치킨
초밥
샤브샤브
육회
연어회
샤브샤브
my linkedlist: 15485

치킨
초밥
샤브샤브
육회
연어회
샤브샤브
std:list: 12106
```



std::list쪽이 10번중 7번 더 빨랐다. 역시 표준은 못따라가나보다. 끝
