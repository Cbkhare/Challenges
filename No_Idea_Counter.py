from collections import Counter

def my_happiness(Array,Dict_A,Dict_B,Num):
    Like = 0
    for j in range(0,int(Num[1])):       #Revolving Dict_A
        for i in range(0,int(Num[0])):   #Revolving Array Step 1
            print (Dict_A[j],Array[i])
            if Dict_A[j]==Array[i]:
                Like = Like + 1
        #print (Like)
    for j in range(0,int(Num[1])):       #Revolving Dict_B
        for i in range(0,int(Num[0])):   #Revolving Array Step 2
            print (Dict_A[j],Array[i])  
            if Dict_B[j]==Array[i]:
                Like = Like - 1
        #print (Like)
    return Like
   

def my_happiness(Count,Dict_A,Dict_B):
    Lcount = 0
    A = list(Dict_A.intersection(set(Count)))
    B = list(Dict_B.intersection(set(Count)))
    for i in A:
        Lcount += Count[i]
    for i in B:
        Lcount -= Count[i]
    print (Lcount)
    

""" Declerations
Num = input().split(' ')    #List contains the No. of array and dict A/B int
Array = defaultdict(list)
Dict_A = defaultdict(list)
Dict_B = defaultdict(list)"""

#Inputs
Num    = input().split(' ')
Array  = map(int,input().split(' '))
Dict_A = set(map(int,input().split(' ')))
Dict_B = set(map(int,input().split(' ')))
Count = Counter(Array)
my_happiness(Count,Dict_A,Dict_B)
"""call function
result = my_happiness(Array,Dict_A,Dict_B,Num)
print (result) 
"""
