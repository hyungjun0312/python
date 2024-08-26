#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	long long n;
	scanf("%lld", &n);

	long long five = n / 5;
	long long rest = n % 5;

	if (n < 5) {
		if (n == 3) {
			printf("1");
		}
		else {
			printf("-1");
		}
	}

	else if (five == 1) {
		if (rest == 0)
			printf("%lld", (five));
		else if (rest == 1)
			printf("%lld", (five - 1 + 2));
		else if (rest == 2)
			printf("-1");
		else if (rest == 3)
			printf("%lld", (five + 1));
		else if (rest == 4)
			printf("%lld", (five - 1 + 3));
	}

	else if (five >= 2) {
		if (rest == 0)
			printf("%lld", (five));
		else if (rest == 1)
			printf("%lld", (five - 1 + 2));
		else if (rest == 2)
			printf("%lld", (five - 2 + 4));
		else if (rest == 3)
			printf("%lld", (five + 1));
		else if (rest == 4)
			printf("%lld", (five - 1 + 3));
	}

	return 0;
}