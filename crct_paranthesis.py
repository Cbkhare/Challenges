from sys import argv 
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []      #Real Stack
        Graph = {
        ']':'[',
        '}':'{',
        ')':'('
        }

        for e in A:
            if e in ['[','{','(']:
                stack.append(e)
            else:
                if stack==[] or Graph[e]!=stack[-1]:
                    return False
                else:
                    stack.pop(len(stack)-1)     #pop last 
        if len(stack) ==0:
            return True
        else:
            return False
              
if __name__=='__main__':
    file_name = argv[1]
    fp =open(file_name,'r+')
    B = Solution()
    for line in fp:
        print (B.isValid(line.strip('\n')))
'''
 Given a string comprising just of the characters (,),{,},[,] determine if it is well-formed or not.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a string comprising of the characters mentioned above. E.g.

()
([)]

Output sample:

Print out True or False if the string is well-formed. E.g.

True
False
'''
