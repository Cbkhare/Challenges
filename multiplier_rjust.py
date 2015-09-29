w = 4
for i in range(1,13):
    stack = []
    for j in range (1,13):
        stack.append(i*j)
        '''
    line_new = '{:>2}  {:>2}  {:>2}   {:>2}   {:>2}'.format(stack[0],stack[1],\
                                            stack[2],stack[3],stack[4],\
                                            stack[5],stack[6],stack[7],\
                                            stack[8],stack[9],stack[10],\
                                            stack[11],stack[12])
    '''
    stack = list(map(str,stack))
    line_new =stack[0].rjust(w)+stack[1].rjust(w)+\
              stack[2].rjust(w)+stack[3].rjust(w)+stack[4].rjust(w)+\
              stack[5].rjust(w)+stack[6].rjust(w)+stack[7].rjust(w)+\
              stack[8].rjust(w)+stack[9].rjust(w)+stack[10].rjust(w)+\
              stack[11].rjust(w)
    print (line_new)
    #print (line_new.replace('\'','').replace(', ','').replace('(','').replace(')',''))

    '''

Study more on Input Formating

https://docs.python.org/3/tutorial/inputoutput.html

'''
