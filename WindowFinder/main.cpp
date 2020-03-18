#include <iostream>
#include "WindowsFinder.h"
#include <list>
#include <vector>
using namespace std;

int main()
{
	list<HWND> vec;
	WindowsFinder<list<HWND>>::Find(&vec);

	wcout.imbue(locale("kor"));
	wchar_t str[256] = { 0 };
	for (auto i : vec)
	{
		WindowsFinder<>::GetWindowName(str, i, 256);
		wcout << str << endl;
	}
}