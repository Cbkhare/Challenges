import sys

file_name = sys.argv[1]
fp = open(file_name,'r+')
contents = [line.strip('\n') for line in fp]

#print (contents)

def check_self_desc(num):
    l,i = len(num),0          #remember num is in string format
    if num.count('0') >=1:
        checkd = ['0']            #list holding digits that are already checked
    else:
        checkd = []
    while i <= l-1:
        #if num[i]!='0':                  #digit at the ith position is != 0
            if i == num.count(num[i]):   #i'th pos == no. of time that no is repeating in the num
                checkd.append(num[i])
            i+=1
    r = set(num)#.difference('0')  #refiened num without zero
    if r==set(checkd):
        return True
    else:
        return False

for item in contents:
    print (int(check_self_desc(item)))
    
'''
 A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.
Input sample:

The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. E.g.

2020
22
1210

Output sample:

If the number is a self-describing number, print out 1. If not, print out 0. E.g.

1
0
1

For the curious, here's how 2020 is a self-describing number: Position '0' has value 2 and there is two 0 in the number. Position '1' has value 0 because there are not 1's in the number. Position '2' has value 2 and there is two 2. And the position '3' has value 0 and there are zero 3's.
'''
