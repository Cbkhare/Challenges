"""Problem Statement

There is an array of n integers, and 2 disjoint sets of m integers each A and B. You like all integers in A and dislike all integers in B. Your initial happiness is 0 and for each integer in the array, i, if i∈A, you add 1 to your happiness, if i∈B, you add −1 to your happiness, else your happiness does not change. Output your final happiness at the end.

Note that since A and B are sets, they have no repeated elements. But, the array might contain duplicate elements.

Constraints
1≤n≤105
1≤m≤105
1≤Any integer in the input≤109

Input Format

First line contains n and m.
Second line contains n integers, the array.
Third and fourth lines contain m integers, A and B respectively.

Output Format

Output a single integer, the answer.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1"""

from collections import defaultdict

def my_happiness(Array,Dict_A,Dict_B,Num):
    Like = 0
    for j in range(0,int(Num[1])):       #Revolving Dict_A
        for i in range(0,int(Num[0])):   #Revolving Array
            #print (Dict_A[j],Array[i])
            if Dict_A[j]==Array[i]:
                Like += 1
    for j in range(0,int(Num[1])):       #Revolving Dict_B
        for i in range(0,int(Num[0])):   #Revolving Array
            #print (Dict_A[j],Array[i])
            if Dict_B[j]==Array[i]:
                Like -= 1
    return Like
    


# Declerations
Num = input().split(' ')    #List contains the No. of array and dict A/B int
Array = defaultdict(list)
Dict_A = defaultdict(list)
Dict_B = defaultdict(list)

#Inputs
Array  = input().split(' ')
Dict_A = input().split(' ')
Dict_B = input().split(' ')

#call function
result = my_happiness(Array,Dict_A,Dict_B,Num)
print (result)
    
    
