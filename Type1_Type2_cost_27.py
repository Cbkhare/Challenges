def cal_score(num):
    score = 0
    if num[4]>num[3] and num[4]>num[2]:
        if num[0]>num[1]:           #ex 5 4 20 30 60 type1 > type2
               diff = num[0]-num[1] #diff will be place on its own location
               num[0] -= diff       #will be multiplied to last
               score = diff*num[2]+num[0]*num[4]+num[1]*num[4] #type1 + type2
        elif num[0] < num[1]:#ex 4 5 20 30 60 type1 < type2
               diff    = num[1]-num[0]
               num[1] -= diff
               score  = diff*num[3]+num[1]*num[4]+num[0]*num[4]
        else:
            score = (num[0]+num[1])*num[4]    
    elif (num[4]==num[3] or num[4]==num[2]) and num[2]>num[3]:
        if num[0]>num[1]:           #ex 5 4 20 30 60 type1 > type2
               diff = num[0]-num[1] #diff will be place on its own location
               num[0] -= diff       #will be multiplied to last
               score = diff*num[2]+num[0]*num[4]+num[1]*num[4] #type1 + type2
        elif num[0] < num[1]:#ex 4 5 20 30 60 type1 < type2
               diff    = num[1]-num[0]
               num[1] -= diff
               score  = diff*num[3]+num[1]*num[4]+num[0]*num[4]
        else:
            score = (num[0]+num[1])*num[4]
    else:
        score = num[0]*num[2]+num[1]*num[3]
    return score
           

n_test  = int(raw_input())
score = []
for i in range(n_test):
    num_list = map(int,raw_input().split())
    score.append(str(cal_score(num_list)))
for items in score:
    print items

'''
input
n
a b c d e

n = no. of test cases
a = no. of type 1
b = no. of type 2
c = cost of type 1
d = cost of type 2
e = cost of places other than then original type

target is to maximize the cost '''

