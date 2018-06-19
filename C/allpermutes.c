//Permutations of all strings
#include <stdio.h>
#include <stdlib.h>

// C program to print all permutations with duplicates allowed
#include <stdio.h>
#include <string.h>
 
/* Function to swap values at two pointers */
void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
 
/* Function to print permutations of string
   This function takes three parameters:
   1. String
   2. Starting index of the string
   3. Ending index of the string. */
void permute(char *a, int l, int r)
{
    
    if (l == r){
        printf("%s\n", a);
        return ;
    }
    permute(a,l+1,r);           //It will firstly print the whole string, since it goes until the end
   //else
   //{
    int i;                      
    for (i = l+1; i <= r; i++) {
        if(strncmp(&a[i],&a[l],1)==0){
          continue ;
        } 
        swap(&a[l], &a[i]);
        permute(a, l+1, r);
        swap(&a[l], &a[i]); //backtrack
   }
   //}
}
 
/* Driver program to test above functions */
int main()
{
    char str[] = "AABC";
    int n = strlen(str);
    permute(str, 0, n-1);
    return 0;
}

/*
AABC
AACB
ABAC
ABCA
ACBA
ACAB
BAAC
BACA
BCAA
CABA
CAAB
CBAA
*/