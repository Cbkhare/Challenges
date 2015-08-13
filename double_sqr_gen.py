import sys
import math

file_name = sys.argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

#print (contents)

###############Code begins here################

#contents = [10,36,38,25]
def get_odd_factor(num):
        prime_fac = []
        others = []
        for i in range(4,num+1):   #excluding 2,3 by default to incude 36 etc
                if i not in prime_fac:  
                        if num%i ==0:
                                prime_fac.append(i)
                                for j in range(i*i,num+1,i):
                                        others.append(j)
                        else:
                                continue
        return prime_fac    
                
                        
def count_way(num):
        r_num = math.sqrt(num)
        dec_num, int_num = math.modf(r_num)   #modf(3.45)= 0.45000 , 3.0
        ways = 0
        for i in range(0,int(int_num)+1):
                for j in range(0,int(int_num)+1):
                        if i**2+j**2==num:
                                ways +=1
                                if i==j==0:   #special inclusion for num=zero 
                                        ways=2
        return int(ways/2)


if __name__=='__main__':
        for item in contents[1:]:
                factors = get_odd_factor(int(item))
                check =0
                for values in factors:
                        if (values-3)%4==0:
                                check+=1
                if check==0:
                        num_way = count_way(int(item))
                        print (num_way)
                elif check==0 and int(item)%2==0:
                        num_way = count_way(int(item))
                        print (num_way)
                else:
                        num_way=0
                        print (num_way)#print (str(item)+':'+'No way')


'''
Double Squares
Sponsoring Company:

  
Challenge Description:
Credits: This challenge appeared in the Facebook Hacker Cup 2011.

A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares.

For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2.
NOTE: Do NOT attempt a brute force approach. It will not work. The following constraints hold:
0 <= X <= 2147483647
1 <= N <= 100
Input sample:

Your program should accept as its first argument a path to a filename. You should first read an integer N, the number of test cases. The next N lines will contain N values of X.

5
10
25
3
0
1

Output:
1
2
0
1
1
'''
