import sys

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = fp.read().split()




def sieve(n):
    not_prime = []
    prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return prime

if __name__ == '__main__':
    for i in range(len(contents)):
        z = sieve(int(contents[i]))
        print (str(z).replace('[','').replace(']','').replace(', ',','))


'''
Sieve of Eratosthenes is a prime number generator algorithm, probably the most
popular one now a days. The basic concept of the algorithm is-

We’ll input the number up to which we want to generate all the primes.
We’ll take an empty list named not_prime and start a loop from 2(because
there is no prime number before 2) and will first check if 2 is in not_prime
or not. If not, then we’ll print 2 & append all the multiples of 2 in to the
not_prime list. Then we’ll check for 3 in the same way. As 4 is a multiple
of 2, so this value will not be checked again and we’ll do the same for 5
and so on.

The simple code of the above description is as follows. Let’s have a look-
1
2
3
4
5
6
7
8
	
def sieve(n):
    not_prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            print i
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
sieve(100)

This code will print all the prime numbers between 1 to 100.

If you want to put all the primes in another list and want to print/use it later then just make two little changes in the previous code.
1
2
3
4
5
6
7
8
9
10
	
def sieve(n):
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime
sieve(100)'''
