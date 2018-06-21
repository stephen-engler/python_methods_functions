def name_of_function():
    '''
    Docstring: info about the function
    '''
    print('hello')
#help(name_of_function)
name_of_function()

def say_hello(name = 'Human'):
    return 'hello ' + name

say_hello()
result  = say_hello('Stephen')

def add(n1,n2):
    return n1 + n2

print(add(3,2))

#find if dog is in a string

def dog_check(mystring):
    return 'dog' in mystring.lower():
