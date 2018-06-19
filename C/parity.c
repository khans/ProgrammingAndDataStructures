//Parity
#include <stdio.h>
#include <stdbool.h>
bool calParity(int val){
    bool ret = false ;
    int a = 0;
    bool check;
    while(val){
    check = (val&1);
    ret = ret^check;
    printf("%s\n",check?"true":"false");
    val = val>>1; a++;
    }
    printf("a is %d\n",a);
    return ret;
}

bool calAltParity(int val){
    if (val==1){
        return true;
    }
    else if(val==2){
        return true;
    }
    else{
        int a = 0;
        bool ret = false;
        while(val){
            ret = ret^1;        //always xor with 1
            val &= val-1;           //always & val with val-1 and make that the new value of x, this unsets the lowest set bit.
            a += 1;
        }
        printf("\na is %d\n",a);
        return ret;    
    }
}

int main(){
    int val;
    scanf("%i",&val);       //%hi is for short
    bool ans;
    ans = calParity(val);
    if(ans){
        printf("Parity is 1");
    }else{
        printf("Parity is 0");
    }
    
    //Alternative method--by switching off the lowest set bit.
    bool ans2;
    ans2=calAltParity(val);
    printf("\nParity by alternative method is %d\n",ans2?1:0);
    
    
    return 0;
}