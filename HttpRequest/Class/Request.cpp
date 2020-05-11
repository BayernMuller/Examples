#include "Request.h"
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sstream>

Request::Request(int port)
	: mPort(port)
{
}

std::string Request::Get(char url[], const char* header)
{
	std::string str;
	std::ostringstream oss;
	auto host = Request::devideUrl(url);
	oss << "GET /" << host.second << " HTTP/1.1\r\n";
	oss << "Host: " << host.first << "\r\n";
	oss << "Connection: close\r\n";
	if (header)
	{
		oss << header << "\r\n";
	}

	

	return str; // RVO
}

std::string Request::Post(char url[], void* data, int len, const char* header)
{
	std::string str;
	return str; // RVO
}

void Request::SetPort(int port)
{
}

int Request::GetPort(int port)
{
	return 0;
}

std::pair<char*, char*> Request::devideUrl(char url[])
{
	char* domain = const_cast<char*>(url);
	char* other = nullptr;
	for (int i = 0; domain[i]; i++)
	{
		if (domain[i] == '/')
		{
			domain[]
		}
	}
	return std::make_pair(domain, other);
}
