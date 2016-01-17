class Solution:
    # @param A : string
    # @return a list of strings
    gp = {
        '0':'0',
        '1':'1',
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}
    def letterCombinations1(self, A,stack):
        if A=='':
            return stack
        else:
            if stack==[]:
                stack = list(self.gp[A[0]])
                #for i in self.gp[A[0]]:
                #    stack.append(i)
            else:
                ts = stack
                stack = []
                for j in ts:
                    for i in self.gp[A[0]]:
                        stack.append(j+i)
            return self.letterCombinations1(A[1:],stack)
            
    def letterCombinations(self,A):
        stack = []
        return  self.letterCombinations1(A,stack)
 
        

    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = input()
        print (S.letterCombinations(c))
        


'''
LETTERPHONE

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Make sure the returned strings are lexicographically sorted.
'''
