#pragma once
#include <Windows.h>
#include <vector>
using namespace std;

class WindowsFinder
{ 
public:
	static void Find(vector<HWND>* set)
	{
		EnumWindows(&WindowsFinder::GetWindowsList, LPARAM(set));
	}
	
private:
	static BOOL __stdcall GetWindowsList(HWND hWnd, LPARAM lParam)
	{
		auto* vec = reinterpret_cast<vector<HWND>*>(lParam);
		if (::IsWindow(hWnd))
		{
			if (!::IsWindowVisible(hWnd))
				return TRUE;
			if (::GetWindowTextLength(hWnd) == 0)
				return TRUE;
			if (::GetParent(hWnd) != 0)
				return TRUE;
			vec->push_back(hWnd);
			return TRUE;
		}
		return FALSE;
	}
};

