pal_num =  []
for i in range(101,1000):
    count = 0
    for j in range(2,i):
        if i%j ==0:
            break
        else:
            count = j
    if  count == i-1:
        if i//100 == i%10:
            pal_num.append(i)
pal_num.reverse()
print (pal_num[0])
    
'''
 Write a program which determines the largest prime palindrome less than 1000.
Input sample:

There is no input for this program.
Output sample:

Print to stdout the largest prime palindrome less than 1000.

929

'''
