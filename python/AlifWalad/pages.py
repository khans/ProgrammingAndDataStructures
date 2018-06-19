pages = [['Hello', 'my','name','is','Safa'],['Hello', 'what', 'is', 'your','name','?']]
ans = {}
l = []
for i in range(len(pages)):
  page = set(pages[i])
  for element in page:
    if element not in ans:
      ans[element] = [i]
    else:
      ans[element].append(i)


print (ans)