#ifndef __REQUEST_H__
#define __REQUEST_H__
#include <string>

class Request
{
public:
	Request(int port = 8282);

	static std::string Get(char url[], const char* header = nullptr);
	static std::string Post(char url[], void* data, int len, const char* header = nullptr);

	void SetPort(int port);
	int GetPort(int port);

private:
	static std::pair<char*, char*> devideUrl(char url[]) ;
	int mPort;
};

#endif//__REQUEST_H__