#include <iostream>
#include <fstream>
#include <Windows.h>
using namespace std;

int main()
{
	BITMAPFILEHEADER bmfile;
	BITMAPINFOHEADER bminfo;
	ifstream file("filename.bmp", ios::binary);
	const char* table[] =
	{
		"  ", "..", ",,", "ii", "--", "++", "**", "==", "//" ,"&&", "##", "@@", "WW"
	};

	if (not file.is_open())
		return 0;

	file.read(reinterpret_cast<char*>(&bmfile), sizeof(BITMAPFILEHEADER));
	file.read(reinterpret_cast<char*>(&bminfo), sizeof(BITMAPINFOHEADER));

	int padding = 0;
	if ((bminfo.biWidth * 3) % 4 != 0)
		padding = 4 - ((bminfo.biWidth * 3) % 4);

	byte* bytes = new byte[bminfo.biSizeImage];
	file.read(reinterpret_cast<char*>(bytes), bminfo.biSizeImage);
	file.close();

	int detail = 1;
	while (detail)
	{
		cout << "Enter figure of detail. Enter 0 to exit." << endl; 
		cin >> detail;
		if (!detail)
			break;
		
		for (int i = bminfo.biHeight - 1; i >= 0 ; i -= detail)
		{
			byte* pt = &bytes[i * (bminfo.biWidth * 3 + padding)];
			for (int j = 0; j < bminfo.biWidth; j += detail)
			{
				int average = (pt[0] + pt[1] + pt[2]) / 3;
				pt += 3 * detail;
				cout << table[average * 12 / 255];
			}
			cout << '\n';
		}
		cin.get();
	}
	delete[] bytes;
}

