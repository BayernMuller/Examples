#include <iostream>
#include "WindowsFinder.h"
#include <list>
#include <vector>
using namespace std;

int main()
{
	list<HWND> lis;
	WindowsFinder::Find(&lis);

	vector<HWND> vec;
	WindowsFinder::Find(&vec);
	
	wcout.imbue(locale("kor"));
	wchar_t str[256] = { 0 };
	for (auto i : vec)
	{
		WindowsFinder::GetWindowName(str, i, 256);
		wcout << str << endl;
	}
	cout << "\n\n";
	for (auto i : lis)
	{
		WindowsFinder::GetWindowClass(str, i, 256);
		wcout << str << endl;
	}
}