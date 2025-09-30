#include <stdio.h>
#include <math.h>

float result(double a, double b){
        float res = (float)a/b;
        return res;
}

int main(void){
        printf("%f", result(pow(25,4), pow(5,3)));
}
