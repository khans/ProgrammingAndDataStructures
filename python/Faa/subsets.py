#'ABCD' => '1111'
import sys
given = [1,2]
n = len(given)
p = 1<<n
for i in range(p):
  pos = n-1
  bitmask = i
  sys.stdout.write ('{')
  while(bitmask > 0):
    if (bitmask & 1):
      sys.stdout.write (str(given[pos]))
      sys.stdout.write (',')
    bitmask >>= 1
    pos -= 1
  sys.stdout.write ('}')
  