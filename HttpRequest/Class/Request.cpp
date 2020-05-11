#include "Request.h"
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netdb.h>
#include <cstring>
#include <sstream>



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

	int sock;
	sockaddr_in serv_sock;

	sock = socket(PF_INET, SOCK_STREAM, 0);
	if (sock == -1)
	{
		return "socket() ERROR";
	}
	
	auto hostname = gethostbyname(host.first);
	std::memset(&serv_sock, 0, sizeof(sockaddr_in));
	serv_sock.sin_family = AF_INET;
	serv_sock.sin_addr.s_addr = *((int*)hostname->h_addr_list[0]);
	serv_sock.sin_port = htons(9090);

	if (connect(sock, (sockaddr*)&serv_sock, sizeof(sockaddr_in)) == -1)
	{
		return "connect() ERROR";
	}

	return str; // RVO
}

std::string Request::Post(char url[], void* data, int len, const char* header)
{
	std::string str;
	return str; // RVO
}

std::pair<char*, char*> Request::devideUrl(char url[])
{
	char* domain = const_cast<char*>(url);
	char* other = nullptr;
	for (int i = 0; domain[i]; i++)
	{
		if (domain[i] == '/')
		{
			domain[i] = '\0';
			other = domain + i + 1;
		}
	}
	return std::make_pair(domain, other);
}
