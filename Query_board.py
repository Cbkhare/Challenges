from sys import argv

file_name = argv[1]
fp = open(file_name,'r+')

#contents = [line.strip('\n').split(' | ') for line in fp]
st = [[0]*256]*256
for line in fp:
    item = line.strip('\n').split(' ')
    #print (item)  
    if item[0]== 'SetRow':
        st[int(item[1])-1]= [int(item[2])]*256
    elif item[0]=='SetCol':
        for i in range(256):
            st[i][int(item[1])-1]=int(item[2])
    elif item[0]=='QueryRow':
        print (sum(st[int(item[1])-1]))
    elif item[0]=='QueryCol':
        s = 0
        for j in range(256):
            s += int(st[j][int(item[1])-1])
        print (s)


'''
Query Board

    Solution submitted successfully. You can now view your score.

View challenge description
Challenge Description:

There is a board (matrix). Every cell of the board contains one integer, which is 0 initially.

The next operations can be applied to the Query Board:
SetRow i x: it means that all values in the cells on row "i" have been changed to value "x" after this operation.
SetCol j x: it means that all values in the cells on column "j" have been changed to value "x" after this operation.
QueryRow i: it means that you should output the sum of values on row "i".
QueryCol j: it means that you should output the sum of values on column "j".

The board's dimensions are 256x256
"i" and "j" are integers from 0 to 255
"x" is an integer from 0 to 31
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains an operation of a query. E.g.

SetCol 32 20
SetRow 15 7
SetRow 16 31
QueryCol 32
SetCol 2 14
QueryRow 10
SetCol 14 0
QueryRow 15
SetRow 10 1
QueryCol 2

Output sample:

For each query, output the answer of the query. E.g.

5118
34
1792
3571

'''
