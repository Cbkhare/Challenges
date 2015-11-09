class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, lst ):
        stack = []
        lst.sort()
        print (lst)
        i = 0

        while i< len(lst)-1:
            if lst[i+1][0] in range(lst[i][i],lst[i][1]+1):
                if lst[i][1]<=lst[i+1][1]:
                        if [lst[i][i],lst[i+1][1]] not in stack:
                            stack.append([lst[i][i],lst[i+1][1]])
                        lst[0]=[lst[i][i],lst[i+1][1]]
                        lst.pop(1)
                else:
                    if [lst[i][i],lst[i][1]] not in stack:
                            stack.append([lst[i][i],lst[i][1]])
                    lst[0]=[lst[i][i],lst[i][1]]
                    lst.pop(1)
                    #i+=1
            print(stack,lst)
        if len(stack)>=2:
            if stack[-2]<stack[-1]: stack.pop(0)
        return stack         
        '''
        while len(lst)>0:
            if len(lst)>=2:
                if lst[1][0] in range(lst[0][0],lst[0][1]+1):   
                    if lst[0][1]<=lst[1][1]:
                        if [lst[0][0],lst[1][1]] not in stack:
                            stack.append([lst[0][0],lst[1][1]])
                        lst[0]=[lst[0][0],lst[1][1]]
                        lst.pop(1)
                    else:
                        if [lst[0][0],lst[0][1]] not in stack:
                            stack.append([lst[0][0],lst[0][1]])
                        lst.pop(1)
                else:
                    if lst[0] not in stack:
                        stack.append(lst.pop(0))
                    lst.pop(0)
            else:
                if lst[0] not in stack:
                    stack.append(lst.pop(0))
                lst.pop(0)
            print (stack,lst)
        return stack
                
        '''  
        

if __name__=='__main__':

    B =Solution()
    n = int(input())
    sup = []
    for i in range(n):
        #c = list(map(int,input().split(' ')))
        sup.append(list(map(int,input().split(' '))))
    print (B.merge(sup))

'''


Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''
