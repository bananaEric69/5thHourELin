#Team Members: Gage & Eric
#Class: 5th Hour
#Assignment: Scenario 5


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.
WalmartList17 = ['Egg',"Bread","Ham","Bacon","Milk","Cheese","Cereal","Frozen Pizza","Burger","Wigs","Tv","Couch","Christmas Tree","Wrapping Paper","Wings","Cheetos Puffs","Fries"]
print("Welcome to Walmart Online")
ao = 0
buyingList = []

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

print(f"The options are {WalmartList17}")




while 1 == 1:
    item = int(input("What item do you want to add?    -"))

    ao +=1

    if item == 1:
        print("Eggs Added.")
        buyingList.append("Eggs")

    if item == 2:
        print("Bread Added.")
        buyingList.append("Bread")

    if item == 3:
        print("Ham Added.")
        buyingList.append("Ham")

    if item == 4:
        print("Bacon Added.")
        buyingList.append("Bacon")

    if item == 5:
        print("Milk Added.")
        buyingList.append("Milk")

    if item == 6:
        print("Cheese Added.")
        buyingList.append("Cheese")

    if item == 7:
        print("Cereal Added.")
        buyingList.append("Cereal")

    if item == 8:
        print("Frozen Pizza Added.")
        buyingList.append("Frozen Pizza")

    if item == 9:
        print("Burger Added.")
        buyingList.append("Burger")

    if item == 10:
        print("Wigs Added.")
        buyingList.append("Wigs")

    if item == 11:
        print("Tv Added.")
        buyingList.append("Tv")

    if item == 12:
        print("Couch Added.")
        buyingList.append("Couch")

    if item == 13:
        print("Christmas Tree Added.")
        buyingList.append("Christmas Tree")

    if item == 14:
        print("Wrapping Paper Added.")
        buyingList.append("Wrapping Paper")

    if item == 15:
        print("Wings Added.")
        buyingList.append("Wings")

    if item == 16:
        print("Cheetos Puffs Added.")
        buyingList.append("Cheetos Puffs")

    if item == 17:
        print("Fries Added.")
        buyingList.append("Fries")




    if item >= 18 or item < 1:
        print("ERROR Try Again")
        continue





    exiter = int(input("Press 1 To Exit, If You Want To Continue, Press Any Other Number."))


    if exiter == 1:
        print(f'Total Items Bought Was {ao}')
        break

    else:

        continue









