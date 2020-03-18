#pragma once
#include <Windows.h>

template<class Container>
class WindowsFinder
{ 
public:
	static bool Find(Container* set)
	{
		return EnumWindows(&WindowsFinder::GetWindowsList, LPARAM(set));
	}
	
	static bool Find(WNDENUMPROC lpEnumFunc, Container* set)
	{
		return EnumWindows(lpEnumFunc, LPARAM(set));
	}


private:
	static BOOL __stdcall GetWindowsList(HWND hWnd, LPARAM lParam)
	{
		auto* con = reinterpret_cast<Container*>(lParam);
		if (hWnd)
		{
			if (!::IsWindowVisible(hWnd))
				return TRUE;
			if (::GetWindowTextLength(hWnd) == 0)
				return TRUE;
			if (::GetParent(hWnd) != 0)
				return TRUE;
			con->push_back(hWnd);
			return TRUE;
		}
		return FALSE;
	}
};

