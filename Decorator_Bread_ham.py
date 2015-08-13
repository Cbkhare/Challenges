def bread(func):
    def wrapper():
        print ("</''''''\>")
        func()
        print ("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print ("#tomatoes#")
        func()
        print ("~salad~")
    return wrapper

@bread        #calling the bread function, this is Decorator other way to do
@ingredients  # is described in the comments 
def sandwich(food="--ham--"):
    print (food)

sandwich()


'''
sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>'''
