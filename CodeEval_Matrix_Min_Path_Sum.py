from sys import argv 
class Solution(object):

    def minimumPath(self,M):
        n = len(M)
        for i in range(n-1,-1,-1):
            l = len(M[i])
            if i==n-1:
                for j in range(l-2,-1,-1):
                    M[i][j]=M[i][j+1]+M[i][j]
            else:
                for j in range(l-1,-1,-1):      #for j in range(0,i+1):
                    if j==l-1:
                        M[i][j] = M[i+1][j] + M[i][j]
                    else:
                        M[i][j] = min(M[i+1][j],M[i][j+1]) + M[i][j]
        #print(M)
        return M[0][0]


if __name__=='__main__':
    
    file_name = argv[1]
    fp = open(file_name,'r')
    contents = [ line.strip('\n') for line in fp]
    i = 0
    while i<len(contents):
        T = []
        S = Solution()
        for j in range(int(contents[i])):
            i+=1
            T.append(list(map(int,contents[i].split(','))))
        print(S.minimumPath(T))
        i+=1
    

'''
Minimum Path Sum

Challenge Description:

You are given an n*n matrix of integers. You can move only right and down. Calculate the minimal path sum from the top left to the bottom right
Input sample:

Your program should accept as its first argument a path to a filename. The first line will have the value of n(the size of the square matrix). This will be followed by n rows of the matrix. (Integers in these rows will be comma delimited). After the n rows, the pattern repeats. E.g.

2
4,6
2,8
3
1,2,3
4,5,6
7,8,9

Output sample:

Print out the minimum path sum for each matrix. E.g.

14
21
'''
