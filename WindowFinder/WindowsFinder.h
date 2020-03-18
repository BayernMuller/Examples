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

	static WNDENUMPROC GetCallbackFunc()
	{
		return GetWindowsList;
	}

	static wchar_t* GetWindowName(wchar_t str[], HWND hWnd, std::size_t maxsize)
	{
		if (!::IsWindow(hWnd))
			return nullptr;
		::GetWindowText(hWnd, str, maxsize);
		return str;
	}

	static wchar_t* GetWindowClass(wchar_t str[], HWND hWnd, std::size_t maxsize)
	{
		if (!::IsWindow(hWnd))
			return nullptr;
		::GetClassName(hWnd, str, maxsize);
		return str;
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

