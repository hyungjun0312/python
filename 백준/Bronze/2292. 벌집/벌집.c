#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);

	
	float i = 1;
	int six = 6;
	int dis = 1;

	while (1) {
		if (n / i > 1) {
			i += six;
			six += 6;
			dis++;
			continue;
		}

		else if (n / i <= 1) {
			printf("%d", dis);
			break;
		}
		break;
	}
	return 0;
}