from ctypes import *
import win32pipe
import win32process
import win32file
import win32con
import win32api
import pywintypes

class console_pipe():
	def __init__(self, path):
		self.hInRead = None;
		self.hInWrite = None;
		self.hOutRead = None;
		self.hOutWrite = None;
		sa = pywintypes.SECURITY_ATTRIBUTES()
		sa.SetSecurityDescriptorDacl(1, None, 0)

		self.hInRead, self.hInWrite = win32pipe.CreatePipe(sa, 0)
		self.hOutRead, self.hOutWrite = win32pipe.CreatePipe(sa, 0)

		si = win32process.STARTUPINFO()
		si.dwFlags = win32con.STARTF_USESTDHANDLES | \
                     win32process.STARTF_USESHOWWINDOW
		si.hStdError = self.hOutWrite
		si.hStdOutput = self.hOutWrite
		si.hStdInput = self.hInRead
		si.wShowWindow = win32con.SW_HIDE

		create_flags = win32process.CREATE_NEW_CONSOLE
		self.info = win32process.CreateProcess(None, path, None, None, \
			True, create_flags, None, None, si)

		if self.info[0]:
			print('create process success')

	def write(self, buf):
		return win32file.WriteFile(self.hInWrite, buf, None)

	def read(self, length):
		return win32file.ReadFile(self.hOutRead, length, None)

	def close(self):
		win32process.TerminateProcess(self.info[0], 0)
		win32api.CloseHandle(self.hInRead)
		win32api.CloseHandle(self.hInWrite)
		win32api.CloseHandle(self.hOutRead)
		win32api.CloseHandle(self.hOutWrite)