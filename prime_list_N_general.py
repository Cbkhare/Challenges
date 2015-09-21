import sys

file_name = sys.argv[1]
fp = open(file_name,'r+')

#to find contents
contents = fp.read().split()



def prime_gen(n):
    num_list=[2]
    if n <=2:
        return []
    else:
        for i in range(3,n,2):
            check=0
            for u in range(2,i):
                if i%u == 0:
                    check += 1
                    continue
            if check == 0:
                num_list.append(i)
    return num_list

if __name__== '__main__':
    for j in range(len(contents)):
            num_list = prime_gen(int(contents[j]))
            print (str(num_list).replace('[','').replace(']','')) #to print without []
'''
contents = ['10','15']#'20','100','2','5']    #to-check


for i in range(len(contents)):
    target = int(contents[i])
    num_list= [2]
    for j in range(3,target,2):
        check = 0
        for u in range(2,j):
            if j%u == 0:
                check +=1
                continue
        if check == 0:
            num_list.append(j)
    #print (num_list)
    print (str(num_list).replace('[','').replace(']','')) #to print without []

'''

'''
A file will be given as input contaning no. blow as input

input
10
20
100
2

Output

print all the prime no. less than the given no. Output for
below program
[2, 3, 5, 7]
[2, 3, 5, 7, 11, 13, 17, 19]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
[2]
'''
