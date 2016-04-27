from sys import stdin as Si, maxsize as m
#import numpy as np


def makeIt(T,k):
    print(T)
    if k<=0:
        if T==T[::-1]:  return T
        else:   return ['-1']

    if len(T)==0:   return ['']
    if len(T)==1:   return T
    
    s,e,Ans = 0,len(T)-1,''
    if T[s]==T[e]:
        t = T[s]
        ans = makeIt(T[s+1:e],k)
        if ans !=['-1']:
            if ans == ['']:
                Ans = ['9']*2
            else:
                Ans = [t]+makeIt(T[s+1:e],k)+[t]
        else:   Ans=['-1']
    if k>=2:
        Ans1 = makeIt(T[s+1:e],k-1)
        Ans2 = makeIt(T[s+1:e],k-2)
        if Ans1!=['-1']:
            if Ans1 == ['']:
                Ans = ['9']*2
            else:
                t = max(T[s],T[e])
                Ans1 = [t]+Ans1+[t]
        if Ans2!=['-1']:
            if Ans2 == ['']:
                Ans = ['9']*2
            else:
                Ans2 = ['9']+Ans2+['9']
        Ans = max(Ans1,Ans2)
    elif 0<k<2:
        if T[s]>T[e]:   T[e]=T[s]
        else:   T[s]=T[e]
        Ans = T
    if Ans!=['-1'] and Ans==Ans[::-1]:  return Ans
    else:   return ['-1'] 
        
        
        

if __name__=='__main__':
    n,k = map(int,Si.readline().split())
    T = list(Si.readline().strip('\n'))
    s,e=0,len(T)-1
    Ans = makeIt(T,k)
    if Ans ==['-1']:    print(-1)
    else:   print(''.join(Ans))

'''


Sandy likes palindromes. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as it does forward. For example, madam is a palindrome.

On her birthday, Sandy's uncle, Richie Rich, offered her an -digit check which she refused because the number was not a palindrome. Richie then challenged Sandy to make the number palindromic by changing no more than digits. Sandy can only change digit at a time, and cannot add digits to (or remove digits from) the number.

Given and an -digit number, help Sandy determine the largest possible number she can make by changing digits.

Note: Treat the integers as numeric strings. Leading zeros are permitted and can't be ignored (So 0011 is not a palindrome, 0110 is a valid palindrome). A digit can be modified more than once.

Input Format

The first line contains two space-separated integers, (the number of digits in the number) and (the maximum number of digits that can be altered), respectively.
The second line contains an -digit string of numbers that Sandy must attempt to make palindromic.

Constraints

    Each character in the number is an integer where .

Output Format

Print a single line with the largest number that can be made by changing no more than digits; if this is not possible, print -1.

Sample Input 0

4 1
3943

Sample Output 0

3993

Sample Input 1

6 3
092282

Sample Output 1

992299

Sample Input 2

4 1
0011

Sample Output 2

-1

Explanation

Sample 0

There are two ways to make a palindrome by changing exactly digits:

, so we print .

'''
