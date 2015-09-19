tc = int(input())
a = 'XY'
b = 'YX'
for i in range(tc):

    s = input()

    if 'X' not in s or 'Y' not in s:
        print (len(s)-1)
        continue
    count = 0
    j = 0
    while j < len(s):
        
        if s[j] == s[j+1]:
            s = s[j+1:]
            count +=1
            if len(s) == 1:
                #count +=1
                break
            #print (j)
            #print (s,count)
        else:
            s = s[j+1:]
            #print (s,count)
            #print (j)
            if len(s)==1:
                break
    print (count)

'''
Only one by one


All submissions for this problem are available.

 

Maiya like strings which are in flip flop in nature. For example, he likes XYXY, while he doesn't like XXYX. Now he want to convert every string into a string which he likes. for this, he can only delete the character in the string.

Now find the minimum number of delete operation which is required to covert a string that Maiya likes. 
Input

The first line contains an integer T i.e the number of test cases. Next T lines contain a string each.

 
Output

For each test case, print the minimum delete operation required.

 
Constraints

    1 ≤ T ≤ 10
    1 ≤ Length of the string ≤ 105

 
Example

Input:
5
XXXX
YYYYY
XYXYXYXY
YXYXYX
XXXYYY

Output:
3
4
0
0
4

 
Explanation

XXXX => X, 3 deletions YYYYY => Y, 4 deletions XYXYXYXY => XYXYXYXY, 0 deletions YXYXYXYX => YXYXYXYX, 0 deletions XXXYYY => XY, 4 deletions
'''
