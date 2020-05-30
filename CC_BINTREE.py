# cook your dish here
from sys import stdin as si

def evaluate(a, b):
    step = 0
    lookup = {a: 0}
    while a > 1:
        step += 1
        lookup[a//2] = step
        a //= 2
    step_b = 0
    while b > 1:
        if b in lookup:
            break
        step_b += 1
        b //= 2
    return lookup[b] + step_b


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        a, b = map(int, si.readline().strip().split())
        print(evaluate(a, b))
