# IF Statements which are used to compare things

# variable = input("This is input that takes response:  ")
# print(variable)


# height = int(input("How tall are you? "))

# if height >= 48:
#     print("You may ride")
# else:
#     print("Sorry! you may not ride right now.")
    
    
# Password Checker
#userName = Shivanip
#password = BlueJay

# password = "BlueJay"

# userLoginInput = input("Enter your password: ")

# while userLoginInput != password:
#     print("Wrong Password!Please try again")
    
#     userLoginInput = input("Enter your password: ")
# print("OPen Sesame")

# if password == userLoginInput:
#     print("Open Sesame")
# else:
#     print("Access Denied!")    

# Check Odd/even number

# inputNumber = int(input("Please Enter Number: "))

# if inputNumber %2 == 0:
#     print(inputNumber, "is Even!")
# else:
#     print(inputNumber, "is odd")    

# Write a for loop for values 1-152

# for number in range(1,153):
#     print(number)
    
#Countdown from 10-1

# for number in range(10,0,-1):
#     print(number)
#     if number == 1:
#         print("Blase Off!")
        
# numberofRootBeers = 31
# for people in range(numberofRootBeers,1 , -1):
#     print(f"{people} bottles of rootbeer on the wall...")
#     print("Take one down, pass it around...")
#     print(f"{people-1} bottles left on the wall")

# what is the sum of 1-10
# total = 0

# for i in range(1,10):
#     total = i+total
# print(f"Your total is: {total}")    

#find the largest number

# numberList = [7, 42, 8, 946, -1, 4235, 6, 730]
# largeestNumber = numberList[0]

# for i in numberList:
#     if i > largeestNumber:
#         largeestNumber = i
# print(largeestNumber)

#Guess that number!

secretNumber = 7

GuessedNumber = int(input("Please Enter Your Guess: "))

while GuessedNumber != secretNumber:        
    GuessedNumber = int(input("Please Enter Your Guess: "))
print("You Got it!")