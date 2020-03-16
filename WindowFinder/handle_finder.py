import win32gui

class handle_finder:
	def __init__(self):
		self.list = {}

	def get_handle_list(self):
		self.list = {}
		win32gui.EnumWindows(self.callback, 0)
		return self.list

	def get_handle(self, name):
		self.get_handle_list()
		return self.list[name]

	def callback(self, hwnd, param):
		if not win32gui.IsWindowVisible(hwnd):
			return
		if win32gui.GetWindowTextLength(hwnd) == 0:
			return
		if win32gui.GetParent(hwnd):
			return
		self.list.update({win32gui.GetWindowText(hwnd) : hwnd})