#include <iostream>
#include <string>
#include "Signal.h"
using namespace std;

class object
{
public:
	void method(const string& str, int n)
	{
		cout << str << endl;
		cout << n << endl;
	}
};

void add_and_print(int a, int b, int c)
{
	cout << a + b + c << endl;
}

int main()
{
	Signal<int, int, int> signal;
	signal.connect(add_and_print);
	signal(1, 3, 8);

	object obj;
	string str = "I am methods!";
	Signal<const string&, int> method_singnal;
	method_singnal.connect(&obj, &object::method);
	method_singnal(str, 4);
	method_singnal(str, 5);
}