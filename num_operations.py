#In case data is passed as a parameter

from sys import argv
from itertools import permutations 
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n').split(' ') for line in fp]

#print (contents)

for item in contents:
    possible = ''
     
    for i in range(0,3):
        op_list = []
        if i ==0:
            op_list = ('+','-','*','+')
        elif i==1:
            op_list = ('+','-','*','-')
        else:
            op_list = ('+','-','*','*')

        per_op_list = list(permutations(op_list,4))

        #print (len(per_op_list))
        
        for p_list in per_op_list:
            num_list = [int(ite) for ite in  item]
            pn_list = permutations(num_list,5)

            for pn in pn_list :
                pn = list(pn)
                summ = pn[0]
                pn.pop(0)
                p = [it for it in p_list]
                while p != [] :
                    if p[0]=='+':
                        summ += pn[0] 
                    elif p[0]=='-':
                        summ -= pn[0] 
                    elif p[0]=='*':
                        summ *= pn[0]
                    #print (summ,p,pn,pn[0])
                    pn.pop(0)
                    p.pop(0)
            
                if summ == 42:
                    possible = 'YES'
                    break

            if possible == 'YES': break 
             
        
        if possible == 'YES': break 
    
    if possible == 'YES':
        print ('YES')
    else:
        print ('NO')
    

            
            

    
