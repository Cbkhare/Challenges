#In case data is passed as a parameter

from sys import argv
import re
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(';') for line in fp]

#print (contents)

for item in contents:
    part1 = item[0].split(' ')
    part2 = item[1].split(' ')
    lp2 = len(part2)

    #print (part1,part2)
        
    while '' in part1: part1.remove('')
    found = True
    stack,x = [],0
    last_word = 0
    while len(part2) !=0 and found:
        found = False
        w = part2[0]

        #print (part2[0],part1[x:len(part1)-len(part2)+1])
        for strng in part1[x:len(part1)-len(part2)+1]:  #use len(part2) since it is dynamic

            if w in strng:
                
                #print (x,stack)
                word = re.sub(w,'1',strng)
                #print (w,word)
                word = re.sub('[A-Za-z]','_',word)
                word = word.replace('1',w)
                old = x
                x = part1.index(strng)+1
                #print(old,x,stack,part1[old:x])
                stack += part1[old:x-1]
                stack.append(word)
                last_word = strng
                found = True                
                break

            else:
                word = re.sub('[A-Za-z]','_',strng)
                part1[part1.index(strng)] = word
                #print (part1)
                
        part2.pop(0)

    if len(stack)>=lp2 and last_word != part1[-1]:
    #i.e all words are found and some words are remaning uncheked
        #print (part1[part1.index(last_word)+1:])
        for words_left in part1[part1.index(last_word)+1:]:
            jam = re.sub('[A-Za-z]','_',words_left)
            stack.append(jam)
    if stack == []:
        print ('I cannot fix history')
    else:
        print (str(stack).replace('[','').replace(']','').replace(', ',' ').replace('\'',''))     #,last_word)
            

