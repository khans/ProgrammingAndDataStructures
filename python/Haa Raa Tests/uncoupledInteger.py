n = input()
n.strip()
numbers = [int(x) for x in n.split(',')]

ans = 0
for each in numbers:
    ans = ans ^ each

print (ans)