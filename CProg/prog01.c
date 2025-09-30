include <stdio.h>

float result(float x, float y){
	float res = (float)x/y;
	return res;
}

int main(){
	printf("%f", result(5.0,25.0/7.0));
}
