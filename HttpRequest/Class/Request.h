#ifndef __REQUEST_H__
#define __REQUEST_H__
#include <string>

class Request
{
public:

	static std::string Get(char url[], const char* header = nullptr);
	static std::string Post(char url[], void* data, int len, const char* header = nullptr);

private:
	static std::pair<char*, char*> devideUrl(char url[]) ;
};

#endif//__REQUEST_H__