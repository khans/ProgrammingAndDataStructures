//Anagram question
/**Write a method to decide if two strings are anagrams or not? 

Wikipedia: 
An anagram is a type of word play, the result of rearranging the 
letters of a word or phrase to produce a new word or phrase, using all the original letters
exactly once; e.g., orchestra = carthorse, 
A decimal point = I'm a dot in place. 
In O(n+m) time*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool anagram(char *str1, char*str2, int n1, int n2){
    int allChar[256]={0};   //characters can only be between 0 to 255, set all to 0
    for (int i=0;i<n1;i++){
        allChar[str1[i]]++;     //increment the value at that index
    }
    
    for(int j=0;j<n2;j++){
        allChar[str2[j]]--;     //decrement the value at that index
    }
    
    for (int k=0;k<256;k++){
        if (allChar[k]!=0){ 
            return false;
        }
    }
    return true;
}

int main(){
    printf("Please give us two strings\n");
    
    char str1[100];
    char str2[100];
    fgets(str1,100,stdin);
    fgets(str2,100,stdin);
    int n1 = strlen(str1); int n2 = strlen(str2);
    printf("%zu-----------------%zu",strlen(str1),strlen(str2));
    bool isAnagram;
    if(n1!=n2){
        isAnagram = false;
    }
    else{
        isAnagram = anagram(str1,str2,n1,n2);
    }
    
    printf("The answer is %s",(isAnagram?"true":"false"));
    
     
    return 0;
    
}

//This is O(n)

