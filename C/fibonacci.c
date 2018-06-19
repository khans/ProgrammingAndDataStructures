//Fibonacci Series

#include <stdio.h>
#include <stdlib.h>

//Iterative  O(n)
void fibonacci(int n){
    int fib[n];
    fib[0]=0; fib[1]=1;
    if(n==0 || n==1){printf("%d\n",fib[n]);}
    if (n>1){
        for(int i=2;i<=n;i++){
            fib[i]= fib[i-1]+fib[i-2];
        }
    printf("%d",fib[n]);
    }
}

//Using Recursion: O(n^2)
int fibor(int n){
    if(n==0 || n==1){return n;}
    if(n>1){
        return fibor(n-1)+fibor(n-2);
    }
}

int main(){
    int x=7;
    fibonacci(x);
    int ans = fibor(x);
    printf("\nRecursion's answer is %d\n",ans);
    return 0;
}