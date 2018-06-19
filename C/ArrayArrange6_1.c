/**Function takes Array A of length n and index i, 
rearranges elements st elements less than A[i] are on left
and then between ==A[i] and then greater than A[i] */

#include <stdio.h>
#include <stdlib.h>
#define MAX_COUNT 100
/**
 * 5 3                                                                                                                                                                                                 
98 87 65 4 23 34                                                                                                                                                                                    
98      87      65      4       23  */


/*
 * Following are the invariants during partitioning
 * bottom group : between indiices 0 and sm-1;
 * midd: from sm to eq-1
 * unclassified: eq to lg;
 * top: lg+1 to sizeofarray - 1
 * 
 */
void swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
    return;
} 
 
//Maintain different groups as follows:
void arrange(int *a,int size,int index){
    int pivot = a[index];
    int sm = 0; int eq=0; int lg = size-1;
    while(eq<=lg){          //initially eq is 0 and lg is the size-1 index.
       if (a[eq]<pivot){
           swap(&a[sm],&a[eq]);
           sm++; eq++;
           
       }
       if(a[eq] == pivot){
           ++eq;
       }
       else{    //if a[eq]>pivot
           swap(&a[eq],&a[lg]);
           lg --; 
       }     
       
    }
    
    return ;
}

int main(){
   
    //Take length;
    int n,i;        //n is size of A and i is the index (will be the pivot or the mid))
    scanf("%d%d",&n,&i);
    //Remember i cannot be greater than or equal to n
    int *arr = malloc(n);
    //printf("\n%d  %d",n, i);
    
    for(int j = 0; j<n ;j++){
        int temp;
        scanf("%d",&arr[j]);
    }
    
    for(int j = 0; j<n ;j++){
        printf("%d\t",arr[j]);
    }  
    
    printf("\n%d\n",arr[i]);
   
    arrange(arr,n,i); //send in the array pointer and nuber of elements
    for(int j = 0; j<n ;j++){
        printf("%d\t",arr[j]);
    }  
    
    return 0;
}