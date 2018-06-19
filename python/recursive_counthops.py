#A child running a flight of stairs, may take 1, 2 or 3 hops, find the number of possible hops
#n is the number of stairs
def counthops(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return counthops(n-1)+counthops(n-2)+counthops(n-3)