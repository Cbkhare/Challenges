#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(' ') for line in fp]

#print (contents)

for item in contents:
    stack = []
    #print (item)
    for stuff in item:

        if item.count(stuff)==1:
            stack.append(int(stuff))
    #print (stack)
    if len(stack) > 0:
        print (item.index(str(min(stack)))+1)   #+1 for zero based list
    else:
        print ('0')
        

'''
 There is a game where each player picks a number from 1 to 9, writes it on a paper and gives to a guide. A player wins if his number is the lowest unique. We may have 10-20 players in our game.
Input sample:

Your program should accept as its first argument a path to a filename.

You're a guide and you're given a set of numbers from players for the round of game. E.g. 2 rounds of the game look this way:

3 3 9 1 6 5 8 1 5 3
9 2 9 9 1 8 8 8 2 1 1

Output sample:

Print a winner's position or 0 in case there is no winner. In the first line of input sample the lowest unique number is 6. So player 5 wins.

5
0
'''
