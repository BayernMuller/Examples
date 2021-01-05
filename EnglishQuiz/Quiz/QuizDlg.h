
// QuizDlg.h: 헤더 파일
//

#pragma once
#include <vector>
#include <string>
using namespace std;

// CQuizDlg 대화 상자
class CQuizDlg : public CDialogEx
{
// 생성입니다.
public:
	CQuizDlg(CWnd* pParent = nullptr);	// 표준 생성자입니다.
	~CQuizDlg();
// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_QUIZ_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 지원입니다.


// 구현입니다.
protected:
	HICON m_hIcon;
	vector<string> mQuiz;
	CString mName;
	bool mbIsPlaying;
	int mAnswer;
	int mScore;
	int mCnt;
	int mChoise[3];
	bool* mDP;
	void CreateQuiz();
	// 생성된 메시지 맵 함수
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	CStatic m_Pic;
	CStatic m_Pic2;
	CStatic m_Pic3;
	afx_msg void OnBnClickedButtonA();
	afx_msg void OnBnClickedButtonB();
	afx_msg void OnBnClickedButtonC();
	afx_msg void OnBnClickedButtonStart();
};
