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
    return 'dog' in mystring.lower()

def pig_latin(word):
    first_letter = word[0]

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('apple'))
