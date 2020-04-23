#include "Astar.h"

const int Astar::mRow[] = { -1 ,0 ,1 ,1 ,1 ,0 ,-1 ,-1 };
const int Astar::mCol[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
// initialize static member variables

Astar::Astar(int height, int width, map_type map, point start, point end)
	: mWidth(width), mHeigth(height), mpMap(map), mStart(start), mEnd(end)
	, mCompare([](node_ptr left, node_ptr right) { return left->F() < right->F(); })
	, mOpenList(mCompare), mCloseList(mCompare), mpCurrent(nullptr)
{
}

node* Astar::FindPath()
{
	mpCurrent = nullptr;
	freeList(mOpenList);
	freeList(mCloseList);
	mOpenList.clear();
	mCloseList.clear();
	mOpenList.insert(new node(mStart));
	while (!mOpenList.empty())
	{
		auto path = OneStep();
		if (path)
		{
			return path;
		}
	}
	return nullptr;
}

node* Astar::OneStep()
{
	mpCurrent = *mOpenList.begin();
	if (mpCurrent->pt == mEnd)
	{
		return mpCurrent;
	}

	mCloseList.insert(mpCurrent);
	mOpenList.erase(mOpenList.begin());

	for (int i = 0; i < 8; i++)
	{
		point newPt = make_pair(mpCurrent->pt.first + mCol[i], mpCurrent->pt.second + mRow[i]);
		if (!isValid(newPt) || findOnList(mCloseList, newPt) != end(mCloseList))
		{
			continue;
		}

		int newNodeG = mpCurrent->G + ((i % 2 == 0) ? 14 : 10);
		auto pSuccess = findOnList(mOpenList, newPt);
		auto newNode = new node(newPt, mpCurrent);
		newNode->G = newNodeG;
		newNode->H = calculateH(newPt);
		if (pSuccess == end(mOpenList))
		{
			mOpenList.insert(newNode);
			continue;
		}
		else if (newNodeG < (*pSuccess)->G)
		{
			mOpenList.erase(pSuccess);
			mOpenList.insert(newNode);
			continue;
		}
		delete newNode;
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
