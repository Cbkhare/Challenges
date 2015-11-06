class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):

        #Note X[0] == Y[0]
        dis = 0 
        for i in range(1,len(X)):
            dis += max(abs(X[i-1]-X[i]),abs(Y[i-1]-Y[i]))
            #calculating x
            #x,y =0,0
            #x = abs(X[i-1]-X[i])
            #y = abs(Y[i-1]-Y[i])
            #dis += max(x,y)
        return dis 
        
if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = list(map(int,input().split(', ')))
        b = list(map(int,input().split(', ')))
        print (B.coverPoints(a,b))
        
'''


You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.
'''
