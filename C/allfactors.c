#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int sqrt(int n){
    
}

int* allFactors(int A, int *length_of_array) {
	// SAMPLE CODE
        /*
         * *length_of_array = 1000; // length of result array
         * int *result = (int *) malloc(*length_of_array * sizeof(int));
         * // DO STUFF HERE. NOTE: length_of_array is inaccurate in this example. 
         * return result;
         */
        int *result = (int*) malloc(*length_of_array*sizeof(int));
        memset(result,'\0',*length_of_array*(sizeof(int)));
        //we want factors
        result[0]= 1;
        int i,j,q;
        for(i=1,j=2;j<=sqrt(A);j++){
            if(A%j==0){
                q = A/j;
                result[i]=j; result[i+1]=q;
                i +=2;
            }
            else i++;
        }
        result[i]=A;
        return result;
}

int main(){
    int A=85463;int x = 1000;
    int *res = allFactors(A, &x);
    //puts(res);
    for(int i =0;i<1000;i++){
        printf("res is %d\n",res[i]);
    }
    return 0;
}