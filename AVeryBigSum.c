/*

Solved For:
You are given an array of integers of size . 
You need to print the sum of the elements 
in the array, keeping in mind that 
some of those integers may be quite large.

*/


#include <stdio.h>

int main(void){
    int n;
    long sum=0;
    scanf("%d", &n);
    long value;
    //long arr[n];
    for (int i=0; i < n; i++) {
        scanf("%li", &value);
        sum += value;
    }
    printf("%li", sum);
    return 0;
}