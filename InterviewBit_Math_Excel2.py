chars = {}
for i in range(97,123):                 #A-65,a-97
    chars[i-96] = (chr(i)).upper()
    
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        stack = []
        num =A
        while num != 0.0:
            if num <= 26:
                #print (num)
                stack.append(chars[int(num)])
                num = num - num
            else:
                if num%26 == 0.0:
                    stack.append('Z')
                    num = (num-26)/26
                    #print (num)
                else:
                    divisor  = 0
                    while (num-divisor)%26 != 0.0:
                        divisor +=1
                    num = (num-divisor)/26
                    #print (num)
                    stack.append(chars[divisor])
        stack.reverse()
        return (''.join(stack))


if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        #c  = tuple(map(int,input().split(' ')))
        m = int(input())
        #c = input()
        print (B.convertToTitle(m))
    

'''


Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

'''
