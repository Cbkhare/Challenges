#n = input()
lis = input().split()
z =sorted(list(set(lis)),key=int) #.intersection(lis))
#lis.sort()
#print (z,lis)  #sorted makes a new list so time complexity increases
#zz=sorted(z,key=int)
print (z)
if all(int(i) <= 0 for i in z) == True:
    print (z[len(z)-2])
else:
    z.reverse()
    print (z[1])
    

