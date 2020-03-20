#include <string>
#include <winsock2.h>
#include <iostream>
#include <sstream>
using namespace std;
#pragma comment(lib,"ws2_32.lib")
#pragma warning(disable:4996)

int main() 
{
	const char* url = "www.google.com";
	ostringstream oss;
	oss << "GET / HTTP/1.1\r\n";
	oss << "Host: " << url << "\r\n";
	oss << "Connection: close\r\n";
	oss << "\r\n";

	WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) 
	{
		return -1;
	}

	SOCKET sock;
	sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

	hostent* host = gethostbyname(url);
	SOCKADDR_IN address;
	address.sin_port = htons(80);
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = *((int*)host->h_addr);

	if (connect(sock, (SOCKADDR*)(&address), sizeof(address))) 
	{
		return -1;
	}

	string str = move(oss.str());
	send(sock, str.c_str(), str.size(), 0);

	string html;
	html.reserve(10000);

	char buffer[10000];
	while (recv(sock, buffer, 10000, 0) > 0)
	{
		html += buffer;
	}

	cout << html.c_str() << endl;

	closesocket(sock);
	WSACleanup();
	cin.get();
	return 0;
}