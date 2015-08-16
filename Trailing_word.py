from sys import argv
from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp  if len(line)>1] #to avoid blank lines

#print (contents)

for track in contents:
    if '' in track:
        continue
    word = str(track[1])+'$'
    #print (word,track)
    if (bool(search(word,track[0]))):# and word !='\\b$':
        print (1)
    else:
        print (0)
    



'''
    string = track[0].split(' ')
    word   = track[1].split(' ')
    if '' in (string or word):
        print (0)
        #print (word,string, 'skipped')
        continue
    print (word,string)
    if len(string) >1:
        if track[1] == string[1]:
            print (1)
        else:
            print(0)
    else:
        print(0)
''' 
'''
for item in contents:
    string = item[0].split(' ')
    word = item[1]
    if len(string) !=2 or len(word)<1:# or word =='':
        #print ('jump',len(string),len(word),word)
        continue
    if word == string[1]:
        print (1)
    else:
        print(0)
    #print (string,word)
'''
'''
 There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.
Input sample:

The first argument is a path to the input filename containing two comma-delimited strings, one per line. Ignore all empty lines in the input file.

For example:

Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose


Output sample:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:
1
1
0

'''
