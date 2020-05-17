from sys import stdin as si


def alternative(n):
    l = len(n)
    n = n*10
    jump = int(n[0])
    num = n[0]
    encountered = {n[0]: True}
    for _ in range(l-1):
        if n[jump] in encountered:
            return False
        num = n[jump]
        encountered[num] = True
        jump += int(num)
    if n[jump] == num or num != n[-1]:
        # number should end with last digit
        return False
    return True



if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        n = si.readline().strip()
        print(alternative(n))

"""
This solution prints whether a number is magic number or not.
A magic number is a number that has two characteristics:
    No digits repeat.
    Beginning with the leftmost digit, take the value of the digit and move that number of digits to the right. 
    Repeat the process again using the value of the current digit to move right again. Wrap back to the leftmost 
    digit as necessary. A magic number will visit every digit exactly once and end at the leftmost digit.
For example, consider the magic number 6231.
    Start with 6. Advance 6 steps to 3, wrapping around once (6→2→3→1→6→2→3).
    From 3, advance to 2.
    From 2, advance to 1.
    From 1, advance to 6.
"""
