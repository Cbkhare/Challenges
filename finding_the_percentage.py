#Making a dictionary of key and list from input
#Finding average, find more details in comments
#Rounding float, into to 2 decimal places
#Sorting dictionary

from operator import itemgetter as ig
n = int(input())
d = {}  #dictionary
l = []  #list
for i in range(n):
    l = input().split()
    new_l =[]       #new list
    for j in range(1,len(l)):
        new_l.append(l[j])
    d[l[0]] = list(map(float,new_l))  # making dictionary and converting 
#print (d)                           # string list to int list    
for key, values in d.items():
    avg = round(sum(values)/len(values),2) # to round up to 2 digits
    #print (avg)
    d[key] = avg
sort_d = dict(sorted(d.items(), key=ig(1))) #sorting dictionary
print ("%.2f" %sort_d[input()])
#print (sort_d, d)



'''
by lambda
l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
print reduce(lambda x, y: x + y, l) / len(l

by numpy
import numpy as np
print np.mean(l)

by statistics
l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
mean(l)
'''
'''
Problem Statement

There is a record of 'n' students, each record having name of student, percent marks obtained in Maths, Physics and Chemistry. Marks can be floating values. The user enters an integer 'n' followed by names and marks for the 'n' students. You are required to save the record in a dictionary data type. The user then enters name of a student and you are required to print the average percentage marks obtained by that student, correct to two decimal places.

Input Format

Integer N followed by name and marks for N students.

Output Format

Average percentage of marks obtained

Constraints
2 <= N <= 10
0 <= Marks <= 100

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00
'''
