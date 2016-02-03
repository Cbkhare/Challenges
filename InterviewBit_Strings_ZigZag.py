class Solution:
    def convert(self, A,B):
        inc,dec = True, False
        result = {}
        i,row = 0, 1  #tem will increase upto B
        if B==1:    return A
        while i<len(A):
            #print (A[i])
            if inc:
                if row in result:   result[row] +=[A[i]]
                else:   result[row]=[A[i]]
                if row==B:
                    inc= False
                    dec = True
                    row-=1
                else:   row+=1
                i+=1
                continue
            if dec:
                if row in result:   result[row] +=[A[i]]
                else:   result[row]=[A[i]]
                
                if row==1:
                    inc= True
                    dec = False
                    row+=1
                else:   row-=1
                i+=1
                continue
        str_final = ''
        for k,v in result.items():
            str_final+=''.join(v)       
        return str_final
                
        
if __name__ =='__main__':
    S = Solution()
    a,b = input().split(' ')
    print (S.convert(a,int(b)))

'''


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R

And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"

**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D

and hence the answer would be ACBD.

'''
    
