from sys import stdin as Si, maxsize as m 

class Solution:

    def jump(self,A):
        l = len(A)
        i,count = l-1,0
        while i>0:
            if A[i-1]>=A[i-2]:  i=i-2
            else:   i=i-1
            count+=1
        return count
        
            

    
if __name__=='__main__':

    n = map(int,Si.readline())
    lst = Si.readline().strip('\n').split()

    S = Solution()
    print(S.jump(lst))
    

'''
Emma is playing a new mobile game involving nn clouds numbered from 00 to n−1n−1. A player initially starts out on cloud c0c0, and they must jump to cloud cn−1cn−1. In each step, she can jump from any cloud ii to cloud i+1i+1 or cloud i+2i+2.

There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a thundercloud, but if she reaches the last cloud (i.e., cn−1cn−1), she wins the game!

[jump(1).png]

Can you find the minimum number of jumps Emma must make to win the game? It is guaranteed that clouds c0c0 and cn−1cn−1 are ordinary-clouds and it is always possible to win the game.

Input Format

The first line contains an integer, nn (the total number of clouds).
The second line contains nn space-separated binary integers describing clouds c0,c1,…,cn−1c0,c1,…,cn−1.

    If ci=0ci=0, the ithith cloud is an ordinary cloud.
    If ci=1ci=1, the ithith cloud is a thundercloud.

Constraints

    2≤n≤1002≤n≤100
    ci∈{0,1}ci∈{0,1}
    c0=cn−1=0c0=cn−1=0

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0

Sample Output 0

4

Sample Input 1

6
0 0 0 0 1 0

Sample Output 1

3

'''
