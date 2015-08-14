from itertools import permutations

cases = int(input())

stack = []

def taste(lst,n):
    tst_lst = []
    tup = list(permutations(lst,n))
    for tups in tup: 
        tst =0
        for j in range(1,n):
            tst += (j+1)*abs(tups[j]-tups[j-1])
        print (tups)
        tst_lst.append(tst)
    return (max(tst_lst))



for i in range(cases):
    nf = int(input())                         #No. of Fruits
    sw  = list(map(int,input().split(' ')))   #Fruits sweetness
    stack.append(taste(sw,nf))


for tastes in stack:
    print (tastes)


'''
Samu had got N fruits. Sweetness of ith fruit is given by A[i]. Now she wants to eat all the fruits , in such a way that total taste is maximised.

Total Taste is calculated as follow (Assume fruits sweetness array uses 1-based indexing) :

int taste=0;
for(int i=2;i<=N;i++){
    if (A[i]-A[i-1] >= 0){
       taste = taste + i*(A[i]-A[i-1]);
    }
    else{
       taste = taste + i*(A[i-1]-A[i]);   
    }
}

So, obviously the order in which she eat the fruits changes the Total taste. She can eat the fruits in any order. Also once she start eating a fruit she will finish that one before moving to some other fruit.

Now she got confused in deciding the order in which she should eat them so that her Total taste is maximized. So she ask for help from you. Help her find the maximum taste she can have , if she can eat the fruits in any order.

Input Format :
First line contain number of test cases T. First line of each test case contains N, denoting the number of fruits. Next line contain N space separated integers denoting the sweetness of each fruit.

Output Format :
For each test case you need to print the maximum taste Samu can have by eating the fruits in any order she want to.

Constraints :
1 ≤ T ≤ 10
1 ≤ N ≤ 15
Sweetness of each fruit, A[i] lies between 1 to 100 for 1 ≤ i ≤ N
Sample Input
(Plaintext Link)

1
3
2 5 4

Sample Output
(Plaintext Link)

13

Explanation

[2,4,5] -> 2*(2) + 3*(1) = 7
[2,5,4] -> 2*(3) + 3*(1) = 9
[5,4,2] -> 2*(1) + 3*(2) = 8
[5,2,4] -> 2*(3) + 3*(2) = 12
[4,5,2] -> 2*(1) + 3*(3) = 11
[4,2,5] -> 2*(2) + 3*(3) = 13

So maximum is 13 that can be obtained by eating the fruits according to sweetness order [4,2,5].
'''
