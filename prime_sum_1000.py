summ =2
pnt  = 1
p_num = 3   # start from prime no. 3 
while pnt<=999:   # 2 is already included
    check = 0
    for i in range(2,p_num):
        if p_num%i == 0:
            check += 1
            continue
    if check == 0:
        summ += p_num
        pnt +=1
        #print (p_num)
    p_num +=1 
print (summ)


'''
challenge Description:

Write a program which determines the sum of the first 1000 prime numbers.
Input sample:

There is no input for this program.
Output sample:

Print to stdout the sum of the first 1000 prime numbers.

3682913
'''
    
     
