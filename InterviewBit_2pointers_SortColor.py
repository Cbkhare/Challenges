class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        red,white,blue = 0
        for color in A :
            if color == 0 :
                red+=1
            elif color == 1 :
                white+=1
            else:
                blue+=1
        return red*[0] + white*[1] + blue*[2]     
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.sortColors(c))


'''
SORTCOLOR

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]

'''
