from sys import maxsize as m
if __name__=='__main__':
    n,p = map(int,input().split(' '))
    buyer = []
    for i in range(n):
        buyer += [input()]
        
    a = 1   #last will always be halfplus
    for i in range(n-2,-1,-1):
        if buyer[i]=='half':
            a = 2*a
        elif buyer[i]=='halfplus':
            a = 2*a+1

    cost = 0
    for i in range(n):
        if a%2==0:
            if buyer[i]=='half':
                cost += p*(a/2)
                a/=2
            elif buyer[i]=='halfplus':
                cost += p*(a/2 - 1/2)
                a = int(a/2 - 1/2)
        else:
            cost += p*(a/2)
            a = int(a/2 - 1/2)
    print (int(cost))
            
    
'''

A. Grandma Laura and Apples
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Grandma Laura came to the market to sell some apples. During the day she sold all the apples she had. But grandma is old, so she forgot how many apples she had brought to the market.

She precisely remembers she had n buyers and each of them bought exactly half of the apples she had at the moment of the purchase and also she gave a half of an apple to some of them as a gift (if the number of apples at the moment of purchase was odd), until she sold all the apples she had.

So each buyer took some integral positive number of apples, but maybe he didn't pay for a half of an apple (if the number of apples at the moment of the purchase was odd).

For each buyer grandma remembers if she gave a half of an apple as a gift or not. The cost of an apple is p (the number p is even).

Print the total money grandma should have at the end of the day to check if some buyers cheated her.
Input

The first line contains two integers n and p (1 ≤ n ≤ 40, 2 ≤ p ≤ 1000) — the number of the buyers and the cost of one apple. It is guaranteed that the number p is even.

The next n lines contains the description of buyers. Each buyer is described with the string half if he simply bought half of the apples and with the string halfplus if grandma also gave him a half of an apple as a gift.

It is guaranteed that grandma has at least one apple at the start of the day and she has no apples at the end of the day.
Output

Print the only integer a — the total money grandma should have at the end of the day.

Note that the answer can be too large, so you should use 64-bit integer type to store it. In C++ you can use the long long integer type and in Java you can use long integer type.
Examples
Input

2 10
half
halfplus

Output

15

Input

3 10
halfplus
halfplus
halfplus

Output

55

Note

In the first sample at the start of the day the grandma had two apples. First she sold one apple and then she sold a half of the second apple and gave a half of the second apple as a present to the second buyer.


'''
        
