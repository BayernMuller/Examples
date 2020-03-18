#include <iostream>
#include "WindowsFinder.h"
#include <list>
#include <vector>
using namespace std;

int main()
{
	list<HWND> vec;
	WindowsFinder<list<HWND>>::Find(&vec);
}