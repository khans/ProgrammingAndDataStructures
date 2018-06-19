from collections import defaultdict
s = 'the song is the best'
d = defaultdict(list)
word = ''
k = 0
last = 0
for i,j in enumerate(s):
  
  if j != ' ':
    word = word+j
    k += 1
  else:
    print(word)
    location = i-k
    print(location)
    d[word].append(location)
    k = 0
    word = ''
    d[j].append(i)
    
  

d[word].append(len(s)-k)
print(d)

total = 0

for k,v in d.items():
  total += len(k)*len(v)
r = ['']*total
for k,v in d.items():
  for each in v:
    for e in k:
      r[each] = e;
      each += 1
sr = ''.join(r)