#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isPal(char *name, int size){
    int mid = size/2;
    if(size%2==0){              //even size
        for(int i=0,j=size-1;i<mid,j>=mid;i++,j--){
            if(name[i]!=name[j]){
                return false;
            }
        }
    return true;    
    }
    
    else{
        for(int i=0,j=size-1;i<mid,j>mid;i++,j--){
            if(name[i]!=name[j]){
                return false;
            }
        }
        return true;
    }
}


int main(){
    char name[100]; char n[100];
    scanf ("%[^\n]%*c", name); int n1= strlen(name);        //* in scanf clears stdin
    printf("%zu\n",strlen(name));
    fgets(n,100,stdin);        int n2=strlen(n);
    printf("%zu",strlen(n));
    
    bool check = isPal(name,n1);
    printf("%s\n",check?"true":"false");
    check = isPal(n,n2);
    printf("%s\n",check?"true":"false");
    
    
    return 0;
}