#Define a procedure,

#hashtable_lookup(htable,key)

#that takes two inputs, a hashtable
#and a key (string),
#and outputs the value associated
#with that key.

def hashtable_update(htable,key,value):
    if hashtable_lookup(htable,key) == None:     # simply add
        hashtable_add(htable,key,value)
    else:
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key and entry[1] != value:
                entry[1] = value
                return
        return 

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])    


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

newHT = make_hashtable(3)   # [[],[],[]]
print (hash_string('udacity',3))
print (hash_string('idacity',3))
print (hash_string('vdacity',3))

hashtable_add(newHT,'udacity',128)
hashtable_add(newHT,'udacity',139)
hashtable_add(newHT,'idacity',127)
hashtable_add(newHT,'vdacity',124)
print (newHT)
hashtable_update(newHT,'udacity', 140)
hashtable_update(newHT,'pdacity', 140)
print (newHT)

