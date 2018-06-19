def flip_bit(number,n):
    mask = 0b1<<n-1   # to turn on the nth bit so it will be like 10000 ,,,n-1 0s
    desired = number^mask # xor with the original number to turn on the nth bit and let others remain as it is
    return bin(desired)
    
''' xor 1 1 0   0 0 0   0 1 1   1 0 1
'''
