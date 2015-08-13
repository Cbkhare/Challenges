from sys import argv

file_name = argv[1]
fp = open(file_name,'r+')
'''
contents = [line.strip('\n') for line in fp]
content = [item.split(' ') for item in contents]
'''
content = fp.read().split()

#print (content)
#content = input().split()
#boolean= []
#jhakas = lambda lst,siz: [lst[i:i+siz] for i in range(0,len(lst),siz)]
'''
for item in content:
        for j in range(len(item)):
                print (item[j])
'''

for item in content:
        #print (item)
        size  = len(item)
        h_size = int(len(item)/2)  #half of the list
        check = 0
        for i in range(0,h_size):
                #print (item[i])
                if item[i]=='[':
                        if item[size-i-1]==']':  #looking at mirror oppostie pos
                                check+=1
                elif item[i]=='{':
                        if item[size-i-1]=='}':  #looking at mirror oppostie pos
                                check+=1
                elif item[i]=='(':
                        if item[size-i-1]==')':  #looking at mirror oppostie pos
                                check+=1
                else:
                        continue    #No need to check further, exp is False
        if check == h_size:
                print ('True')
        else:
                print ('False')
                
              

'''
 Given a string comprising just of the characters (,),{,},[,] determine if it is well-formed or not.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a string comprising of the characters mentioned above. E.g.

()
([)]

Output sample:

Print out True or False if the string is well-formed. E.g.

True
False'''









