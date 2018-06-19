#Staircase Problem
def  StairCase(n):
    if n == 0:
        print ("")
    else:
        i = n-1;
        x = 0;
        y = 0;
        j = 1
        s = ''
        while(i >= 0 and j <= n):
            while (x<i):
                s = s + " "
                x += 1
            while(y<j):
                s = s + "#";
                y += 1
            i -= 1; j += 1
            x =0; y=0;
            print (s);
            s = "";
            
StairCase(100)            