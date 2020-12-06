#include <stdio.h>

int stare(int left, int weak = 0)
{
	if (weak)
		weak--;
	if (!left)
		return 1;
	int sum = stare(left - 1);
	if (left > 1)
		sum += stare(left - 2);
	if (left > 2 && weak == 0)
		sum += stare(left - 3, 3);
	return sum;
}

int main()
{
	printf("%d\n", stare(3));
}

