#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n').split(';') for line in fp]

#print (contents)


for item in contents:

    if item == ['']: continue

    str1,str2 = list(item[0]),list(item[1])
    while ' ' in str1:
        str1.remove(' ')
    while ' ' in str2:
        str2.remove(' ')
    print (str1,str2)
    

    stack = []
    length = 0
    jack = []
    for ltr in str1:

        seq = []

        if ltr in str2:
            seq.append(ltr)
            ctr1 = str1.index(ltr) + 1  #i.e Next ltr
            ctr2 = str2.index(ltr)


            while ctr2 < len(str2) and ctr1<len(str1):    #i.e ctr2 reaches the end of srt2
                
                print (ctr1,ctr2)
                if str1[ctr1] in str2[ctr2:]:
                    print('added',str1[ctr1],str2[ctr2:])
                    seq.append(str1[ctr1])
                    ctr2 += str2.index(str1[ctr1])       #to maintain the index
                
                ctr1 +=1
                
        if len(seq)>=2: jack.append(seq)               #to find all subseq
        if len(seq) >=2 and len(seq)>length:
            stack= seq
            length = len(seq)
    stack = ''.join(stack)
    #print (stack)
    print (item,jack)

