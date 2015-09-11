n1= int(input())
set1 = set(input().split())
n2=int(input())
set2 = set(input().split())
f_set = sorted(list(set1.symmetric_difference(set2)), key=int)
for item in f_set:
    print (item)
