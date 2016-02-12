def prody(N,memo):
    print (memo)
    if N in memo:   return memo[N]
    elif N==1:
        memo[1]=1
    elif N==2:
        memo[2]=2
    elif N==3:
        memo[3]=3
    else:
        maxy = 0
        for i in range(1,int(N/2)+1):
            print (i,N)
            maxy = max(maxy,i*(N-i),prody(N-i,memo)*i)
        memo[N]=maxy
    return memo[N]
            
#7412080755407364  
def maxProd(N):
    if N<4:    return N-1
    else:
        memo = {}
        return prody(N,memo)

            
if __name__=='__main__':
    n = int(input())
    for j in range(n):
        s = int(input())
        print (maxProd(s))

'''
Dynamic Programming
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.

Examples:

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)
'''
