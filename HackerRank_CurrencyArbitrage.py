from sys import stdin as Si, maxsize as m
from math import log

def arbitrage(N):
    #print(N)
    A = 100000
    for i in N:
        A=round(A/i,4)
    if A>100000: return int(A-100000)
    else:   return 0
        

if __name__=='__main__':
    n = int(Si.readline())
    for i in range(n):
        print(arbitrage(list(map(float,Si.readline().split()))))


'''

Currency Arbitrage
An arbitrage is the simultaneous purchase and sale of an asset in order to profit from a difference in the price. This type of trade exploits price differences between similar or identical financial instruments, either on different markets or in different forms.

You are a currency trader looking for arbitrage opportunities in the currency market using these three quotes:

    The cost of USD per EUR (USD/EUR) for converting .
    The cost of EUR per GBP (EUR/GBP) for converting .
    The cost of GBP per USD (GBP/USD) for converting .

You must use your USD to buy EUR, then use your EUR to buy GBP, and finally use your GBP to buy USD, resulting in some sort of profit or loss (i.e., ). Reverse trading is not allowed, so you are limited to the exchanges in the direction shown above. For example, you can convert , which means selling US Dollars and buying Euros; you cannot invert the fraction to sell Euros and buy US Dollars.

Given USD for each trade, calculate the arbitrage profit truncated to whole dollars (USD); otherwise, print if there is no arbitrage opportunity.

Input Format

The first line contains a single integer, , denoting the number of quotes.
Each of the subsequent lines describes a quote in the form of three space-separated integers:

    The first quote is a real number denoting the price quote for (USD/EUR).
    The second quote is a real number denoting the price quote for (EUR/GBP).
    The third quote is a real number denoting the price quote for (GBP/USD).

Constraints


Output Format

For each trade, print a single line denoting the arbitrage profit for that trade; if no arbitrage opportunity exists, print . You should have a total of lines of output.

Sample Input

2
1.1837 1.3829 0.6102
1.1234 1.2134 1.2311

Sample Output

114
0

Explanation

There are test cases:

    You use your USD to buy EUR. You then use your EUR to buy GBP. Finally, you use your GBP to buy USD. Because we started out with USD, our net profit in whole dollars is USD.
    There is no arbitrage opportunity here (the conversion would end up losing money), so we print .


'''
    

        
