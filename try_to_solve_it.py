from sys import argv

file_name = argv[1]
file = open(file_name,'r+')

g= {'g': 'n', 'h': 'o','j': 'q', 'd': 'x',
    'm': 't', 'b': 'v', 'c': 'w', 'a': 'u',
    'i': 'p', 'e': 'y', 'f': 'z', 'k': 'r', 'l': 's',
    's': 'l', 'q': 'j', 'p': 'i', 'w': 'c',
    'y': 'e', 'x': 'd', 'n': 'g', 't': 'm',
    'o': 'h', 'v': 'b', 'z': 'f', 'u': 'a', 'r': 'k'}

for line in file:
    line = [g[x] for x in line.strip('\n')]
    print (''.join(line))
    

'''
Challenge Description:

The history of cryptography has about four thousand years. It dates back to the days of the Ancient Rome and continues up till our times. Over the years, a countless number of methods and encryption algorithms have emerged. However, as hackers say, there is nothing impossible to hack or decipher. Try your hand at decoding the code below and see how quickly you will get it right!
So, you have to determine the encryption algorithm of the message below and print the decoded word. If you find the task too difficult, get a hint at the bottom of the page.
Input sample:

The first argument is a path to a file. Each row includes a test case with an encoded word.
mke
mh
lhsby
pm


Output sample:
try
to
solve
it

You have to print the decoded word.
Constraints:

    The word can include from 2 to 40 symbols.
    All letters are lowercase.
    If you need a hint, select the text at the bottom of the page.
    The number of test cases is 40.
'''
