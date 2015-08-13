import sys

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n').split(',') for line in fp]



#print (contents)

def check(n):
     count = 0
     for i in range(2,n):
          if n%i == 0:
               count +=1
               break
     if count ==0:
          return True

if __name__ == '__main__':
    for x in contents:
        z= [i for i in range(int(x[0]),int(x[1])+1) if check(i)==True]
        #print (len(z), z)
        print (len(z))

'''
 Given two integers N and M, count the number of prime numbers between N and M (both inclusive)
Input sample:
2,10
20,30


Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.
Output sample:
4
2

Print out the number of primes between N and M (both inclusive)
'''
