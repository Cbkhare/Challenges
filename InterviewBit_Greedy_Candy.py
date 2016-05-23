from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
import collections
from operator import itemgetter as ig 

        
class Solution:
    def candy(self, ratings):
        L = len(ratings)
        C = [1 for i in range(L)]
        for i in range(1, L):
            if ratings[i] > ratings[i - 1]:
                C[i] = C[i - 1] + 1
        for i in range(L - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                C[i] = max(C[i], C[i + 1] + 1)
        return sum(C)      
                

if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        a = list(map(int,Si.readline().split()))
        print (S.candy(a))

'''


There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

        Each child must have at least one candy.
        Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Sample Input :

Ratings : [1 2]

Sample Output :

3

The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor. So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.

'''
