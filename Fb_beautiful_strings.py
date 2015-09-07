#In case data is passed as a parameter

from sys import argv
import string
from operator import itemgetter

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

#print (contents)


alphas = list(string.ascii_lowercase)      #Else use this list(map(chr, range(97, 123)))  

#print (alphas)


for item in contents:

    zapak = [ ltr.lower() for ltr in list(item) if ltr.lower() in alphas]

    zapak_dict = {}

    for zap in zapak:
        if zap not in zapak_dict:
            zapak_dict[zap]=zapak.count(zap)

    summ = 0
    count = 26
    l = len(zapak_dict)
    for z in range(l):
        k,v = (max(zapak_dict.items(), key=itemgetter(1))[0],max(zapak_dict.items(), key=itemgetter(1))[1])
        summ += count* v
        del zapak_dict[k]
        count -=1

    print (summ)

'''
 Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file has a sentence. E.g.

ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves



Output sample:

Print out the maximum beauty for the string. E.g.
152
754
491
729
646

'''
