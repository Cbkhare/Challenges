#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [list(map(int,line.strip('\n').split(' '))) for line in fp]

#print (contents)

for item in contents:
    
    wire_len = item[0]
    min_dis  = item[1]

    hang_point = 6
    count = 1

    if item[2] == 0 :             #i.e no bats are hanging
                
        while hang_point < wire_len-6:
            
            hang_point = hang_point + min_dis
            if hang_point > wire_len-6: break
            count +=1             #bats added
    else:
        s_bats = sorted(item[3:])
        #print (s_bats)
        no_change = 0
        for bats in item[3:]:
            if bats - hang_point >= min_dis and hang_point not in item[3:]:
                while bats - hang_point > min_dis:
                    hang_point = hang_point + min_dis
                    if hang_point > bats: break
                    count += 1
                    no_change = 1 #there is atleast some addition 
            else:
                hang_point = bats + min_dis
            
        if hang_point >= s_bats[-1]:

            while hang_point < wire_len - min_dis:
                hang_point += min_dis
                if hang_point > wire_len - 6 : break
                count +=1
                no_change = 1    #there is atleast some change
        if no_change == 0: count =0
    print (item,count)


'''
Bats Challenge

Challenge Description:

There is a wire between two buildings outside of your window. Bats love to hang there, but they never hang closer than "d" centimeters from each other. They also don't hang closer than 6 centimeters from any of the buildings.

Your task is to determine the maximum number of additional bats that can fit on the wire assuming they have a zero width.
Input sample:

Your program should accept a file as its first argument. Each line of input contains three space separated integers: the length of the wire "l", distance "d", and number of bats "n" that are already hanging on the wire.


22 2 2 9 11
33 5 0
16 3 2 6 10
835 125 1 113
47 5 0


The "n" number of bats is located in any order. All numbers are integers. You can assume that the bats that are already hanging on the wire are at least 6 cm from the buildings and at least "d" centimeters apart from each other.

For example:
Output sample:

For each line of input, print out one integer to determine the maximum number of additional bats that can possibly hang on the wire.

3
5
0
5
8

'''
 
