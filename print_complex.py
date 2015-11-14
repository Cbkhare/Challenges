size = int(input())
lst = size*2-1                     # length of list, size+(size-1)
sub_lst = 4*size - 3               #len of sub list, 1-5-9-13-17....
stack = []
letrs = tuple([chr(i) for i in range(97,97+size)])  #ord(97)=astack = []
inc = 0
ci = -1 
#prepare stack 
for x in range(size):
    pos = lst - 1 - inc   #last pos of sub_lst and zero based list
    c = ci                #for refrence in letrs list 
    min_stack = ['-']*lst
    for j in range(lst-1,pos-1,-2):
        #print (pos,inc,j,c)
        min_stack[j] = letrs[c]
        c+=1     
    stack.append(min_stack)
    #print (min_stack,stack)
    ci +=-1             # to print c-b-a, reverse increment 
    inc+=2              # to redefine pos
#completing list 
for min_st in range(len(stack)-2,-1,-1):
    stack.append(stack[min_st])

if size==1:
    print('a')
else:
    for st in stack:
        print (''.join(st)+''.join(st[len(st)-2::-1]))

'''        
Problem Statement

You are given an integer, N. Your task is to print an alphabet rangoli of size N.

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a,
and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format

Only one line of input containing N, the size of the rangoli.

Constraints

0<N<27

Output Format

Print the alphabet rangoli in the format explained above.
'''
