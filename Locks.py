#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(' ') for line in fp]

#print (contents)

for item in contents:

    doors, beats = int(item[0]),2*int(item[1])

    stack = [0]*doors

    for it in range(1,beats-1):
        
        if it%2 != 0:       #for 1st beat

       #closing 2nd door, for a zero #based list i,e 1,3,5 etc
            for j in range(1,len(stack),2):

                if not stack[j]:
                    stack[j] = 1

        else:            #second beat

            for h in range(2,len(stack),3):

                if stack[h]:
                    stack[h] = 0
                else:
                    stack[h] = 1 


    if stack[-1]:
        stack[-1] = 0
    else:
        stack[-1] = 1
    #print (stack)
    print (stack.count(0))

'''
 There are N unlocked rooms located in a row along the corridor.

A security guard, who starts the beat at the beginning of the corridor, passes by and closes the lock of every second door (2nd, 4th, 6th…). Then he returns to the beginning of the corridor, and passes by again changing the state of every third door (3rd, 6th, 9th…) to the opposite state — if the door is closed, security guard opens it; if the door is open, he closes it.

One iteration consists of two beats (when the security guard closes each second door, and changes the state of each third door to the opposite state). The iteration repeats M-1 times.

During the last iteration, the security guard just changes the state of the last door in a row (closes it, if the door is open or opens it, if the door is closed).

Your task is to determine how many doors have been left unlocked.

Input sample:

3 1
100 100

Your program accepts a filename as its first argument.

Each line of input contains 2 integers separated by space. The first integer represents number of doors (N), the second — number of iterations (M).

Output sample:
2
50
For each line of input print out how many doors are left unlocked:
'''
        
