#include <stdio.h>

int main(){
    int A[4][3] ={  { 1, 2, 3 },
                    { 4, 5, 6 },
                    { 7, 8, 9 },
                    { 15,16,17}
                 };
                 
    int C[2][2] ={{1,2},{3,4}};
    int rows = 4; int cols = 3;
    int T=0;
    int B= rows-1;
    int L=0;
    int R=cols-1;
    
    int totsz = rows*cols; 
    int result[totsz+1];
    
   // int i,j,k;
    int k=0;
    int d=0;
    
    while(T<=B && L<=R){
        if(d==0){           //Traverse from Left to Right
            for(int j=L;j<=R;j++){
                result[k++]=A[T][j];
            }
            T++;    //row change
          
        }
        else if(d==1){       //Traverse from Top to Bottom
            for(int i=T;i<=B;i++){
                result[k++]=A[i][R];
            }
            R--;
            
        }
        else if(d==2){   //Traverse from Right to Left //row is not changing, column is changing
            for(int j=R;j>=L;j--){
                result[k++]=A[B][j];
            }
            B--;
            
        }
        else if(d==3){       //Traverse from bottom to top; row changes, column doesn't;
            for(int i=B;i>=T;i--){
                result[k++]=A[i][L];
            }
            L++;
            
        }
        d=(d+1)%4;
    }
    
    for(int x = 0; x<totsz;x++){
        printf("%d    ",result[x]);
    }
    return 0;
}