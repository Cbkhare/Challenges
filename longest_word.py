from sys import argv
file_name = argv[1]
fp = open(file_name,'r+')
contents = [line.strip('\n').split(' ') for line in fp]
for item in contents:
    old = ''
    for it in item:
        if len(it)> len(old):
            old = it
    print (old)

'''
Challenge Description:

In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following
some line with text
another line

Each line has one or more words. Each word is separated by space char.
Output sample:

Print the longest word in the following way.
some
another
'''
