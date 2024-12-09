#Team Members: Gage & Eric
#Class: 5th Hour
#Assignment: Scenario 5


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.
WalmartList17 = ['Egg',"Bread","Ham","Bacon","Milk","Cheese","Cereal","Frozen Pizza","Burger","Wigs","Tv","Couch","Christmas Tree","Wrapping Paper","Wings","Cheetos Puffs"]
print("Welcome to Walmart Online")

while 1 == 1:
    User = int(input("Login (1) or Create Account (2)  :"))

    if User == 1:
        print("Login Selected")
        accname = input("Input Account Name :")
        print(f"Welcome {accname}")
        input("Input Password :")
        break

    if User == 2:
        print("Create Account Selected")
        accnamed = input("Input New Account Name :")
        print(f"Welcome {accnamed}")
        input("Input New Password :")
        break

    else:
        print("Try again")
        continue




