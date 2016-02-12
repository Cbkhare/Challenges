if __name__=='__main__':
    str1 = input()       #Gogol
    str2 = input()       #Pineapple

    if str2 in str1:
        h = 0
        while str2 in str1:
            #print (str1)
            i = str1.index(str2)
            h += 1 
            str1 = str1[i+len(str2):]
        print (h)
    else:
        print (0)

'''

B. War of the Corporations
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

A long time ago, in a galaxy far far away two giant IT-corporations Pineapple and Gogol continue their fierce competition. Crucial moment is just around the corner: Gogol is ready to release it's new tablet Lastus 3000.

This new device is equipped with specially designed artificial intelligence (AI). Employees of Pineapple did their best to postpone the release of Lastus 3000 as long as possible. Finally, they found out, that the name of the new artificial intelligence is similar to the name of the phone, that Pineapple released 200 years ago. As all rights on its name belong to Pineapple, they stand on changing the name of Gogol's artificial intelligence.

Pineapple insists, that the name of their phone occurs in the name of AI as a substring. Because the name of technology was already printed on all devices, the Gogol's director decided to replace some characters in AI name with "#". As this operation is pretty expensive, you should find the minimum number of characters to replace with "#", such that the name of AI doesn't contain the name of the phone as a substring.

Substring is a continuous subsequence of a string.
Input

The first line of the input contains the name of AI designed by Gogol, its length doesn't exceed 100 000 characters. Second line contains the name of the phone released by Pineapple 200 years ago, its length doesn't exceed 30. Both string are non-empty and consist of only small English letters.
Output

Print the minimum number of characters that must be replaced with "#" in order to obtain that the name of the phone doesn't occur in the name of AI as a substring.
Sample test(s)
Input

intellect
tell

Output

1

Input

google
apple

Output

0

Input

sirisiri
sir

Output

2

Note

In the first sample AI's name may be replaced with "int#llect".

In the second sample Gogol can just keep things as they are.

In the third sample one of the new possible names of AI may be "s#ris#ri".

'''