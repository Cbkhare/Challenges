if __name__=='__main__':
    n = int(input())
    for i in range(n):
        lRope = int(input())
        upNode = list(map(int,input().split(' ')))
        loNode = list(map(int,input().split(' ')))
        for i in range(lRope-1):
            upNode[i] = upNode[i] - (lRope-i)+1
            loNode[i] = loNode[i] - (lRope-i)+1
        #print(loNode,upNode,lRope)
        extra = max(max(upNode),max(loNode),0)
        print (extra+lRope)


'''
Roy has a rope of length L

meters. This rope has several other ropes attached to it at the end of every meter (except for the end of the rope).
At each meter there are two ropes attached to this main rope, let's call them upper and lower ropes. See the following example.

enter image description here

Roy lit the rope on fire from the left end. This fire burns down the rope by 1

meter/minute.
Your task is to find how much time (in minutes) will the fire take to burn down the entire rope.

Input:
First line contains T
- number of test cases.
First line of each test case contains L - length of the rope.
Second line of each test case contains L−1 integers separated by space denoting lengths of all the upper ropes at each meter.
Third line of each test case contains L−1

integers separated by space denoting lengths all the lower ropes at each meter.

Output:
Output the time (in minutes) required to burn down the entire rope for each test case in a new line.

Constraints:
1≤T≤10

2≤L≤1000000
0≤upper[i]≤1000000 where 1≤i≤L−1
0≤lower[i]≤1000000 where 1≤i≤L−1

Sample Explanation:

Follow the nature of fire. Note that after 1
min. Fire can go in all three directions. Hence after 2 mins fire burnt 1 meter in all 3

directions. Rest is explained in the image below.

enter image description here
SAMPLE INPUT

1
5
1 2 1 2
1 0 2 1

SAMPLE OUTPUT

6

Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, CPP, CLOJURE, CSHARP, GO, HASKELL, JAVA, JAVASCRIPT, JAVASCRIPT_NODE, LISP, OBJECTIVEC, PASCAL, PERL, PHP, PYTHON, RUBY, R, RUST, SCALA
Link:- https://www.hackerearth.com/problem/algorithm/roy-and-ropes/description/
'''
