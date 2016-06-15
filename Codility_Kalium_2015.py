from sys import stdin as Si,maxsize as m
from math import ceil as C


def solution(A):
    zi,oi = len(A),0
    for i in range(len(A)):       #use pythonic way instead 
        if A[i]==1: oi=max(oi,i)
        if A[i]==0: zi=min(zi,i)
    zc,oc=0,0                     #actual count of zero one 
    for i in range(zi,oi+1):
        if A[i]==1: oc+=1
        if A[i]==0: zc+=1 
    I,czc,coc = zi,0,0           #Index , current count of zero and one 
    for i in range(zi,oi+1):
        #print(I)
        if A[i]==0: czc+=1
        if A[i]==1: coc+=1 
        if czc > (i-zi+coc)/2 and oc-coc > (oi-i+zc-czc)/2:   I=i+1
        '''
        what above done is
        count of current zero should be greater than range i+1-zi with coc
        which is count of one in that range
        coc is the count of 1 in the range i-zi
        similarly for the range oi-i count of one int hat range should be
        greater range with count of one
        '''
    #print(I)
    zc,oc = czc,oc-coc
    i=zi-1
    while i>=0:
        t=0
        if A[i]==0: t+=1
        if zc+t > (I-i)/2:  zi-=1;zc+=t  #reducing counter, incr. count
        i-=1
    i = oi+1
    while i<len(A):
        t = 0
        if A[i]==1: t+=1
        if oc+t > (i-I)/2:  oi+=1;oc+=t #incr. counter, incr. count
        i+=1

    return len(A[zi:oi+1]),zi,oi,I  #zi,oi,I,
        
    
if __name__=='__main__':
    t = int(Si.readline())
    for i in range(t):
        n = list(map(int,Si.readline().split()))
        print (solution(n))
'''


You want to spend your next vacation in Poland. Despite its not being a very big country, Poland has a highly diverse natural environment ranging from the Baltic Sea in the north to the Tatra Mountains in the south. As you enjoy swimming in the sea as well as trekking up mountains, you would like to spend some time in both of those locations. However, the weather in Poland can sometimes be very capricious, so you also need to take that into account when planning your vacation.

In the summer you are free for N consecutive days. You can start and finish your vacation on any of these days. You want to spend the first part of your vacation at the seaside and the remaining part in the mountains. These parts can each be of any positive length, and you want to maximize the total length of the vacation.

You have obtained a weather forecast for all N days when you are free. By curious coincidence, the weather on every day is expected to be either perfect for spending the day at the seaside but not in the mountains, or vice versa (perfect for trekking but not for swimming). Obviously, you want the best possible weather during each part of your vacation, so you require the weather to be perfect for swimming for more than half of the days in the first part of your vacation, and perfect for trekking for more than half of the days in the second part of your vacation.

The weather forecast is described in a zero-indexed array A: for each K (0 ≤ K < N), A[K] is equal to 0 if the weather during day K favors the seaside, or 1 if the weather during that day favors the mountains.

Write a function:

    def solution(A)

that, given a zero-indexed array A of N integers, returns the length of the longest vacation consistent with your requirements.

For example, consider array A such that:
    A[0] = 1
    A[1] = 1
    A[2] = 0
    A[3] = 1
    A[4] = 0
    A[5] = 0
    A[6] = 1
    A[7] = 1

You are free for eight days. The weather during days 2, 4 and 5 will be better for swimming, and better for trekking during the remaining days. You can start your vacation on day 1, spend five days at the seaside (three days will have perfect weather, which is more than half) and then spend two days in the mountains (both days will have perfect weather). That results in a vacation length of seven days, which is the longest possible vacation that meets your criteria, so the function should return 7.

For array A such that:
    A[0] = 1
    A[1] = 0

there is no vacation that satisfies your requirements, so the function should return 0.

Assume that:

        N is an integer within the range [2..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

'''
