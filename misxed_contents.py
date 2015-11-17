from sys import argv

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(',') for line in fp]

for item in contents:
    words = []
    nums = []
    for it in item:
        if ord(it[0])>=97:
            words.append(it)
        else:
            nums.append(it)
    if len(words)>0 and len(nums)>0:    print (','.join(words)+'|'+','.join(nums))
    elif len(words)==0 and len(nums)>0:  print (','.join(nums))
    elif len(words)>0 and len(nums)==0:  print (','.join(words))
    

'''
Mixed Content

Challenge Description:

You have a string of words and digits divided by comma. Write a program which separates words with digits. You shouldn't change the order elements.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
24,13,14,43,41

Output sample:

melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
24,13,14,43,41

As you cas see you need to output the same input string if it has words only or digits only.
'''
