'''
Write program to remove duplicate characters from a string. 
Optimize it. Give different strategies to approach the problem.
'''

def rem_duplicates(string):
    if len(string) < 2:
        return string
    new_clean_string = []
    for char in string:
        if char not in new_clean_string:
            new_clean_string.append(char)
        else:
            continue
    return "".join(new_clean_string)