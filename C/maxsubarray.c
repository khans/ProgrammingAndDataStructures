//Maxsubarray
#include <stdio.h>

int calsum(int *A, int start, int end){
    int total = 0;
    for(int i=0;i<=end;i++){
        total += A[i];
    }
    return total;
    
}

int max(int val1,int val2){
    if (val1<=val2){
        return val2;
    }
    else if (val1>val2){
        return val1;
    }
}

int main(){
    int A[] = {-2,1,-3,4,-1,2,1,-5,4};
    int n1 = sizeof(A)/sizeof(A[0]);
    int start,stptr;
    start = 0; int maximum;
    int prevS, currS = 0;
    maximum = calsum(A,0,n1-1);
    
    
    while(start<n1){
        for(stptr=start; stptr<n1; stptr++){
            currS += A[stptr];
            maximum = max(currS,maximum);
        }
        start++; currS=0;
    }
    printf("The maximum is: %d\n",maximum);
    return 0;
    
}