def odd(num):
  new_num = int((num-1)/2)
  return new_num

def even(num):
  new_num = int(num/2)
  return new_num

def even2(num):
  new_num = 2*num
  return new_num

def check_pow(num):    #chck if num is power of 2, also includes 1
  if num == int(num):
    num = int(num)
    return ((num & (num-1))==0) and num != 0
  else:
    return False

      

def find_ways(kase):
  ini,tar,l = kase[0],kase[1],len(kase)   #Initial, Target, Length values
  result = 0
  count = 0
  '''
  excluding cases where target
  1) when even, is not a power of 2. For this cases it doesn't matter if initial
     value is even or odd.
  2) when odd, is other than '1'. other values can never be achieved. Also for
     this case it doesn't matter if initial value is even or not.
  Only possible cases, when initial value is :
  Pure even fun:- 4,1.. 4,32(tar/ini= pow of 2)..4,32(target is pow of 2)
  Pure odd fun :- 5,1.. 5,10(tar/ini= pow of 2)..5,32(target is pow of 2)
  A composite  :- 6,1.. 6,12(tar/ini= pow of 2)
  '''
  #First case every thing is odd and tar!=1
  if tar%2 != 0 and tar!=1:  return result

  #Second case (4,1) & (5,1) & (6,1)
  if tar==1:
    if ini%2 ==0:       # if ini is even 
      while ini//2 >=1:  #reaching init =1 
        ini = even(ini)
        if ini%2 != 0 and ini !=1:  #if ini becomes odd and not equal to one 
          ini = odd(ini)
          count +=1
        count +=1
      result = count
    else:
        while ini%2!=0 and ini!=1:
          ini = odd(ini) #making odd to even 
          count +=1
        while ini//2 >=1:  #reaching init =1 
          ini = even(ini)
          if ini%2 != 0 and ini !=1:  #if ini becomes odd and not equal to one 
            ini = odd(ini)
            count +=1
          count +=1
        result = count
    return result             #end of second case


  #Third case when ini could be even or odd but tar is power of 2

  if check_pow(tar):    #if tar is power of 2
      if ini%2 ==0:     #if ini is even or odd
          if check_pow(ini):    #if ini is power of 2
            if ini < tar:
              while ini!=tar:
                ini=even2(ini)
                count +=1
              result = count
            else:
              while ini!=2:
                ini=even(ini)
                count +=1
              result = count
          else:                              #Reduce to pow of 2 and then raise 
            while check_pow(ini) == False:   #Note no. less than pow of 2 wont enter
              ini = even(ini)
              if ini%2 != 0 and ini !=1:   #though ini!=1 is not needed
                ini = odd(ini)
                count +=1
              count +=1
            while ini!= tar:
              ini = even2(ini)
              count +=1
            result = count
      else:                #if num is odd
        while ini%2 !=0 and ini!=1:      #making odd to even 
          ini = odd(ini)
          count +=1
          
        while check_pow(ini)==False:     #untill even comes to a power of 2
          ini=even(ini)
          if ini%2 !=0:
            ini=odd(ini)
            count +=1
          count+=1
          
        while ini != tar:
          ini =even2(ini)
          count +=1
        result = count
      return result         #end of third case

    

  #Fourth case when target is composite while ini could be even or odd

  if tar%2==0 and check_pow(tar) == False:  #tar is even but not a pow of 2
      if ini%2 ==0: # if ini is even
        if check_pow(ini):   #ini is a pow of 2
          result = 0         #target can never be achieved
        elif check_pow(tar/ini):   #if tar is a multiple of 2 with 2''s power
          while ini != tar:
            ini=even2(ini)
            count+=1
          result = count
        else:               #for any other cases 
          result = 0
      else:          #if num is odd
        if check_pow(tar/ini):
          '''
          while ini%2 !=0 and ini!=1:  #converting odd to even
              ini =odd(ini)
              count +=1
          while check_pow(ini)==False:  #converting even to pow of 2
            ini=even(ini)
            if ini%2 != 0:
              ini=odd(ini)
              count +=1
            count +=1
            '''
          while ini != tar:
            ini =even2(ini)
            count +=1
          result =count
        else:
          result = 0
      return result
        
          
            
              
    

n_case = int(input())
stack =[]
for i in range(n_case):
  case = list(map(int,input().split(' ')))
  case = find_ways(case)
  stack.append(case)

for i in stack: print (i)






'''
Chef is on a vacation these days, so his friend Chefza is trying to solve Chef's everyday tasks.
Today's task is to make a sweet roll. Rolls are made by a newly invented cooking machine. The machine is pretty universal - it can make lots of dishes and Chefza is thrilled about this.
To make a roll, Chefza has to set all the settings to specified integer values. There are lots of settings, each of them set to some initial value. The machine is pretty complex and there is a lot of cooking to be done today, so Chefza has decided to use only two quick ways to change the settings. In a unit of time, he can pick one setting (let's say its current value is v) and change it in one of the following ways.
    If v is even, change this setting to v/2. If v is odd, change it to (v − 1)/2.
    Change setting to 2 × v
The receipt is given as a list of integer values the settings should be set to. It is guaranteed that each destination setting can be represented as an integer power of 2.
Since Chefza has just changed his profession, he has a lot of other things to do. Please help him find the minimum number of operations needed to set up a particular setting of the machine. You can prove that it can be done in finite time.
Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains two integers A and B denoting the initial and desired values of the setting, respectively.
Output
For each test case, output a single line containing minimum number of operations Chefza has to perform in order to set up the machine.
Constraints
    1 ≤ T ≤ 200
    1 ≤ A ≤ 107
    1 ≤ B ≤ 107, and B is an integer power of 2
Subtasks
    Subtask #1 [40 points]: A ≤ 100 and B ≤ 100
    Subtask #2 [60 points]: No additional constraints
Example
Input:
6
1 1
2 4
3 8
4 16
4 1
1 4
Output:
0
1
4
2
2
2
Explanation
    In the first test case, you don't need to do anything.
    In the second test case, you need to multiply 2 by 2 and get 4. This is done in 1 operation.
    In the third test case, you need to obtain 1 from 3 and then multiply it by 2 three times to obtain 8. A total of 4 operations.
    In the fourth test case, multiply 4 by 2 twice.
    In the fifth test case, divide 4 by 2 twice.
    In the sixth test case, multiply 1 by 2 twice.
'''
