import sys
from itertools import chain

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n').split(', ') for line in fp]

#print (contents)



for item in contents:
     string = [i.split(',') for i in item[0]]
     char = [i.split(',') for i in item[1]]
     #print (string,char)
     for c in char:
          if c in string:
               string.remove(c)
     stack = []
     for stufs in string:
          stack = list(chain(stack,stufs))
     print (''.join(stack))


'''
 Write a program which removes specific characters from a string.
Input sample:


The first argument is a path to a file. The file contains the source strings and the characters that need to be scrubbed. Each source string and characters you need to scrub are delimited by comma.

For example:


how are you, abc
hello world, def



Output sample:

Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.

For example:

how re you
hllo worl
'''
