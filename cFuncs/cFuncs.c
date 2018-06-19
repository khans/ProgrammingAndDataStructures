//Struct for rotation function
struct Results solution1(int A[], int N, int K) {
    struct Results result;
    // write your code in C99 (gcc 4.8.2)
    int r; r = K%N; //Number of times to rotate will depend on the size of the Array
    int temp; 
    
    while(r!=0){
        temp = A[N-1];
        for(int i =1; i<=N-1;i++){
            A[N-i]=A[N-i-1];
        }
        A[0]=temp;
        r--;
    }
    result.A = A;
    result.N = N;
    return result;
}

//unpaired element in array
int solution2(int A[], int N) {
    // write your code in C99 (gcc 4.8.2)
    //XOR bitiwise, if they match the XOR is 0 ele the XOR is different.
    int x = 0;
    for(int i=0;i<N;i++){
        x = x^A[i];
    }
    return x;
}

//time complexity codility
int retMin(int a, int b){
    return (a<=b)?a:b;
}
int solution3(int A[], int N) {
    // write your code in C99 (gcc 4.8.2)
    int sum = 0; int absmin = 0; int min= 0;
    //Calculate the sum of all integers
    for(int i=0; i<N; i++){
        sum = sum+A[i];
    }
    int ini =0;
    for(int i=0; i<N; i++){
        sum = sum-A[i];
        ini = A[i]+ini;
        min = abs(ini-sum);
        absmin = (i==0)?min:retMin(absmin,min);        
    }
    return absmin;
    
}