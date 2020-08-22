from sys import stdin as si


def make_path(num):
    l = [['.' for _ in range(8)] for _ in range(8)]
    l[0][0] = 'O'
    # placing X
    if num < 64:
        # placing last X
        row = num//8
        position = num % 8
        if position < 8:
            l[row][position] = 'X'
        if row > 0:
            for i in range(position+1, 8):
                l[row][i] = 'X'
        if row < 7:
            for i in range(position+1):   # +1 for corner X
                l[row+1][i] = 'X'
    for i in range(8):
        print("".join(l[i]))
    return


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        make_path(int(si.readline().strip()))

"""
https://www.codechef.com/JULY20B/problems/ADAKING
"""
