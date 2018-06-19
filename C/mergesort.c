#include <stdio.h>
#include <string.h>

//MAIN MERGE FUNCTION
void merge(int *A, int *left, int *right, int n, int nl, int nr){
    int i=0,j=0,k=0;
    while(i<nl && j<nr){
        if (left[i]<=right[j]){
            A[k]=left[i]; i++; k++;
        }
        else{
            A[k]=right[j]; j++; k++;
        }
    }
    //Only one of the following loops will be executed! Waise bhi they are sorte
    while(i<nl){
        A[k]=left[i]; k++;i++;
    }
    while(j<nr){
        A[k]=right[j]; k++;j++;
    }
   
    return ;
    
    
}

//----MERGESORT----
void mergesort(int *A, int n){
    
   if(n<2){
       return;
   }
   else{
       int mid;
       int lftsz; 
       int rtsz;
       mid = n/2;
       lftsz = mid;
       rtsz = n-mid;
       printf("leftsz and rtsz are %d    %d\n",lftsz,rtsz);
       
       int left[lftsz];
       int right[rtsz];
       int i;
       for(i=0;i<lftsz;i++){          //i<=mid-1
            left[i]=A[i];
       }
       
       //printf("Current i is %d\n",i);
       //printf("%d A[i], ",A[i]);
       //------------------CRUCIAL--------------------------- rtsz is the n of right
       for(int k=0; k<rtsz; k++,i++){
           right[k]=A[i];
       }
       //-------------------------------------------
       /*for(int j=0;j<mid;j++){          //i<=mid-1
            printf("left is %d------",left[j]);
       }
        for(int z=0;z<rtsz;z++){          //i<=mid-1
            printf("right is %d------",right[z]);
       }*/
       mergesort(left,lftsz);
       mergesort(right,rtsz);
       merge(A,left,right,n,lftsz,rtsz);
   }
    return;
}

//----MAIN----
int main(){
    int A[] = {12, 45, 32, 28, 4, 9, 7, 3, 1};
    int n = sizeof(A)/sizeof(A[0]);         //size of the array
    
    mergesort(A,n);
    
    for(int i=0;i<=n-1;i++){
        printf("A at position %d is %d-------------",i,A[i]);
    }
    
    return 0;
    
}