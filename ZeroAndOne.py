def m (A):
    i = 0
    n = len( A )
    while i < n:
        #print (A)
        if A[i]==0:
            x = A.pop( i )
            A = [ x ] + A

        if A[ i ]==1:
            i+=1
    return A

print (m([1,0,0,1,1,1,0,0]))

