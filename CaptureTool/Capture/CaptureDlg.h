
// CaptureDlg.h : ��� ����
//

#pragma once
#include "afxwin.h"
#include <vector>

using namespace std;

// CCaptureDlg ��ȭ ����
class CCaptureDlg : public CDialogEx
{
// �����Դϴ�.
public:
	CCaptureDlg(CWnd* pParent = NULL);	// ǥ�� �������Դϴ�.

// ��ȭ ���� �������Դϴ�.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_CAPTURE_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV �����Դϴ�.


// �����Դϴ�.
protected:
	HICON m_hIcon;

	// ������ �޽��� �� �Լ�
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()

private:
	BOOL GetFilePath(CString &str);
	static BOOL __stdcall GetWindowsList(HWND hWnd, LPARAM lParam);
	void DeleteWindowsList();

public:
	CStatic m_picture;
	int m_option;
	int m_saveoption;
	CListBox m_list;
	
	CWnd* m_pCaptureWnd;
	static CStringArray m_strArray;
	static vector<CWnd*> m_pWnds;

	

	afx_msg void OnBnClickedButtonSave();
	afx_msg void OnBnClickedButtonRefresh();
	afx_msg void OnBnClickedRadio1();
	afx_msg void OnBnClickedRadio2();
	afx_msg void OnTimer(UINT_PTR nIDEvent);
	afx_msg void OnBnClickedRadiobmp();
	afx_msg void OnLbnSelchangeList1();
};
