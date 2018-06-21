#arbitrary number of arguments
#positional arguments 
def myfunc(a,b):
    # return 5% of sum of a and b
    return sum((a,b)) * 0.05
#by default python turns whatever is passed in a tupil
def newfunc(*args):
    return sum(args) * 0.05

#key word arguments
#python turns into dictionary
def anotherfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruits')

anotherfunc(fruit = 'apple')

