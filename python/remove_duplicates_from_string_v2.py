def rem_duplicates(string):
    if len(string) < 2:
        return string
    new = set()
    for c in string:
        new.add(c)
    
    return "".join(new)