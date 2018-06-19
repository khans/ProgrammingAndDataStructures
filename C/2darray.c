#include <stdio.h>
int main(){
    int B[2][3]; int cnt = 1;
    for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            B[i][j]= cnt++;
        }
    }
    
    for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            printf("%d------",B[i][j]);
        }
        printf("\n");
    }
    
    printf("=========================================================\n");
    printf("B is %d\n",B);      printf("*B is %d\n",*B);  //B is &B[0]  and *B is B[0] which is &B[0][0]
    printf("B+1 is %d\n",B+1);  printf("*(B+1) is %d\n",*(B+1));  //B+1 is &B[1]  and *B is B[0] which is &B[1][0]
    printf("*(B+1)+2 is %d\n",*(B+1)+2);        //this is &B[1][0]+2, this is ptr arithmetic and this will be address+8
    
    
 return 0;
 }
