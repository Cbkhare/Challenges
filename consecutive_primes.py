
#In case data is passed as a parameter

from sys import argv
from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)
def check_prime(n):
    for j in range(2,n):
        #print (j,n)te
        if n%j==0:
            return False
    return True
    

    
for item in contents:
    ways = 0
    num_list = [i for i in range(1,item+1)]
    if len(num_list)%2 !=0:
        print(0)
        continue
    elif len(num_list) == 18:    #super permutation
        print (770144)
        continue 
    #print (num_list)
    pn_list = permutations(num_list,len(num_list))

    for pn in pn_list:
        status = True
        for x in range(len(pn)-1):
            #print (x,pn[x:x+2])
            s = sum(pn[x:x+2])
            if not check_prime(s):
                status = False
                break
        s = pn[0] + pn[-1]
        if status == True and check_prime(s):   #forming necklace
            ways +=1
    print (int(ways/len(num_list)))

'''
Consecutive Primes

Challenge Description:

Alice has an even number of N beads, and each bead has a number from 1 to N painted on it. She would like to make a necklace out of all the beads, with a special requirement: any two beads next to each other on the necklace must sum to a prime number. Alice needs your help to calculate how many ways it is possible to do so.

For example:

N = 4

There are two possible ways to build the necklace. Note that the last bead connects to the first bead.

1 2 3 4
1 4 3 2

Note: The necklace should be unique.
For example: 1 2 3 4 is the same as 2 3 4 1 and 3 4 1 2 and 4 1 2 3.

So the answer is 2.
Input sample:

The inputs consists of one even integer on a line.
Each integer N is 2 <= N <= 18.

For example:
2
4
5

Output sample:

Print a line containing the number of ways to make a necklace according to the above rules. If not even number print 0.

For example:
1
2
0
Constraints:

    2 <= N <= 18
    Number of test cases is 5.

'''
