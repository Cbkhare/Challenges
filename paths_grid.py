from itertools import permutations
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        l = [A,B]
        l.sort()
        m,n = l        
        ret = 1
        # What is C(m+n-2, n-1)
        # m/1 * (m+1)/2 * ... * (m+n-2)/(n-1)
        for i in range(1,n):
            ret *= (m+i-1)/i
        return int(ret)

if __name__=='__main__':

    B =Solution()
    n = int(input())
    for i in range(n):
        a = int(input())
        b = int(input())
        print (B.uniquePaths(a,b))
        
'''
#Incomplete ZigZag
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A,N):
        A = list(A)
        n = len(A)
        i = 1
        stack = []
        delt = 0   #no. of words del
        while len(A) > 0 :
            zig = (N-i)*2 
            zag = 2*(i-1)

            stack.append(A.pop(0))
            counter = zig #since it is a zero based list
            c=2
            print ('1',stack,A,counter,delt,len(A),n)
            while 0< counter < len(A):
                counter -=1 
                print ('2',stack,A,counter,delt,len(A),n)
                stack.append(A.pop(counter))  #zig
                if zag !=0:
                    if N < counter <len(A)-N:
                        stack.append(A.pop(counter))  #Zag will always be the net num
                    elif counter <=N:
                        stack.append(A.pop(counter-1))
                    delt +=2                      #not on last segment
                else:
                    if N <= counter <len(A)-N:  delt +=1  #not on last segment 
                counter += zig - delt
                c +=1
                print ('3',stack,A,counter,delt,len(A),n)
            i+=1
        return stack
                
'''                
                



