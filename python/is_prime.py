def is_prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        else:
            return True
