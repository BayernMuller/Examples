#pragma once
using position = void*;
template<class T>
class linkedlist
{
public:
	linkedlist<T>();
	~linkedlist<T>();

	void PushBack(T&& data);
	void PushBack(const T& data);
	void PushFront(T&& data);
	void PushFront(const T& data);

	template<typename Param>
	position Insert(position pos, Param data);
	position GetHeadPos();
	position GetTailPos();
	position GetEnd();
	position GetNext(position pos);
	position GetPrev(position pos);
	position Erase(position pos);
	position Find(T&& data, position _begin, position _end);
	std::size_t Size();
	T& GetAt(position pos);

private:
	struct node
	{
		node* next;
		node* prev;
		T data;
	};

	node m_Head;
	node m_Tail;
	std::size_t m_nSize;
};

template<class T>
linkedlist<T>::linkedlist()
{
	m_Head.next = &m_Tail;
	m_Tail.prev = &m_Head;
	
}

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

template<class T>
position linkedlist<T>::GetHeadPos()
{
	return m_Head.next;
}

template<class T>
position linkedlist<T>::GetTailPos()
{
	return m_Tail.prev;
}

template<class T>
inline position linkedlist<T>::GetEnd()
{
	return &m_Tail;
}

template<class T>
position linkedlist<T>::GetNext(position pos)
{
	auto* p = static_cast<node*>(pos)->next;
	return p == &m_Tail ? nullptr : p;
}


template<class T>
position linkedlist<T>::GetPrev(position pos)
{
	auto* p = static_cast<node*>(pos)->prev;
	return p == &m_Head ? nullptr : p;
}

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

template<class T>
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

template<class T>
inline std::size_t linkedlist<T>::Size()
{
	return m_nSize;
}

template<class T>
T & linkedlist<T>::GetAt(position pos)
{
	return static_cast<node*>(pos)->data;
}
