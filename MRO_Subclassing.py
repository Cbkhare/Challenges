class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.movable.draw()
        super().draw()

class MovableColoredShape(MoveableAdapter, ColoredShape):
    pass

class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

MovableColoredShape(color='red', shapename='triangle',
                    x=10, y=20).draw()



'''
import collections

class CountedOrderedDict(collections.OrderedDict):
    def __init__(self, *args, **kwargs):
        self.counter = collections.Counter()
        super(CountedOrderedDict, self).__init__(*args, **kwargs)

    def __delitem__(self, key):
        super(CountedOrderedDict, self).__delitem__(key)
        self.counter[key[1]] -= 1

    def __setitem__(self, key, value):
        if key not in self:
            self.counter[key[1]] += 1

        super(CountedOrderedDict, self).__setitem__(key, value)

my_dict = CountedOrderedDict({(123,1): 'sda', (232,1) : 'bfd', (234,2) : 'csd', (6745,2) : 'ds', (456,3) : 'rd'})
print(my_dict.counter)

+++++++++++++++
import collections

Lines = int(input())
words = collections.OrderedDict()
for i in range(Lines):
    add = input()
    words[i]=add
for k,v in words:
    counter = collections.Counter(v)
#counter = collections.Counter(words[)
print (words, counter)
+++++++
counter = Counter(List_of_words)
count_list = []
for items in counter:
    count_list.append(counter[items])
count_list.reverse()
print (count_list)
'''

