#include <string>
#include <winsock2.h>
#include <iostream>
#include <sstream>
using namespace std;
#pragma comment(lib,"ws2_32.lib")
#pragma warning(disable:4996)

int main() 
{
	string url = "www.google.com";
	string get_http = "GET / HTTP/1.1\r\nHost: " + url + "\r\nConnection: close\r\n\r\n";

	WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) 
	{
		return -1;
	}

	SOCKET Socket;
	Socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

	hostent* host;
	host = gethostbyname(url.c_str());

	SOCKADDR_IN SockAddr;
	SockAddr.sin_port = htons(80);
	SockAddr.sin_family = AF_INET;
	SockAddr.sin_addr.s_addr = *((unsigned long*)host->h_addr);

	if (connect(Socket, (SOCKADDR*)(&SockAddr), sizeof(SockAddr)) != 0) 
	{
		return -1;
	}

	send(Socket, get_http.c_str(), get_http.size(), 0);

	string html;
	html.reserve(10000);

	char buffer[10000];
	while (recv(Socket, buffer, 10000, 0) > 0)
	{
		html += buffer;
	}
	
	cout << html.c_str() << endl;

	closesocket(Socket);
	WSACleanup();
	cin.get();
	return 0;
}