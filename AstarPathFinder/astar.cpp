#include <list>
#include <iostream>
#include <queue>
using namespace std;

int g_map[5][7] =
{
	{0,0,0,0,0,0,0},
	{0,0,0,1,0,0,0},
	{0,0,0,1,0,0,0},
	{0,0,0,1,0,0,0},
	{0,0,0,0,0,0,0}
};

struct node
{
	int y;
	int x;
	node* parent;
	int G;
	int H;

	int F() const
	{
		return G + H;
	}

	bool operator>(const node& t) const 
	{
		return F() > t.F();
	}

	bool operator<(const node& t) const
	{
		return F() < t.F();
	}

	bool operator==(const node& t) const
	{
		return x == t.x && y == t.y;
	}
};

bool isValid(int y, int x)
{
	return 0 <= y && y < 5 && 0 <= x && x < 7 && !g_map[y][x];
}

int getH(int y, int x)
{
	return 10 * (abs(2 - y) + abs(5 - x));
}

bool isClosed(const node& n, const list<node>& l)
{
	for (const auto& i : l)
	{
		if (n == i)
			return true;
	}
	return false;
}

bool isOpen(const node& n, const list<node>& l)
{
	for (const auto& i : l)
	{
		if (n == i && n > i)
			return true;
	}
	return false;
}

int main()
{
	node start{ 2, 1, nullptr, 0 };
	node cur = start;
	priority_queue<node> openlist;
	list<node> closelist;
	
	int row[] = { -1,0,1,1,1,0,-1,-1 };
	int col[] = { -1,-1,-1,0,1,1,1,0 };
	openlist.push_back(cur);
	while (!openlist.empty())
	{
		for (int i = 0; i < 8; i++)
		{
			if (isValid(cur.y + col[i], cur.x + row[i]) 
				&& !isClosed(node{ cur.y + col[i], cur.x + row[i] }, closelist))
			{
				int G = cur.G + ((i % 2 == 0) ? 14 : 10);
				int H = getH(cur.y + col[i], cur.x + row[i]);
				node child{ cur.y + col[i], cur.x + row[i], &cur, G, H };
				if (!isOpen(child, openlist))
				{
					openlist.push_back(child);
				}
			}
		}

		if (min(openlist) == node{ 2,5 })
		{
			cout << "end";
			break;
		}
		
		closelist.push_back(openlist.top());
		openlist.pop();
	}
	


	/*
	while (!openlist.empty())
	{
		const node* top = &openlist.top();
		cout << "(" << top->y << ", " << top->x << ") ";
		cout << "G:" << top->G << " H:" << top->H << " F:" << top->F() << endl;
		openlist.pop();
	}
	*/
	cin.get();


}

