from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt
from operator import itemgetter as ig
from math import pi


if __name__== '__main__':
    n = int(Si.readline())
    #H = tuple(map(int,Si.readline().split()))
    h = {}
    for hh in tuple(map(int,Si.readline().split())):
        h[hh] = h.get(hh,0)+1
        
    m = int(Si.readline())
    lan = {}
    for l in tuple(map(int,Si.readline().split())):
        lan[l] = lan.get(l,0)+1
    sub = {}
    for s in tuple(map(int,Si.readline().split())):
        sub[s] = sub.get(s,0)+1
        
    Vp = max(h.items(), key=ig(1))
    VP = [k for k in h if h[k]==Vp[1]]
    print(VP)
    if len(VP)==1:  print(VP[0])
    else:
        '''
        M,Ap = -m,None
        for v in VP:
            if v not in sub:    continue
            if sub[v]>M: Ap=v;M=sub[v]
        print(Ap)
        '''
        tp = {v:lan[v] for v in VP if v in lan}
        ap = max(tp.items(),key=ig(1))
        AP = [k for k in tp if tp[k]==ap[1]]
        if len(AP)==1:  print(AP[0])
        else:
            M,Ap = -m,None
            for v in VP:
                if v not in sub:    continue
                if sub[v]>M: Ap=v;M=sub[v]
            print(Ap)
            
        
'''
C. Cinema
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Moscow is hosting a major international conference, which is attended by n scientists from different countries. Each of the scientists knows exactly one language. For convenience, we enumerate all languages of the world with integers from 1 to 109.

In the evening after the conference, all n scientists decided to go to the cinema. There are m movies in the cinema they came to. Each of the movies is characterized by two distinct numbers — the index of audio language and the index of subtitles language. The scientist, who came to the movie, will be very pleased if he knows the audio language of the movie, will be almost satisfied if he knows the language of subtitles and will be not satisfied if he does not know neither one nor the other (note that the audio language and the subtitles language for each movie are always different).

Scientists decided to go together to the same movie. You have to help them choose the movie, such that the number of very pleased scientists is maximum possible. If there are several such movies, select among them one that will maximize the number of almost satisfied scientists.
Input

The first line of the input contains a positive integer n (1 ≤ n ≤ 200 000) — the number of scientists.

The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 109), where ai is the index of a language, which the i-th scientist knows.

The third line contains a positive integer m (1 ≤ m ≤ 200 000) — the number of movies in the cinema.

The fourth line contains m positive integers b1, b2, ..., bm (1 ≤ bj ≤ 109), where bj is the index of the audio language of the j-th movie.

The fifth line contains m positive integers c1, c2, ..., cm (1 ≤ cj ≤ 109), where cj is the index of subtitles language of the j-th movie.

It is guaranteed that audio languages and subtitles language are different for each movie, that is bj ≠ cj.
Output

Print the single integer — the index of a movie to which scientists should go. After viewing this movie the number of very pleased scientists should be maximum possible. If in the cinema there are several such movies, you need to choose among them one, after viewing which there will be the maximum possible number of almost satisfied scientists.

If there are several possible answers print any of them.
Examples
Input

3
2 3 2
2
3 2
2 3

Output

2

Input

6
6 3 1 1 3 7
5
1 2 3 4 5
2 3 4 5 1

Output

1

Note

In the first sample, scientists must go to the movie with the index 2, as in such case the 1-th and the 3-rd scientists will be very pleased and the 2-nd scientist will be almost satisfied.

In the second test case scientists can go either to the movie with the index 1 or the index 3. After viewing any of these movies exactly two scientists will be very pleased and all the others will be not satisfied.
'''
