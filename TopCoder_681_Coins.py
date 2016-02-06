if __name__=='__main__':
    strng = input()
    intrst = 0
    for i in range(len(strng)):
        if len(strng)==1:
            continue
        if i==0:
            if strng[i]!=strng[i+1]:
                intrst+=1
        elif i==len(strng)-1:
            if strng[i]!=strng[i-1]:
                intrst+=1
        else:
            if strng[i]!=strng[i-1] or strng[i]!=strng[i+1]:
                intrst+=1
    print (intrst)
                
'''Problem Statement

You have n coins, labeled 0 through n-1. Each of the coins shows either heads or tails. You are given the states of all coins in the state with n characters. For each i, state[i] is 'H' if coin i shows heads, or 'T' if it shows tails.

The coins are laid out in a row, ordered from coin 0 to coin n-1. A coin is called interesting if it differs from at least one of its neighbors. (For example, a coin that shows heads is interesting if at least one of its neighbors shows tails.) Return the number of interesting coins.
Definition
Class:
CoinFlipsDiv2
Method:
countCoins
Parameters:
string
Returns:
integer
Method signature:
def countCoins(self, state):
Limits
Time limit (s):
2.000
Memory limit (MB):
256
Notes
- The value of n is not given explicitly. Instead, you can determine it as the number of characters in state.
Constraints
- state will have between 1 and 50 elements, inclusive.
- Each character of state will be either 'H' or 'T'.
Examples
0)
"HT"
Returns: 2
Coin 0 is interesting because it shows heads and its only neighbor shows tails. Similarly, coin 1 is interesting because it shows tails and its only neighbor shows heads. Thus, the answer is 2.
1)
"T"
Returns: 0
In this test case there is a single coin. It has no neighbors, and therefore it has no different neighbors. This means that the coin is not interesting.
2)
"HHH"
Returns: 0
None of these coins are interesting, because each of them is only adjacent to coins that show the same side.
3)
"HHTHHH"
Returns: 3
Here, the three interesting coins are coins 1, 2, and 3. (Remember that the indices are 0-based.)
4)
"HHHTTTHHHTTTHTHTH"
Returns: 12
'''
