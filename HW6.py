#Name: Eric Lin
#Class: 5th hour
#Assignment: HW6
from selectors import SelectSelector

print('Hello world')

num1 = int(input())

if num1 % 2 == 0:
    print('your number us divisible by 2')
    x = num1 / 2
    print(x)
else num1 % 3 == 0:
    print('your number is divisible by 2 ')
    y = num1 / 3
    print(y)
else:



# If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3