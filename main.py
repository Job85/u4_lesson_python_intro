from operator import truediv


name = 'Julian'
int_var = 36
max_sum = 100
completed = True
immutable_list = ('What', 'is', 'a', 'tuple', 'used', 'for' '?')
numbers_list = ['1', '2', '3', '3.5']
dictionary_definitions = {'eyes': 'blue'}

# Hello
# Big
# Blue
# World
# !

print("36")

print("Julian")


print('{sum}'.format(sum=10+10))

a = 10
b = 10
c = a + b
print(c)

print('{difference}'.format(difference=43-23))

a = 43
b = 23
c = a - b
print(c)

x = 5
y = 4
r = x % y
print('Remainder', r)
print('{remainder}'.format(remainder=5 % 4))


print('{product}'.format(product=2*3))

print('{dividend}'.format(dividend=10/5))

print('{power}'.format(power=3**4))

a = 4
a += 3.4
print(a)
