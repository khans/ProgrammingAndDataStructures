//sprintf() and sscanf() implementation

#include <stdio.h>
#include <string.h>

int main(){
    char array[80];
    int num1=1;
    int num2=2;
 
    sprintf(array,"%d" "%d", num1, num2);
    puts(array);        //appends newline character
 
    char data[]="$23.45 10";
    char dol;
    float price;
    int units;
 
    sscanf(data,"%c%f %d", &dol,&price,&units);
    printf("\n%c%5.2f %d\n", dol, price, units);
    
    printf("=============================================================\n");
    char string[]="Hi there";
    printf("as is   : %s:\n",string);
    printf("format 1: %2s:\n",string);
    printf("format 2: %20s:\n",string);
    printf("format 3: %-20s:\n",string);
 
    /*char *c = "Hello";
    char d[6];
    while(*c++=*d++){
        printf("Hi\n");
    }*/
    
    char x[10];
    char y[] = "Hello";
    int i = 0;
    while(y[i] != NULL){
        printf("%c",y[i]);
        i++;
    }
    printf("\n");
    puts(x);
        
    
    return 0;
    
    

    
}