import sys
from itertools import chain

file_name = sys.argv[1]
fp = open(file_name, 'r+')
contents = [line.strip('\n') for line in fp]

#print (contents)


def replace_n_sum(rac):
     romans = {'I':'1','V':'5','X':'10','L':'50','C':'100','D':'500','M':'1000'}
     
     for i in range(len(rac)):       #repalcing characters with numerals
          if rac[i] in romans:
               rac[i]=romans[rac[i]]
     rac = list(map(int,rac))
     #print (rac)

     for i in range(1,len(rac)-2,2):   #checing if trailing roman is less than
          if rac[i] < rac[i+2]:        # if yes, multiply it by -1
               rac[i]=rac[i]*(-1)
     #print (rac) 

     summ = []

     for i in range (0,len(rac)-1,2):  # appending multiplication of
          summ.append(rac[i]*rac[i+1]) # arabic and numeral
     return  (sum(summ))               # summing
          
for item in contents:
     string = []
     for i in item: #other Method but diff ans:- string =[i.split(' ') for i in item]
          string = list(chain(string,i))
     result = replace_n_sum(string)

     print (result)


'''

 This challenge involves calculating the value of “aromatic” numbers which are a combination of Arabic digits and Roman numerals.
An aromatic number is of the form A1R1A2R2 ... AnRn, where each Ai is an Arabic digit, and each Ri is a Roman numeral. Each pair AiRi contributes a value described below, and by adding or subtracting these values together we get the value of the entire aromatic number.
An Arabic digit A can be 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9.
A Roman numeral R is one of the seven letters I, V, X, L, C, D, or M. Each Roman numeral has a base value: 1, 5, 10, 50, 100, 500, 1000, respectively.
The value of a pair AR is A times the base value of R. Normally, you add up the values of the pairs to get the overall value. However, wherever there are consecutive symbols ARA`R` with R` having a strictly bigger base value than R, the value of pair AR must be substracted from the total, instead of being added.
For example, the number 3M1D2C has the value 3 × 1000 + 1 × 500 + 2 × 100 = 3700 and 3X2I4X has the value 3 × 10 - 2 × 1 + 4 × 10 = 68 . Write a program that calculates the values of aromatic numbers.
Input sample:

3M1D2C
2I3I2X9V1X


The input is a valid aromatic number consisting of between 2 and 20 symbols. Your program should accept as its first argument a path to a filename. E.g.:
Output sample:

3700
-16


The output is the decimal value of the given aromatic number.
'''


