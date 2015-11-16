class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def possible(self,a,bb,curr):     #a is book array, bb is no. of people, curr is value
        stud = 1
        sam = 0
        for page in a:
            if page > curr: return False
            if sam+page > curr:
                stud +=1
                sam  = page
                if (stud > bb): return False
            else:
                sam += page
        return True
            
            
    
    def books(self, A, B):
        n = len(A)
        if (n < B): return -1
        sam = sum(A)
        s, e = 0,sam
        while s<=e:
            m = s+int((e-s)/2)
            if (self.possible(A,B,m)):
                r = m
                e = m - 1
            else:
                s = m +1 
        return r 
        
        

if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = list(map(int,input().split(' ')))
    for i in range(n):
        pages = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        b = int(input())
        print (B.books(pages,b))

'''BOOKS

N number of books are given.
The ith book has Pi number of pages.
You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated atleast one book.

NOTE: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order.

Input:
List of Books M number of students

Your function should return an integer corresponding to the minimum number.

Example:

P : [12, 34, 67, 90]
M : 2

Output : 113

There are 2 number of students. Books can be distributed in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 

'''
