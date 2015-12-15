from math import sqrt
class Solution:
    # @param A : integer
    # @return a list of strings
    def isValidSudoku(self, A):
        row = {} 
        col = {} 
        cel = {}
        gs = int(sqrt(len(A)))
        for i in range(len(A)):             #len(A)=9
            for j in range(len(A[i])):      #len(A[i])=9
                c = A[i][j]
                if c=='.':   continue                
                if row.get(i)==None:
                    row[i]=[]
                    row[i].append(c)
                elif c in row[i]:    return False
                else:   row[i].append(c)

                if col.get(j)==None:
                    col[j]=[]
                    col[j].append(c)
                elif c in col[j]:    return False
                else:   col[j].append(c)

                grid = (i) + (j/gs)
                print (grid)
                if cel.get(grid)==None:
                    cel[grid]=[]
                    cel[grid].append(c)
                elif c in cel[grid]:  return False
                else:   cel[grid].append(c)
        return True


          
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c= list(map(str,input().split(',')))
        print (S.isValidSudoku(c))

'''


Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]

A partially filled sudoku which is valid.

    Note:

        A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
