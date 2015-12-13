class Solution:
    # @param A : list of strings
    # @return an integer
    def add(self,st):
        if st!=[]:
            s = int(st[-2])+int(st[-1])
            #print (s,st[-2],st[-1])
            return s, st[:-2]
    def sub(self,st):
        if st!=[]:
            s = int(st[-2])-int(st[-1])
            return s,st[:-2]
    def mul(self,st):
        if st!=[]:
            s = int(st[-2])*int(st[-1])
            return s,st[:-2]
    def div(self,st):
        if st!=[]:
            s = int(int(st[-2])/int(st[-1]))
            return s,st[:-2]
            
    def evalRPN(self, A):
        stack = []
        SUM= A[-1]
        i = 0
        while i<len(A):
            #print (stack,A[i])
            if A[i] =='+':
                t,stack = self.add(stack)
                SUM=t
                stack.append(str(SUM))
            elif A[i]=='-':
                t,stack = self.sub(stack)
                SUM=t
                stack.append(str(SUM))
            elif A[i]=='*':
                t,stack = self.mul(stack)
                SUM=t
                stack.append(str(SUM))
            elif  A[i]=='/':
                t,stack = self.div(stack)
                SUM=t
                stack.append(str(SUM))
            else:
                stack.append(A[i])
            i+=1
        return SUM
        
        
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(str,input().split(' ')))
        print (S.evalRPN(c))


'''
EVALEXP

Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


'''
