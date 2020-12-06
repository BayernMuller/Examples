
// CaptureDlg.cpp : 구현 파일
//

#include "stdafx.h"
#include "Capture.h"
#include "CaptureDlg.h"
#include "afxdialogex.h"

#include <gdiplus.h>
#include <atlimage.h>
#pragma comment (lib, "Gdiplus.lib")

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

// 구현입니다.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CCaptureDlg 대화 상자

// static 멤버 초기화
CStringArray CCaptureDlg::m_strArray;
vector<CWnd*> CCaptureDlg::m_pWnds;

CCaptureDlg::CCaptureDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(IDD_CAPTURE_DIALOG, pParent)
	, m_option(0)
	, m_saveoption(0)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CCaptureDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_PICTURE, m_picture);
	DDX_Radio(pDX, IDC_RADIO1, m_option);
	DDX_Radio(pDX, IDC_RADIO3, m_saveoption);
	DDX_Control(pDX, IDC_LIST1, m_list);
}

BEGIN_MESSAGE_MAP(CCaptureDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, &CCaptureDlg::OnBnClickedButtonSave)
	ON_BN_CLICKED(IDC_BUTTON2, &CCaptureDlg::OnBnClickedButtonRefresh)
	ON_BN_CLICKED(IDC_RADIO1, &CCaptureDlg::OnBnClickedRadio1)
	ON_BN_CLICKED(IDC_RADIO2, &CCaptureDlg::OnBnClickedRadio2)
	ON_WM_TIMER()
	ON_BN_CLICKED(IDC_RADIO4, &CCaptureDlg::OnBnClickedRadiobmp)
	ON_LBN_SELCHANGE(IDC_LIST1, &CCaptureDlg::OnLbnSelchangeList1)
END_MESSAGE_MAP()


// CCaptureDlg 메시지 처리기

BOOL CCaptureDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 이 대화 상자의 아이콘을 설정합니다.  응용 프로그램의 주 창이 대화 상자가 아닐 경우에는
	//  프레임워크가 이 작업을 자동으로 수행합니다.
	SetIcon(m_hIcon, TRUE);			// 큰 아이콘을 설정합니다.
	SetIcon(m_hIcon, FALSE);		// 작은 아이콘을 설정합니다.

	// TODO: 여기에 추가 초기화 작업을 추가합니다.

	OnBnClickedRadio1();

	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
}

void CCaptureDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다.  문서/뷰 모델을 사용하는 MFC 응용 프로그램의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CCaptureDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트입니다.

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 클라이언트 사각형에서 아이콘을 가운데에 맞춥니다.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 아이콘을 그립니다.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		HDC hdc;
		int cx, cy;
		if (m_option == 0)
		{
			hdc = ::GetDC(NULL);
			cx = GetSystemMetrics(SM_CXSCREEN);
			cy = GetSystemMetrics(SM_CYSCREEN);
		}
		else
		{
			if (::IsWindow(m_pCaptureWnd->m_hWnd))
			{
				hdc = m_pCaptureWnd->GetDC()->m_hDC;
				CRect wndrect;
				m_pCaptureWnd->GetClientRect(&wndrect);
				cx = wndrect.Width();
				cy = wndrect.Height();
			}
			else
			{
				OnBnClickedButtonRefresh();
				return;
			}
		}
		int color_depth = GetDeviceCaps(hdc, BITSPIXEL);

		CClientDC dc(m_picture.GetSafeOwner());
		CRect rect;

		m_picture.GetWindowRect(&rect);
		ScreenToClient(&rect);
		dc.StretchBlt(rect.left, rect.top, rect.Width(), rect.Height(), CDC::FromHandle(hdc), 0, 0, cx, cy, SRCCOPY);
		
		

		CDialogEx::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
HCURSOR CCaptureDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

BOOL CCaptureDlg::GetFilePath(CString & str)
{
	CString strFilter, strDefault;
	if (m_saveoption == 0)
	{
		strDefault = L"jpg file(*.jpg)";
		strFilter = L"jpg file(*.jpg)|*.jpg|";
	}
	else
	{
		strDefault = L"bmp file(*.bmp)";
		strFilter = L"bmp file(*.bmp)|*.bmp|";
	}

	CFileDialog dlg(FALSE, strDefault, L"Untitled", OFN_HIDEREADONLY | OFN_FILEMUSTEXIST, strFilter, NULL);
	if (dlg.DoModal() == IDOK)
	{
		str = dlg.GetPathName();
	}
	else
	{
		return FALSE;
	}
	return TRUE;
}

BOOL CCaptureDlg::GetWindowsList(HWND hWnd, LPARAM lParam)
{
	CWnd* pWnd = nullptr;
	pWnd = CWnd::FromHandle(hWnd);
	if (pWnd)
	{
		if (::IsWindowVisible(hWnd) == FALSE)
			return TRUE;
		if (::GetWindowTextLength(hWnd) == 0)
			return TRUE;
		if (::GetParent(hWnd) != 0)
			return TRUE;
		
		m_pWnds.push_back(pWnd);
		TCHAR name[256] = { 0, };
		TCHAR title[256] = { 0, };

		::GetClassName(hWnd, name, 256);
		::GetWindowText(hWnd, title, 256);
	
		CString str;
		int num = (int)m_strArray.GetCount() + 1;
		str.Format(L"%02d.[%s] [%s]", num, name, title);
		m_strArray.Add(str);
	}
	return pWnd != nullptr;
}

void CCaptureDlg::DeleteWindowsList()
{
	m_pWnds.clear();
	m_list.ResetContent();
	m_strArray.RemoveAll();
}


void CCaptureDlg::OnBnClickedButtonSave()
{
	// TODO: 여기에 컨트롤 알림 처리기 코드를 추가합니다.
	CString str;
	if (GetFilePath(str) == FALSE)
	{
		return;
	}

	if (m_option == 0)
	{
		SendMessage(WM_SHOWWINDOW, FALSE, SW_PARENTCLOSING);
		Sleep(500);
	}

	HDC hdc = nullptr;
	int cx = 0; 
	int cy = 0;

	switch (m_option)
	{
	case 0:
		hdc = ::GetDC(NULL);
		cx = GetSystemMetrics(SM_CXSCREEN);
		cy = GetSystemMetrics(SM_CYSCREEN);
		break;
	case 1:
		if (::IsWindow(m_pCaptureWnd->m_hWnd))
		{
			hdc = m_pCaptureWnd->GetDC()->m_hDC;
			CRect rect;
			m_pCaptureWnd->GetWindowRect(&rect);
			cx = rect.Width();
			cy = rect.Height();
		}
		else
		{
			AfxMessageBox(L"해당 윈도우는 이미 종료되어서 문제가 있습니다.");
			OnBnClickedButtonRefresh();
			return;
		}
		break;
	}

	CImage image;
	int color_depth = GetDeviceCaps(hdc, BITSPIXEL);
	image.Create(cx, cy, color_depth, 0);
	BitBlt(image.GetDC(), 0, 0, cx, cy, hdc, 0, 0, SRCCOPY);
	if (m_saveoption == 0)
	{
		image.Save(str, Gdiplus::ImageFormatJPEG);
	}
	else
	{
		image.Save(str, Gdiplus::ImageFormatBMP);
	}

	::ReleaseDC(NULL, hdc);
	image.ReleaseDC();
	
	if (m_option == 0)
	{
		ShowWindow(SW_SHOW);
	}
}

void CCaptureDlg::OnBnClickedButtonRefresh()
{
	UpdateData(TRUE);
	if (m_option == 1)
	{
		DeleteWindowsList();
		EnumWindows(&CCaptureDlg::GetWindowsList, 0);
		for (int i = 0; i < m_strArray.GetCount(); i++) 
		{
			m_list.AddString(m_strArray[i]);
		}
		if (m_list.GetCount() > 0)
			m_list.SetCurSel(0);
	}
}

void CCaptureDlg::OnBnClickedRadio1()
{
	//DeleteWindowsList();
	UpdateData(TRUE);
	SetTimer(WM_USER + 1, 1000, NULL);
}


void CCaptureDlg::OnBnClickedRadio2()
{
	UpdateData(TRUE);
	KillTimer(WM_USER + 1);
	OnBnClickedButtonRefresh();
	OnLbnSelchangeList1();
}

void CCaptureDlg::OnTimer(UINT_PTR nIDEvent)
{
	if (nIDEvent == WM_USER + 1)
	{
		CRect rect;
		::GetWindowRect(m_picture.m_hWnd, &rect);
		ScreenToClient(&rect);
		InvalidateRect(rect, FALSE);
	}
	CDialogEx::OnTimer(nIDEvent);
}

void CCaptureDlg::OnBnClickedRadiobmp()
{
	UpdateData(TRUE);
}


void CCaptureDlg::OnLbnSelchangeList1()
{
	if (m_list.GetCount() > 0)
	{
		int num = m_list.GetCurSel();
		m_pCaptureWnd = m_pWnds[num];
		Invalidate(FALSE);
	}
}
