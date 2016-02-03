def time(d,l,v1,v2):
	x = ((v1*(l-d))/(v1+v2))
	return (x/v1)
	
if __name__ == '__main__':

    d,l,v1,v2 = map(int,input().split(' '))
    print (round((time(d,l,v1,v2)),6))

'''

A. Save Luke
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Luke Skywalker got locked up in a rubbish shredder between two presses. R2D2 is already working on his rescue, but Luke needs to stay alive as long as possible. For simplicity we will assume that everything happens on a straight line, the presses are initially at coordinates 0 and L, and they move towards each other with speed v1 and v2, respectively. Luke has width d and is able to choose any position between the presses. Luke dies as soon as the distance between the presses is less than his width. Your task is to determine for how long Luke can stay alive.
Input

The first line of the input contains four integers d, L, v1, v2 (1 ≤ d, L, v1, v2 ≤ 10 000, d < L) — Luke's width, the initial position of the second press and the speed of the first and second presses, respectively.
Output

Print a single real value — the maximum period of time Luke can stay alive for. Your answer will be considered correct if its absolute or relative error does not exceed 10 - 6.

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if .
Sample test(s)
Input

2 6 2 2

Output

1.000000

Input

1 9 1 2

Output

2.666667

Note

In the first sample Luke should stay exactly in the middle of the segment, that is at coordinates [2;4], as the presses move with the same speed.

In the second sample he needs to occupy the position . In this case both presses move to his edges at the same time.
'''
        
    
