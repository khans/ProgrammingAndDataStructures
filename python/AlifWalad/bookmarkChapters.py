class Chapter():
  def __init__(self,start):
    self.start = start
class Bookmark():
  def __init__(self,start):
    self.start = start

def findBookmarks(chapters,bookmarks):
  j = 0; k = 0; ans = {}; l = []
  for i in range(len(chapters)-1):
    start = chapters[i].start
    end = chapters[i+1].start
    while (k <= len(bookmarks)):
      if bookmarks[k].start in range(start,end):
        l.append(bookmarks[k].start)
        ans[chapters[i].start]= l
        k += 1
      else:
        break
    l = []
  if len(bookmarks) != 0:
    for i in range (k, len(bookmarks)):
      l.append(bookmarks[k].start)
    ans[chapters[-1].start] = l
  l = []
  return ans
  
chapters = [Chapter(0),Chapter(5000), Chapter(5500),Chapter(7000)]
bookmarks = [Bookmark(2300),Bookmark(5300), Bookmark(5400),Bookmark(8000)]
