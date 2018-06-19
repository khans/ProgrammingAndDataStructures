from sys import stdin

def fibonacci(pos):
    if len(fib) < pos+1:
        diff = pos+1 - len(fib)
        i = 0
        while (i<diff):
            sum = fib[-1]+fib[-2]
            fib.append(sum)
            i += 1
        print (fib[-1])
    else:
        print (fib[pos])
'''       
try:
    while(True):
        n = input()
        if n.strip() == '':
            break
        fib = []
        fib.insert(0,0)
        fib.append(1)
        fibonacci(int(n))
except EOFError:
    pass
'''
lines = stdin.readlines()
for line in lines:
    line.strip()
    fib = []
    fib.insert(0,0)
    fib.append(1)
    fibonacci(int(line))
    