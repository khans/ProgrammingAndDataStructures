#Script to find if the 8th bit is set in a given byte

def bitKnow(byte):
    x = 1<<7
    if(byte&x):
        return True
    return False