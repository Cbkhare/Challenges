if __name__=='__main__':
    d,t = map(int,input().split(' '))
    result = 0
    i2 = d*2
    i3 = t*3
    cm = int(max(i2,i3)/6)  #common
    while cm>0:
        if i2+2<i3+3:
            i2+=2
        elif i2+2> i3+3:
            i3+=3
        else:
            i2+=2
            cm+=1
        cm-=1
    print (max(i2,i3))

    '''
    if index2+common*2<=index3:
        result = index3
    else:
        result = index2+common*2
    if index2>=index3+common*3:
        result = index2
    '''
    '''
    while common>0:
        print (d,t,common,oldCommon)
        if (d+1)*2<=(t+1)*3:
            d+=1
        else:
            t+=1
        index2 = d*2
        index3 = t*3
        print (index2,index3)
        common = int(min(index2,index3)/6)

        x = common 
        common-=oldCommon
        oldCommon=x
    print(max(index2,index3))
    '''

'''

C. Block Towers
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Students in a class are making towers of blocks. Each student makes a (non-zero) tower by stacking pieces lengthwise on top of each other. n of the students use pieces made of two blocks and m of the students use pieces made of three blocks.

The students don’t want to use too many blocks, but they also want to be unique, so no two students’ towers may contain the same number of blocks. Find the minimum height necessary for the tallest of the students' towers.
Input

The first line of the input contains two space-separated integers n and m (0 ≤ n, m ≤ 1 000 000, n + m > 0) — the number of students using two-block pieces and the number of students using three-block pieces, respectively.
Output

Print a single integer, denoting the minimum possible height of the tallest tower.
Examples
Input

1 3

Output

9

Input

3 2

Output

8

Input

5 0

Output

10

Note

In the first case, the student using two-block pieces can make a tower of height 4, and the students using three-block pieces can make towers of height 3, 6, and 9 blocks. The tallest tower has a height of 9 blocks.

In the second case, the students can make towers of heights 2, 4, and 8 with two-block pieces and towers of heights 3 and 6 with three-block pieces, for a maximum height of 8 blocks.

'''
