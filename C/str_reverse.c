#include <stdio.h>
#include <string.h>

int strLen(char *str){
    int i;
    for(i=0;str[i]!='\0';i++){
    }
    return i;
}

void reverse(char *str){
    int len = strLen(str);
    
    char rev[len+1]; memset(rev,'\0',len);
    printf("%s----%d\n",rev,strLen(rev));
    int i,j;
    for(i=len-1,j=0;i>=0,j<len;i--,j++){
        memcpy(&rev[j],&str[i],1);
        printf("%c-----%c\n",rev[j],str[i]);
    }
    rev[j]='\0';
    printf("%s---%d\n",rev,strLen(rev));
    for(i=0,j=0;i,j<len;i++,j++){
        str[i]=rev[j];
    }
    
    
     return ;
    
}

void newRev(char *str){
    int len = strLen(str); int lp = len-1;  //lAST POSITION OR LAST INDEX
    char *start= str;
    
    char *end = &str[len-1];
    for(int i=0;i<len/2;i++){
        char tmp = str[i];
        str[i]=str[lp-i];
        str[lp-i]=tmp;
    }
    puts(start);
    
    
    return ;
}

int main(){
    char testStr[50];
    //scanf("%s",testStr);
    fgets(testStr,50,stdin);
    newRev(testStr);
    strLen(testStr);
    reverse(testStr);
    printf("%s\n",testStr);
    return 0;
}

/** Output
 * Madam I am Adam!
Madam I am Adam!

----0

-----

!-----!
m-----m
a-----a
d-----d
A-----A
 ----- 
m-----m
a-----a
 ----- 
I-----I
 ----- 
m-----m
a-----a
d-----d
a-----a
M-----M

!madA ma I madaM---17

!madA ma I madaM*/