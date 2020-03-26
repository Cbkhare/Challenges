from sys import stdin as si 


def solve(j):
    d = [["" for _ in range(j)] for _ in range(j)]
    # d = [[] for _ in range(j)]

    for x in range(len(d)):
      for y in range(x+1):
        if y%2==0:
            d[x].append('1')
        else:
            d[x].append('0')
      d[x] = d[x][y:] + d[x][::-1][1:]
    

    l = len(d)
    for y in range(l):
      v = ''.join(d[y])
      spc = l-y-1
      d[y] = " "*spc + v
    for x in range(j-2, -1, -1):
      d.append(d[x])
    
    for y in range(len(d)):
      print(d[y])
        

if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        solve(int(si.readline().strip()))
        
        
 """
 4
3
  1
 101
10101
 101
  1
4
   1
  101
 10101
1010101
 10101
  101
   1
1
1
2
 1
101
 1
 """
