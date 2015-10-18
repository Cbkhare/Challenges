import sys
import mmap

# Parameter file is Fizz_Buzz.txt stored in same place as where is script

file_name = sys.argv[1]
fp = open(file_name,'r+')

#TO FIND THE CONTENTS
contents = fp.read().split()
#print (contents)


#To read no. of lines in the filevia Buf mmap"
'''
buf = mmap.mmap(fp.fileno(), 0)
num_lines = 0
readline = buf.readline
while readline():
    num_lines += 1
#print (num_lines)

'''

#To Get No. Of line'''
num_lines = int(sum(1 for line in contents)/3)
print (num_lines)

for i in range(num_lines):
    i *=3
    #print(contents[i],contents[i+1],contents[i+2])
    till = int(contents[i+2])+1
    x = int(contents[i])
    y = int(contents[i+1])
    nums = [ x for x in range(1,till)]
    for j in range(1,till):
        if j%x == 0 and j%y != 0:
            nums[j-1]='F'
        elif j%y == 0 and j%y != 0:
            nums[j-1]='B'
        elif j%x == 0 and j%y == 0:
            nums[j-1]='FB'
    print (' '.join(map(str, nums))) #To join list with only spaces (''.join(str(nums)))
#print (contents)
        
    
'''
data = []
for line in contents:
    print (line)
    int_num = line.strip().split()
    intg = [int(x) for x in int_num]
    data.append(intg)
print (data[0])

buf = mmap.mmap(fp.fileno(), 0)
lines = 0
readline = buf.readline
while readline():
    lines += 1
print (lines)


++++++++++++++++++++++++++
num_lines = sum(1 for line in fp)
print (num_lines)'''
