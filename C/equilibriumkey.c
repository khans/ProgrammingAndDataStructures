//Equilibrium key

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int eqKey(int A[], int N){
    
    return 7;
    
    
}

int solution(int N){
    int cnt =0; int max = 0; bool check = false;
    while(N){
        if(N&1){
            if (!check){
                check = true;
            }
            else{
              if(max <=cnt){
                max = cnt;
              }    
            }
            cnt = 0;
        }
        else {
            cnt += 1; 
        }
        N >>= 1;
    }        
    
    return max;
}



int main(){
    int A[8]={-1,3,-4,5,1,-6,2,1};
    //printf("%d",sizeof(A)/sizeof(A[0]));
    int N = 0;
    int eq;
    
    //result = a > b ? x : y;
    eq = (N==0)? -1 : eqKey(A,N);  //ternary operator
    //printf("Equilibrium key is %d\n", eq);
    
    int max = solution(37);
    printf("%d",max);
    
    return 0;
}