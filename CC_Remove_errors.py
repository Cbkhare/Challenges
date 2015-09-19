tc = int(input())

for i in range(tc):

    sb = input()     #start bit
    eb = input()     #end bit 
    ds = input()     #data stream
    stack = []

    while len(ds)!= 0:
        while sb in ds:
            s = ds.index(sb)        #-1 bcoz it is a zero based list
            if eb in ds:
                e = ds.index(eb)+len(eb)   #-1 is exclded to include last char of eb 
                if e > s:
                    #print (ds[s:e],s,e)
                    st = ds[:e].replace(ds[s:e],'')
                    stack.append(st)
                    ds=ds[e:]
                    #print (ds)
                else:
                    e = e-len(eb)-1
                    #print (ds[:s])
                    stack.append(ds[:s])
                    #print (stack,ds[s:])
                    ds = ds[s:]
            else:
                break
        stack.append(ds)
        ds=''
    print (''.join(stack))


'''
Remove Errors


Problem code: NU02
	

    Submit
    My Submissions
    All Submissions

All submissions for this problem are available.

 

Yathu and Pinku are two network engineers and they are playing with data link layer now a days. Pinku receives the bit data stream from multiple machine and sends it to Yathu's. While sending from one machine,Pinku noticed that some of the bits are Takleef-wala. Yathu does have error correction and detection algorithms but he has no idea how to deal with Takleef-wala bits. So They both found a way out.The method is : While sending the bit stream, Pinku will add a start flag at the starting of the Takleef-wala bits and an end flag at the end of it.

Yathu has to remove every bit between the strat flag and end flag including the flags themselves. Now Yathu is so busy that he asks you to write a code for it. 
Input

Each input has first line denoting the number of test cases (less than 100)

The following three lines are for

start flag (less than 10 charecters)

end flags (less than 10 charecters)

data stream (less than 1000 charecters)

The flags and data stream will be in binary (0 and 1) only.

 
Output

For each test case, print a single line denoting the data bits stream without Takleef wala bits and flags

 
Constraints

 
Example

Input:
3
10
11
10101011111110101010010010100110001111111110101010101010001111
00
00
000000000000000000000000000000000000
111
000
11101010100011011
Output:
11110001111111111
 
11011
'''
