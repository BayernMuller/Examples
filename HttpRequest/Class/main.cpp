#include <iostream>
#include "Request.h"
using namespace std;

int main()
{
	char url[] = "www.google.com";
	cout << Request::Get(url) << endl;

	cout << "end" << endl;
}