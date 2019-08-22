# problem 1
userInput = ""

while userInput != "q":
    userInput = input("Enter anything, or press 'q' to quit: ")
    if userInput != "q":
        print(userInput)


# problem 3
# flag to flip between true or false depending on if the user enters a 'q'
flag = True

while flag is True:
    newInput = input("Enter 1 to print 1, 2 to print 2, 3 to print 3, or 'q' to quit: ")
    if newInput == "1":
        print(newInput)
    elif newInput == "2":
        print(newInput)
    elif newInput == "3":
        print(newInput)
    elif newInput == "q":
        flag = False
    else:
        print("ERROR")


# problem 4
userItem = input("Enter any input to store in a list or press 'q' to quit: ")
userList = ""
# while loop that adds any input to the previously made string and continues to concatenate new inputs
while userItem != "q":
    userList = f"{userList}, {userItem}"
    userItem = input("Add any input to the list or press 'q' to quit and see the list: ")
print(userList)

# problem 2 for fun. This asks for a name, then iterates the name as long as the number input is greater than 0
userName = input("Enter your name: ")
userNum = int(input("How many times would you like to list your name? "))
while userNum <= 0:
    userNum = int(input("Error. Please enter a positive number: "))
while userNum > 0:
    print(userName)
    userNum = userNum - 1