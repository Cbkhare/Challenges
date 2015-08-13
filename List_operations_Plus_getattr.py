'''
Task
You have to initialize your list L = [] and follow the N commands given in N lines.

Commands will be 1 of the 8 commands as given above, other than extend, and each command will have its value separated by space.

Follow this example:

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
++++++++++++++++++++++++++++++++++++++++++++++++++


L= []
n_cmd = int(input())
for i in range(n_cmd):
     task = input().split()
     if task[0] == "insert":
          L.insert(int(task[1]),int(task[2])) #L[int(task[1])]=L[int(task[2])]  # 
     elif task[0] == "print":
          print (L)
     elif task[0] == 'remove':
          L.remove(int(task[1]))
     elif task[0] == 'append':
          L.append(int(task[1]))
     elif task[0] == 'sort':
          L.sort()
     elif task[0] == 'pop':
          L.pop()
     elif task[0] == 'reverse':
          L.reverse()'''


L = []
for i in range(int(input())):
    command, *args = input().split()
    try:
        getattr(L, command)(*(int(x) for x in args))
    except AttributeError:
        print(L)

'''
Instead of try block below code can also be used which would be uch appropraite

if command == 'print':
    print(L)
else:
    getattr(L, command)(*(int(x) for x in args))

'''

















     
