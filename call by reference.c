#include<stdio.h>
#include<conio.h>

void Swap(int *x,int *y) {
    int *temp; 
    *temp = *x;
    *x = *y;
    *y = *temp;
}

int main() {
    int a=10;
    int b=20;
    printf("Outside the function : ");
    printf("a = %d  and b = %d",a,b);
    Swap(a,b);
    printf("\nAfter the function : ");
    printf("a = %d  and b = %d",a,b);
}