class MinStack: 
    def __init__(self):
        self.stack = []
        self.min = []
        
    # @param x, an integer
    def push(self, x):
        if self.min!=[]:
            if x<self.min[-1]:  self.min.append(x)
        else: self.min.append(x)
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack!=[]:
            cm = self.stack.pop(-1)
            if self.min != [] and cm==self.min[-1]:    #i.e the current min is the least
                self.min.pop(-1)    #also we are not adding dplicates during push
                
    # @return an integer
    def top(self):
        if self.stack!=[]:
            return self.stack[-1]
        else:
            return -1
        
    # @return an integer
    def getMin(self):
        if self.min!=[]:
            return self.min[-1]
        else:
            return -1

    def Print(self):
        return self.stack
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = MinStack()
        c = list(map(int,input().split(' ')))
        for j in range(len(c)):
            S.push(i)
        S.pop()
        print (S.top())
        S.pop()
        print (S.getMin())
        
        


'''
MINSTACK

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        push(x) – Push element x onto stack.
        pop() – Removes the element on top of the stack.
        top() – Get the top element.
        getMin() – Retrieve the minimum element in the stack.

Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1

    NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor. 
'''
