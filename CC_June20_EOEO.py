from sys import stdin as si


def evaluate(s):
    if s % 2 != 0:
        print(s//2)
    else:
        count_of_2 = 0
        original = s
        while s % 2 == 0:
            count_of_2 += 1
            s //= 2
        print(original//pow(2, count_of_2+1))
    return


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        s = int(si.readline().strip())
        evaluate(s)

"""
https://www.codechef.com/JUNE20B/problems/EOEO
- find the prime factor of s 
- count the number of 2.
- For jerry to win the game, jerry's strength should have one extra count of as calculated above.
- With above step, jerry will always win as per condition 1 mentioned in the question. 
"""
