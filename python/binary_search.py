#implement binary search:
def find(n,lst):
    if lst == []:
        return
    lst.sort()
    mid = len(lst)/2
    if n == lst[mid]:
        return mid
    elif n<lst[mid]:
        return find(n,lst[:mid])
    else:
        return find(n,lst[mid: ])
        