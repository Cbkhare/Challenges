if __name__=='__main__':
    n = int(input())
    d = input()
    count  = 0
    i=0
        
    while i <=len(d)-2:
        hori,veri =0,0
        if d[i] in ['U','D']:
            if d[i]=='U':   veri+=1
            else:   veri-=1
        elif d[i] in ['L','R']:
            if d[i]=='R':   hori+=1
            else:   hori-=1
        j=i+1
        while j<=len(d)-1:
            if d[j]=='U':
                veri+=1
            elif d[j]=='D':
                veri-=1
            elif d[j]=='L':
                hori-=1
            elif d[j]=='R':
                hori+=1
            if veri==0 and hori==0:
                count+=1
            j+=1
        i+=1
    print (count)

'''
A. Robot Sequence
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Calvin the robot lies in an infinite rectangular grid. Calvin's source code contains a list of n commands, each either 'U', 'R', 'D', or 'L' — instructions to move a single square up, right, down, or left, respectively. How many ways can Calvin execute a non-empty contiguous substrings of commands and return to the same square he starts in? Two substrings are considered different if they have different starting or ending indices.
Input

The first line of the input contains a single positive integer, n (1 ≤ n ≤ 200) — the number of commands.

The next line contains n characters, each either 'U', 'R', 'D', or 'L' — Calvin's source code.
Output

Print a single integer — the number of contiguous substrings that Calvin can execute and return to his starting square.
'''
        
