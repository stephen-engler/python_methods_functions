#map
def square(num):
    return num**2

my_nums = [1,2,3,4,5]


for item in map(square, my_nums):
    print(item)

square_num = list(map(square, my_nums))
print(square_num)

#filter
def check_even(num):
    return num%2 == 0

my_nums = [1,2,3,4,5,6,7]

even_nums = list(filter(check_even, my_nums))
print(even_nums)

#lamba or anonymous function
lambda num: num**2

squared_nums = list(map(lambda num: num**2, my_nums))
print(squared_nums)

