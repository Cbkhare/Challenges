from operator import itemgetter

def bazinga(fun):
    def wrap_fun(d_list,k):
        new_d_list = fun(d_list,k)
        for i in new_d_list:
            if i[3] == 'M':
                print('Mr.'+' '+str(i[0])+' '+str(i[1]))
            else:
                print('Ms.'+' '+str(i[0])+' '+str(i[1]))
    return wrap_fun
        
@bazinga
def sort_list(d_list,k=0):   #k give the key
    d_list.sort(key=itemgetter(k))
    return d_list


if __name__== "__main__":
    num = int(input())
    direct= [] 
    for i in range(num):
        direct.append(input().split())
    k = 2    #column no. of Age
    sort_list(direct,k)
    #print (dl)

'''
Problem Statement

Lets use decorators for building a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. You have to print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people having the same age, the printing should be done in the order of their input. For Henry Davids, the output should be

Mr. Henry Davids

For Mary George, the output should be

Ms. Mary George

Input Format

The first lines contain integer N followed by N lines. Each line contains firstname, lastname, age and sex separated by a single space character.

Constraints
1≤N≤10

Output Format

N names printed in N different lines.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle

Concept

For sorting a nested list based on some parameter you can use itemgetter library. '''
