#Fibonacci series to retun the nth number,

def fib(n):
    fibbo = []
    fibbo.append(0)
    fibbo.append(1)
    for i in xrange(2,n+1):
        fibbo.append(fibbo[i-1]+fibbo[i-2])
    return fibbo[n]
    
