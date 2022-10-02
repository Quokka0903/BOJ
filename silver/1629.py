import sys
a, b, c = map(int,sys.stdin.readline().split())

def gop (a,n):
  if n == 1:
      return a%c
  else:
      nums = gop(a,n//2)
      if n %2 ==0:
          return (nums * nums) % c
      else:
          return (nums  * nums *a) % c
          
print(gop(a, b))