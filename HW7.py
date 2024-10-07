#Name: Eric Lin
#Class: 5th hour
#Assignment: HW7

print('Hello world')

time = 0
wifi = True
login = True
admin = True



if wifi == True :
    if login == True :
        if admin == True :
            print('Welcome sir')
            time += 1
        else:
            print('admin has an Error')
    else:
        print('login has an Error')
else:
    print('wifi has an Error')



#1. Print Hello World!

#2. Create three different boolean variables named wifi, login, and admin.

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".