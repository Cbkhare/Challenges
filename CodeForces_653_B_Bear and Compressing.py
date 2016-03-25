if __name__=='__main__':
    n,m = map(int,input().split(' '))
    d = {}
    depo,res = {},[]
    def bazinga(s):
        if s in depo:   return depo[s]
        if s[0] not in d:  depo[s]=0
        else:
            ans=0
            for aa in d[s[0]]:
                if len(aa+s[1:])==n:
                    ans+=1
                    #res.append(aa+s[1:])   #if problem is to find string
                else:
                    ans+=bazinga(aa+s[1:])  #only applied when (aa+s[1:]<n)
            depo[s]=ans
        return depo[s]

    for i in range(m):
        ai,bi = map(str,input().split(' '))
        if bi in d:     d[bi] +=[ai]
        else:           d[bi]=[ai]
    print((bazinga('a')))
    #print((set(res)))

'''
B. Bear and Compressing
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Limak is a little polar bear. Polar bears hate long strings and thus they like to compress them. You should also know that Limak is so young that he knows only first six letters of the English alphabet: 'a', 'b', 'c', 'd', 'e' and 'f'.

You are given a set of q possible operations. Limak can perform them in any order, any operation may be applied any number of times. The i-th operation is described by a string ai of length two and a string bi of length one. No two of q possible operations have the same string ai.

When Limak has a string s he can perform the i-th operation on s if the first two letters of s match a two-letter string ai. Performing the i-th operation removes first two letters of s and inserts there a string bi. See the notes section for further clarification.

You may note that performing an operation decreases the length of a string s exactly by 1. Also, for some sets of operations there may be a string that cannot be compressed any further, because the first two letters don't match any ai.

Limak wants to start with a string of length n and perform n - 1 operations to finally get a one-letter string "a". In how many ways can he choose the starting string to be able to get "a"? Remember that Limak can use only letters he knows.
Input

The first line contains two integers n and q (2 ≤ n ≤ 6, 1 ≤ q ≤ 36) — the length of the initial string and the number of available operations.

The next q lines describe the possible operations. The i-th of them contains two strings ai and bi (|ai| = 2, |bi| = 1). It's guaranteed that ai ≠ aj for i ≠ j and that all ai and bi consist of only first six lowercase English letters.
Output

Print the number of strings of length n that Limak will be able to transform to string "a" by applying only operations given in the input.
Examples
Input

3 5
ab a
cc c
ca a
ee c
ff d

Output

4

Input

2 8
af e
dc d
cc f
bc b
da b
eb a
bb b
ff c

Output

1

Input

6 2
bb a
ba a

Output

0

Note

In the first sample, we count initial strings of length 3 from which Limak can get a required string "a". There are 4 such strings: "abb", "cab", "cca", "eea". The first one Limak can compress using operation 1 two times (changing "ab" to a single "a"). The first operation would change "abb" to "ab" and the second operation would change "ab" to "a".

Other three strings may be compressed as follows:

    "cab" "ab" "a"
    "cca" "ca" "a"
    "eea" "ca" "a" 

In the second sample, the only correct initial string is "eb" because it can be immediately compressed to "a".
''''
 
