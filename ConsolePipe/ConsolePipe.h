#pragma once
#include <Windows.h>	
class CConsolePipe
{
public:
	CConsolePipe();
	
	// Create Pipe. command must be ARRAY. not pointer.
	// If the function success, return value is true.
	bool Create(TCHAR command[]);

	// Write to child progress. buf must have "\r\n" at last. 
	// It returns bytes of written.
	int Write(const char* buf, int bufsize);

	// Read from child progress. 
	// It returns bytes of read.
	int Read(char* buf, int bufsize);

	// Close all file handles and terminate progress.
	// It returns child progress' exit code.
	int Close();
	
private:
	HANDLE m_hStdInPipeRead = NULL;
	HANDLE m_hStdInPipeWrite = NULL;
	HANDLE m_hStdOutPipeRead = NULL;
	HANDLE m_hStdOutPipeWrite = NULL;
	PROCESS_INFORMATION m_Pi;
};

