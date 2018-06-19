/**
 * @input X : Integer array corresponding to the X co-ordinate
 * @input n1 : Integer array's ( X ) length
 * @input Y : Integer array corresponding to the Y co-ordinate
 * @input n2 : Integer array's ( Y ) length
 *
 * Points are represented by (X[i], Y[i])
 * 
 * @Output Integer
 *
 */
int coverPoints(int* X, int n1, int* Y, int n2) {
    //n1 size of X and n2 is size of Y;
    int cover = n1-1; int d=0;
    if(n1!=n2){
        return 0;
    }
    int path = 0;
    int i = 1; int dir = 0;
    
    int currx = X[0]; int curry = Y[0];
    int nextx = X[i++]; int nexty = Y[i++];
    while(1){
       
        if(nextx-currx ==1 && nexty == curry){
        path++;  
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++]; if (i>n1-1){ break;}
        }
        else if (currx-nextx ==1 && curry == nexty){
        d ++;    path++;
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++]; if (i>n1-1){ break;}
        }
        else if (currx==nextx && nexty-curry == 1) {
        d ++;   path++; 
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        if (i>n1-1){ break;}
        }
        else if (currx==nextx && curry-nexty == 1) {
        d ++;    path++;
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        if (i>n1-1){ break;}
        
        }
        else if (nextx-currx ==1 && curry-nexty == 1) {
        d ++;  path++;
        if (i>n1-1){ break;}
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        }
        else if (nextx-currx==1 && nexty-curry == 1) {
        d ++;    path++;
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        if (i>n1-1){ break;}
        }
        else if (nextx-currx == 1 && nexty-curry == 1) {
        d ++;  path++;
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        if (i>n1-1){ break;}
        }
        else if (nextx-currx == 1 && curry-nexty == 1) {
        d ++;   path++;
        currx = nextx; curry = nexty;
        nextx = X[i++]; nexty = Y[i++];
        if (i>n1-1){ break;}
        }
    }
    
    printf("path is %d",path);
}
