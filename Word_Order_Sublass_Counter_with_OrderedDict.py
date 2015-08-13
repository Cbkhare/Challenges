'''
Problem Statement

You are given n words. Some words may repeat. For each word, you have to output its number of occurences. But the output order should correspond with the order of the first appearance of the word. See the sample input/output for clarification. Note that each line in the input ends with a "\n" character.

Constraints:
1≤n≤105
Sum of lengths of all the words do not exceed 106
All words are composed of lowercase-latin alphabets only.

Input Format

First line contains n.
n lines follow, ith one contains the ith word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words in the input.
In the second line, for each distinct word, output its number of occurences in the order specified in the problem statement.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1
'''

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
     'Counter that remembers the order elements are first seen'
     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__,
                            OrderedDict(self))
     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)

n = int(input())
N=[]
for i in range(n):
    add = input()
    N.append(add)
oc = OrderedCounter(N)
count =[]
for i in oc:
    count.append((oc[i]))
print (str(count).replace('[','').replace(']','').replace(',',''))
