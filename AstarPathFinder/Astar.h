#ifndef ASTAR_H
#define ASTAR_H
#include <set>
#include <list>
using namespace std;

using point = pair<int, int>;
struct node
{
	point pt;
	node* parent;
	int G;
	int H;

	node(point _pt, node* _parent = nullptr)
		: pt(_pt), parent(_parent) {}
	int F() {return G + H;}
};


//////////////////////////////////////////////////

class Astar
{
public:
	using node_ptr = node*;
	using map_type = int**;
	using compare_type = bool(*)(node_ptr, node_ptr);
	using list_type = multiset<node_ptr, compare_type>;
	using node_iterator = list_type::iterator;
	
public:
	Astar(int height, int width, map_type map, point start, point end);
	~Astar();

	node* operator()();

private:
	void freeList(const list_type& ls);
	bool isValid(point pt);
	node_iterator findOnList(const list_type& ls, point pt);
	int calculateH(point n);

private:
	compare_type mCompare;
	list_type mOpenList;
	list_type mCloseList;
	map_type mpMap;
	const point mStart;
	const point mEnd;
	const int mWidth;
	const int mHeigth;
};


#endif // ASTAR_H

