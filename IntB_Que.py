class Queue(object):

    def __init__(self):
        self.Q = []

    def insert(self,value):
        self.Q.append(value)

    def delete(self):
        self.Q.pop(0)

    def genIt(self):
        for value in self.Q:    yield value

    def _print(self):
        return self.Q



myq = Queue()
nyq = Queue()
print (type(myq),type(nyq))

for i in range(10,0,-1):
    myq.insert(i)

for x in myq.genIt():
    print (x)
    print ('its done')

myq.delete()
x = myq._print()
print (x)

