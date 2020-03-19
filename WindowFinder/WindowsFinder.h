#pragma once
#include <Windows.h>

class WindowsFinder
{ 
public:
	template<class Container>
	static bool Find(Container* set)
	{
		return EnumWindows(&WindowsFinder::GetWindowsList<Container>, LPARAM(set));
	}
	
	template<class Container>
	static bool Find(WNDENUMPROC lpEnumFunc, Container* set)
	{
		return EnumWindows(lpEnumFunc, LPARAM(set));
	}

	template<class Container>
	static WNDENUMPROC GetCallbackFunc()
	{
		return GetWindowsList<Container>;
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
	template<class Container>
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

