#include <stdio.h>

float result(int abs, int total){
        float res = (float)abs/total*100;
        return res;
}

int main(void){
        printf("%f%%", result(8, 32));
        return 0;
}
