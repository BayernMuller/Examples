#include <iostream>
#include "Astar.h"
using namespace std;

int main()
{
	int** map;
	map = new int* [5];
	map[0] = new int[7]{ 0,0,0,0,0,0,0 };
	map[1] = new int[7]{ 0,0,0,1,0,0,0 };
	map[2] = new int[7]{ 0,0,0,1,0,0,0 };
	map[3] = new int[7]{ 0,0,0,1,0,0,0 };
	map[4] = new int[7]{ 0,0,0,0,0,0,0 };


	Astar path(7, 5, map, { 2,1 }, { 2,5 });

	auto node = path();
	while (node)
	{
		cout << node->pt.first << " " << node->pt.second << endl;
		map[node->pt.first][node->pt.second] = 9;
		node = node->parent;
	}

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 7; j++)
		{
			cout << map[i][j] << ' ';
		}
		cout << endl;
	}

	for (int i = 0; i < 5; i++)
	{
		delete[] map[i];
	}
	delete[] map;
	cin.get();
}

