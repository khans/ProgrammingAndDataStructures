// Find the largest int value in an int array. //not arranged
#include <stdio.h>
 int main(){
   
     int arr[10]={67,68,54,34,23,8,0,7,4,10};
     int max = arr[0]; 
     for (int i=1;i<10;i++){
         if (max<arr[i]){
             max = arr[i];
         }
     }
     printf("max is %d\n",max);
     
     FILE *fptr;
     fptr = fopen("arraytest.txt","w");
     if(!fptr){
         return 1;
     }
     
     fprintf(fptr,"ok");
     fclose(fptr);
     return 0;
 }