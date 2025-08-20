include <stdio.h>

float result(float x, float y){
	float res = x/y;
	return res;
}
int main(void){
	printf("%f", result(5.0,25.0/7.0));
	return 0;
}
