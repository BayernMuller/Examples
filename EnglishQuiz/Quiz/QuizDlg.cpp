
// QuizDlg.cpp: 구현 파일
//

#include "pch.h"
#include "framework.h"
#include "Quiz.h"
#include "QuizDlg.h"
#include "afxdialogex.h"
#include <fstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CQuizDlg 대화 상자



CQuizDlg::CQuizDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_QUIZ_DIALOG, pParent)
	, mbIsPlaying(false)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

CQuizDlg::~CQuizDlg()
{
	if (mDP)
	{
		delete[] mDP;
	}
}

void CQuizDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_PIC1, m_Pic);
	DDX_Control(pDX, IDC_PIC2, m_Pic2);
	DDX_Control(pDX, IDC_PIC3, m_Pic3);
}

BEGIN_MESSAGE_MAP(CQuizDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON4, &CQuizDlg::OnBnClickedButtonA)
	ON_BN_CLICKED(IDC_BUTTON2, &CQuizDlg::OnBnClickedButtonB)
	ON_BN_CLICKED(IDC_BUTTON3, &CQuizDlg::OnBnClickedButtonC)
	ON_BN_CLICKED(IDC_BUTTON1, &CQuizDlg::OnBnClickedButtonStart)
END_MESSAGE_MAP()


// CQuizDlg 메시지 처리기

void CQuizDlg::CreateQuiz()
{
	if (!mbIsPlaying)
		return;
	mCnt++;
	if (mCnt > mQuiz.size())
	{
		AfxMessageBox(_T("PASS!"));
		mbIsPlaying = false;
		return;
	}
	else if (mScore < 0)
	{
		mbIsPlaying = false;
		AfxMessageBox(_T("FAIL!"));
		return;
	}

	GetDlgItem(IDC_SCORE)->SetWindowText(CString(L"Score: ") + to_wstring(mScore).c_str());
	int quiz = -1;
	do
	{
		quiz = rand() % mQuiz.size();
	} while (mDP[quiz]);
	mDP[quiz] = true;
	mAnswer = rand() % 3;
	memset(mChoise, INT_MAX, sizeof(int) * 3);
	mChoise[mAnswer] = quiz;
	int sec, third;
	do
	{
		sec = rand() % mQuiz.size();
	} while (sec == quiz);
	do
	{
		third = rand() % mQuiz.size();
	} while (third == quiz || third == sec);

	for (int i = 0; i < 3; i++)
	{
		if (mAnswer == i)
			continue;
		if (mChoise[i] == -1)
		{
			mChoise[i] = sec;
			break;
		}
	}

	for (int i = 0; i < 3; i++)
	{
		if (mAnswer == i)
			continue;
		if (mChoise[i] == -1)
		{
			mChoise[i] = third;
			break;
		}
	}
	GetDlgItem(IDC_EDIT2)->SetWindowText(CString(mQuiz[quiz].c_str()));
	CStatic* pic[] = { &m_Pic, &m_Pic2, &m_Pic3 };
	for (int i = 0; i < 3; i++)
	{
		HBITMAP hBitmap = NULL;
		hBitmap = (HBITMAP)LoadImage(0, CString(("list\\"+mQuiz[mChoise[i]]+".bmp").c_str()), IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
		pic[i]->SetBitmap(hBitmap);
	}
}

BOOL CQuizDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
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
	srand(time(NULL));

	ifstream file("list.txt");
	string str;
	while (file >> str)
	{
		mQuiz.push_back(str);
	}
	mDP = new bool[mQuiz.size()];
	

	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
}

void CQuizDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{

	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다.  문서/뷰 모델을 사용하는 MFC 애플리케이션의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CQuizDlg::OnPaint()
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

		CDialogEx::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
HCURSOR CQuizDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CQuizDlg::OnBnClickedButtonA()
{
	if (mAnswer == 0)
	{
		mScore += mQuiz[mChoise[mAnswer]].size();
	}
	else
	{
		mScore--;
	}
	CreateQuiz();
}

void CQuizDlg::OnBnClickedButtonB()
{
	if (mAnswer == 1)
	{
		mScore += mQuiz[mChoise[mAnswer]].size();
	}
	else
	{
		mScore--;
	}
	CreateQuiz();
}

void CQuizDlg::OnBnClickedButtonC()
{
	if (mAnswer == 2)
	{
		mScore += mQuiz[mChoise[mAnswer]].size();
	}
	else
	{
		mScore--;
	}
	CreateQuiz();
}


void CQuizDlg::OnBnClickedButtonStart()
{
	if (mbIsPlaying)
		return;
	CString str;
	GetDlgItem(IDC_EDIT1)->GetWindowText(str);
	mName = str;
	GetDlgItem(IDC_NAME)->SetWindowText(L"Name: " + str);
	mScore = 5;
	GetDlgItem(IDC_SCORE)->SetWindowText(CString(L"Score: ") + to_wstring(mScore).c_str());
	mCnt = 0;
	memset(mDP, 0, sizeof(bool) * mQuiz.size());
	mbIsPlaying = true;
	
	CreateQuiz();
}
