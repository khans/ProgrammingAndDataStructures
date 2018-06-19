//Randomized Quick sort
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a,int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
    return ;
}

int retRan(int start, int end){
    srand(time(NULL));
    return(rand() % end + start); 
}

int partition(int *A,int start,int end){
    int temp_pin = retRan(start,end);
    int pivot = A[temp_pin];
    int pindex=0;
    for(int i=0;i<=end;i++){
        if (i==temp_pin){
            continue;
        }
        if (A[i]<=pivot){
         swap(&A[i],&A[pindex]);
         pindex++;
        }
    }
    swap(&A[temp_pin],&A[pindex]);
    return pindex;
}


void quicksort(int *A, int start, int end){
    if(start<end){          //No invalid input
        int pindex = partition(A,start,end);
        quicksort(A,start,pindex-1);
        quicksort(A,pindex+1,end);
    }
    else 
        return ;
    
}

int main(){
    int A[] = {24,56,9,8,65,32,1,0,89,34,90,32};
    //int A[] ={1,0};
    int n = sizeof(A)/sizeof(A[0]); //printf("%d\n",n);
    int start = 0; int end = n-1; 
    quicksort(A,start,end);
    printf("A is sorted and this is how it looks like: [");
    for (int i=0; i<n; i++){
        printf("%d ",A[i]);
    }
    printf("]");
    return 0;

}

//Answer is A is sorted and this is how it looks like: [8 1 0 9 24 32 32 34 56 65 90 89 ] 