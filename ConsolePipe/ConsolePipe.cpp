#include "pch.h"
#include "ConsolePipe.h"

CConsolePipe::CConsolePipe() :
	m_hStdInPipeRead(NULL),
	m_hStdInPipeWrite(NULL),
	m_hStdOutPipeRead(NULL),
	m_hStdOutPipeWrite(NULL)
{
}

bool CConsolePipe::Create(TCHAR command[])
{
	BOOL result;
	SECURITY_ATTRIBUTES sa = { sizeof(SECURITY_ATTRIBUTES), NULL, TRUE };
	result = CreatePipe(&m_hStdInPipeRead, &m_hStdInPipeWrite, &sa, 0);
	if (result == FALSE)
		return false;
	result = CreatePipe(&m_hStdOutPipeRead, &m_hStdOutPipeWrite, &sa, 0);
	if (result == FALSE)
		return false;
	STARTUPINFO si = { 0 };
	si.cb = sizeof(STARTUPINFO);
	si.dwFlags = STARTF_USESTDHANDLES;
	si.hStdError = m_hStdOutPipeWrite;
	si.hStdOutput = m_hStdOutPipeWrite;
	si.hStdInput = m_hStdInPipeRead;
	ZeroMemory(&m_Pi, sizeof(m_Pi));
	result = CreateProcess(NULL, command, NULL, NULL, TRUE, 0, NULL, NULL, &si, &m_Pi);
	if (result == FALSE) 
		return false;
	return true;
}

int CConsolePipe::Write(const char * buf, int bufsize)
{
	DWORD dwWritten = 0;
	WriteFile(m_hStdInPipeWrite, buf, bufsize, &dwWritten, NULL);
	return dwWritten;
}

int CConsolePipe::Read(char * buf, int bufsize)
{
	DWORD dwRead = 0;
	ReadFile(m_hStdOutPipeRead, buf, bufsize, &dwRead, NULL);
	buf[dwRead] = '\0';
	return dwRead;
}

int CConsolePipe::Close()
{	
	DWORD dwExitCode = 0;
	TerminateProcess(m_Pi.hProcess, 0);
	CloseHandle(m_hStdOutPipeRead);
	CloseHandle(m_hStdInPipeWrite);
	CloseHandle(m_hStdOutPipeWrite);
	CloseHandle(m_hStdInPipeRead);
	m_hStdInPipeRead = m_hStdInPipeWrite = m_hStdOutPipeRead = m_hStdOutPipeWrite = NULL;
	GetExitCodeProcess(m_Pi.hProcess, &dwExitCode);
	return dwExitCode;
}
