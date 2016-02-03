from sys import maxsize as m 
if __name__ == '__main__':
    c = tuple(map(int,input().split(' ')))
    mx,mn = -m,+m  #max,min
    #use pythonic max, min function to skip below for loop to find max min 
    for n in c:
        if n >mx:
            mx = n
        if n <mn:
            mn = n
    least = mx
    for num in range(mn,mx+1):
        if num not in c:
            if num < least: least = num
    print(least)
        
    
'''
How can I find the smallest missing number in the array?
Example: A = [5, -3, 2, 1, 0, -2, 4]
return -1
'''
