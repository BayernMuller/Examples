#include "Astar.h"

Astar::Astar(int height, int width, map_type map, point start, point end)
	: mWidth(width), mHeigth(height), mpMap(map), mStart(start), mEnd(end)
	, mCompare([](node_ptr left, node_ptr right) { return left->F() < right->F(); })
	, mOpenList(mCompare), mCloseList(mCompare)
{
}

node* Astar::operator()()
{
	static const int row[] = { -1,0,1,1,1,0,-1,-1 };
	static const int col[] = { -1,-1,-1,0,1,1,1,0 };

	node_ptr current = nullptr;
	freeList(mOpenList);
	freeList(mCloseList);
<<<<<<< HEAD
=======

>>>>>>> b2ed0c45de85536c6b5ba02f3052a53a1d2a4414
	mOpenList.clear();
	mCloseList.clear();
	mOpenList.insert(new node(mStart));

<<<<<<< HEAD
	while (!mOpenList.empty())
	{
		current = *mOpenList.begin();
=======
	mOpenList.insert(new node{ mStart, nullptr });
	while (!mOpenList.empty())
	{
		current = *mOpenList.begin();

>>>>>>> b2ed0c45de85536c6b5ba02f3052a53a1d2a4414
		if (current->pt == mEnd)
		{
			return current;
		}

		mCloseList.insert(current);
<<<<<<< HEAD
		mOpenList.erase(mOpenList.begin());
=======
		mOpenList.erase(mOpenList.begin());		
>>>>>>> b2ed0c45de85536c6b5ba02f3052a53a1d2a4414

		for (int i = 0; i < 8; i++)
		{
			point newPt = make_pair(current->pt.first + col[i], current->pt.second + row[i]);
			if (!isValid(newPt) || findOnList(mCloseList, newPt) != end(mCloseList))
			{
				continue;
			}

			int newNodeG = current->G + ((i % 2 == 0) ? 14 : 10);
			auto pSuccess = findOnList(mOpenList, newPt);
<<<<<<< HEAD
			auto newNode = new node(newPt, current);
			newNode->G = newNodeG;
			newNode->H = calculateH(newPt);
			if (pSuccess == end(mOpenList))
			{
				mOpenList.insert(newNode);
				continue;
=======


			node* child = new node{ newPt, current };
			child->G = newNodeG;
			child->H = calculateH(child);
			if (pSuccess == mOpenList.end())
			{
				mOpenList.insert(child);
>>>>>>> b2ed0c45de85536c6b5ba02f3052a53a1d2a4414
			}
			else if (newNodeG < (*pSuccess)->G)
			{
				mOpenList.erase(pSuccess);
<<<<<<< HEAD
				mOpenList.insert(newNode);
				continue;
			}
			delete newNode;
=======
				mOpenList.insert(child);
			}
			else
			{
				delete child;
			}
>>>>>>> b2ed0c45de85536c6b5ba02f3052a53a1d2a4414
		}
	}
	return nullptr;
}

void Astar::freeList(const list_type& ls)
{
	for (const auto& pointer : ls)
	{
		delete pointer;
	}
}

bool Astar::isValid(point pt)
{
	return 0 <= pt.first && pt.first < mHeigth \
		&& 0 <= pt.second && pt.second < mWidth \
		&& !mpMap[pt.first][pt.second];
}

Astar::node_iterator Astar::findOnList(const list_type& ls, point pt)
{
	for (auto itr = ls.begin(); itr != ls.end(); itr++)
	{
		if ((*itr)->pt == pt)
			return itr;
	}
	return ls.end();
}

int Astar::calculateH(point pt)
{
	return 10 * (abs(mEnd.first - pt.first) + abs(mEnd.second - pt.second));
}

Astar::~Astar()
{
	freeList(mOpenList);
	freeList(mCloseList);
}