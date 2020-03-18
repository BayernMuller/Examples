#pragma once
#include <Windows.h>
#include <vector>
using namespace std;

template<class Container = vector<HWND>>
class WindowsFinder
{ 
public:
	static bool Find(Container* set)
	{
		if (IsWrongType())
			return false;
		return EnumWindows(&WindowsFinder::GetWindowsList, LPARAM(set));
	}
	
	static bool Find(WNDENUMPROC lpEnumFunc, Container* set)
	{
		if (IsWrongType())
			return false;
		return EnumWindows(lpEnumFunc, LPARAM(set));
	}

	

private:
	static BOOL __stdcall GetWindowsList(HWND hWnd, LPARAM lParam)
	{
		auto* con = reinterpret_cast<Container*>(lParam);
		if (::IsWindow(hWnd))
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

	static bool IsWrongType()
	{
		return typeid(Container::value_type) != typeid(HWND);
	}
};

