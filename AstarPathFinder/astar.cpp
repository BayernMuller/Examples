#include "Astar.h"

Astar::Astar(int width, int height, map_type map, point start, point end)
	: mWidth(width), mHeigth(height), mpMap(map), mStart(start), mEnd(end)
	, mCompare([](node_ptr left, node_ptr right) { return *left < *right; })
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

	mOpenList.clear();
	mCloseList.clear();

	mOpenList.insert(new node{ mStart, nullptr });
	while (!mOpenList.empty())
	{
		current = *mOpenList.begin();

		if (current->pt == mEnd)
		{
			break;
		}

		mCloseList.insert(current);
		mOpenList.erase(mOpenList.begin());		

		for (int i = 0; i < 8; i++)
		{
			auto newPt = make_pair(current->pt.first + col[i], current->pt.second + row[i]);
			if (!isValid(newPt) 
				|| findOnList(mCloseList, newPt) != mCloseList.end())
				continue;

			int newNodeG = current->G + ((i % 2 == 0) ? 14 : 10);
			auto pSuccess = findOnList(mOpenList, newPt);


			node* child = new node{ newPt, current };
			child->G = newNodeG;
			child->H = calculateH(child);
			if (pSuccess == mOpenList.end())
			{
				mOpenList.insert(child);
			}
			else if (newNodeG < (*pSuccess)->G)
			{
				mOpenList.erase(pSuccess);
				mOpenList.insert(child);
			}
			else
			{
				delete child;
			}
		}
	}
	return current;
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
	return 0 <= pt.first && pt.first < mWidth \
		&& 0 <= pt.second && pt.second < mHeigth \
		&& !mpMap[pt.first][pt.second];
}

Astar::node_iterator Astar::findOnList(const list_type& ls, point pt)
{
	for (auto itr = ls.begin(); itr != ls.end(); ++itr)
	{
		if ((*itr)->pt == pt)
			return itr;
	}
	return ls.end();
}

int Astar::calculateH(const node_ptr n)
{
	return 10 * (abs(mEnd.first - n->pt.first) + abs(mEnd.second - n->pt.second));
}

Astar::~Astar()
{
	freeList(mOpenList);
	freeList(mCloseList);
}