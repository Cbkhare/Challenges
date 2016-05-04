from sys import stdin as Si, maxsize as m
#import numpy as np

class Solution:
    pass
    
if __name__=='__main__':

    n = int(Si.readline())
    S = Si.readline().strip('\n')

    count = 0
    while '010' in S:
        i = S.index('010')
        S = S[:i+2]+'1'+S[i+3:]
        count+=1
    print(count)


 
'''
Alice has a binary string, BB, of length nn. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010""010".

In one step, Alice can change a 00 to a 11 (or vice-versa). Count and print the minimum number of steps needed to make Alice see the string as beautiful.

Input Format

The first line contains an integer, nn (the length of binary string BB).
The second line contains a single binary string, BB, of length nn.

Constraints

    1≤n≤1001≤n≤100
    Each character in B∈{0,1}B∈{0,1}.

Output Format

Print the minimum number of steps needed to make the string beautiful.

Sample Input 0

7
0101010

Sample Output 0

2

Sample Input 1

5
01100

Sample Output 1

0

Sample Input 2

10
0100101010

Sample Output 2

3

Explanation

Sample Case 0:

In this sample, B="0101010"B="0101010"

The figure below shows a way to get rid of each instance of "010""010":

[binary.png]

Because we were able to make the string beautiful by changing 22 characters (B2B2 and B5B5), we print 22.

Sample Case 1:

In this sample B="01100"B="01100"

The substring "010""010" does not occur in BB, so the string is already beautiful and we print 00.
'''
