#include <iostream>
#include "WindowsFinder.h"
using namespace std;

int main()
{
	vector<HWND> vec;
	WindowsFinder::Find(&vec);
	wcout.imbue(locale("kor"));
	for (auto handle : vec)
	{
		wchar_t str[256];
		GetWindowText(handle, str, 256);
		wcout << str << endl;
	}
}