//Accept an arranged array from user and a val and ee if that number exists.
//Return the index of the matching number in the array
//Iterative method
//Simple logic l,r,m  l=0,r=n-1,m=l+r/2; if val==a[m] return m; else if val>a[m]; l=m+1 else r=m-1; until min<=max;

#include <stdio.h>

int ibSearch(int *array, int *val, int sz){
    /**
     * First cover corner cases*/
    if(sz == 0){ printf("Error!\n"); return 0;}
    if(sz == 1){
        printf("Answer is %d", (array[sz-1]==*val)?0:-1);    
    }
    
    
    int min= 0;
    int max = sz-1;
    int mid = (min+max)/2;

    while(min<=max){
        
        if(*val==array[mid]){
            printf("min2 =%d, mid3=%d, max4=%d\n",min,mid,max);
            return mid;
        }
        
        if (*val>array[mid]){
            min = mid+1;
            mid = (min+max)/2;
            printf("min =%d, mid=%d, max=%d\n",min,mid,max);
           
        }
        if(*val<array[mid]) {
            max = mid-1;
            mid = (min+max)/2;
            printf("min1 =%d, mid1=%d, max1=%d\n",min,mid,max);
        }
        
    }
    return -1;    
}

int rbSearch(int *array, int*val, int min, int max){
   // if(max < 0){ printf("Error!\n"); return 0;}
    //if(max == 0){
    //   return ((array[0]==*val)?0:-1);    
    //}
    if(min<=max){
        int mid = (min+max)/2;
    
        if(*val==array[mid]){printf("arrmin1 =%d, arrmid1=%d, arrmax1=%d\n",array[min],array[mid],array[max]);return mid;}
        else if(*val>array[mid]){printf("arrmin2 =%d, arrmid2=%d, arrmax2=%d\n",array[min],array[mid],array[max]); min = mid+1; return rbSearch(array,val,min,max);}
        else if(*val<array[mid]){printf("arrmin3 =%d, arrmid3=%d, arrmax3=%d\n",array[min],array[mid],array[max]); max = mid-1; return rbSearch(array,val,min,max);}
    }
    return -1;
    
}


int main(){
    printf("Please tell us the size of your array and the number you are searching for:");
    int sz,num;
    scanf("%d%d",&sz,&num);
    int tArray[sz];
    
    
   
    //Now main part
    for(int i = 0; i<sz; i++){
        int in;
        scanf("%d",&in);
        tArray[i]=in;
    }
    
    for(int j=0;j<sz;j++){
        printf("\n--->%d",tArray[j]);
    }
    printf("\n");
    int min = 0; int max = sz-1;
    printf("\n%d\n",rbSearch(tArray,&num,min,max));
    return 0;
}