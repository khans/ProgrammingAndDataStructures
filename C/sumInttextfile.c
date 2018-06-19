//Write a function that sums up integers from a text file, one int per line.
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sum(){
    return 1;
}
int main(){
    //first I will create a text file:
    FILE *iniptr;
    iniptr = fopen("iniptr.txt","w");
    if (!iniptr){
        return 1;
    }
    for(int i= 0; i<10;i++){
        if (i!=9){
            fprintf(iniptr,"%d\n",i);
        }
        else
            fprintf(iniptr,"%d",i);
    }
    fclose(iniptr);
    
    iniptr = fopen("iniptr.txt","r");
    if (!iniptr){
        return 1;
    }
    char vals[100];  int sum = 0;
    while(fgets(vals,100,iniptr)!=NULL){
        printf("num in char is %s",vals);
        int temp = atoi(vals);
        printf("Number in dig is:    %d\n",temp);
        sum += temp;
        
    }
    printf("Sum is %d\n",sum);
    
    fclose(iniptr);
    
    
    return 0;
}