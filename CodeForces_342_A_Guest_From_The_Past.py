if __name__=='__main__':
    r = int(input())
    a = int(input())    #plastic bottle
    b = int(input())    #glass bottl e
    c = int(input())    #return on glass bottle
    d = 0               #drinks
    if b-c>=a:
        d+=r//a
        r =r%a
        #print('a',d,r)
    else:
        if r>=b:
            t = (r - b + 1)//(b-c)
            d += t
            r -= t * (b-c)
            if r >= b:
                r -= (b-c)
                d += 1
        d+=r//a
        
    '''
        while r>=b:
            d+=r//b
            r = r%b + c*(r//b)
            print(d,r)
        if r>=a:    d+=r//a
    '''
    print (d)
'''

A. Guest From the Past
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Kolya Gerasimov loves kefir very much. He lives in year 1984 and knows all the details of buying this delicious drink. One day, as you probably know, he found himself in year 2084, and buying kefir there is much more complicated.

Kolya is hungry, so he went to the nearest milk shop. In 2084 you may buy kefir in a plastic liter bottle, that costs a rubles, or in glass liter bottle, that costs b rubles. Also, you may return empty glass bottle and get c (c < b) rubles back, but you cannot return plastic bottles.

Kolya has n rubles and he is really hungry, so he wants to drink as much kefir as possible. There were no plastic bottles in his 1984, so Kolya doesn't know how to act optimally and asks for your help.
Input

First line of the input contains a single integer n (1 ≤ n ≤ 1018) — the number of rubles Kolya has at the beginning.

Then follow three lines containing integers a, b and c (1 ≤ a ≤ 1018, 1 ≤ c < b ≤ 1018) — the cost of one plastic liter bottle, the cost of one glass liter bottle and the money one can get back by returning an empty glass bottle, respectively.
Output

Print the only integer — maximum number of liters of kefir, that Kolya can drink.
Sample test(s)
Input

10
11
9
8

Output

2

Input

10
5
6
1

Output

2

Note

In the first sample, Kolya can buy one glass bottle, then return it and buy one more glass bottle. Thus he will drink 2 liters of kefir.

In the second sample, Kolya can buy two plastic bottle and get two liters of kefir, or he can buy one liter glass bottle, then return it and buy one plastic bottle. In both cases he will drink two liters of kefir.
'''
