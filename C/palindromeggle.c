#include <stdio.h>
#include <string.h>

int paliFunc(char *input, int len){
    char *start = input;        //pointer to start
    char *end = &input[len-1];  //pointer to end
    
    
    
    while(start<=end){
        
        if((*start=='6' && *end !='9') || (*start=='9' && *end!='6')){
            printf("Nope 6 9 issues\n"); return -1;
            
        }
        if((*start =='1' || *start =='0' || *start=='8') && (*start!=*end)){
            printf("%c----%c\n",*start,*end);
            printf("Doesn't match\n"); return -1;
        }
        
       
        else{
            start++; end--;
        }
    }
    return 0;
    
}

int main(){
    //input is of type ="1691";
    //output will be true only if we turn it at 180 degree the nuber string should look the same
    
    char input[5]="62";//5 for '\0' at the end
    int len = strlen(input); printf("len is %d\n",len);
    int ans = paliFunc(input,len);
    printf("\nThe answer is %d\n",ans);
    return 0;
    
}