# print("Hello World!")
# learner="Shivani"
# location = "Philadelphia,Pennsylvania."
# print("My name is " + learner + ". I'm from " + location)

# # Int data type
# no_of_pets = 1
# print(no_of_pets)

# # Float Data type
# how_much_is_banana = 9.99
# print(how_much_is_banana)

# # Boolean(true/False) example
# is_our_pet_vaccinated = True
# print(is_our_pet_vaccinated)

# # How to check the type of our data?
# print(type(learner))
# print(type(no_of_pets))
# print(type(how_much_is_banana))
# print(type(is_our_pet_vaccinated))

# print("5+3")

# # Ask the user their favourite color
# fav_color = input("What's your favourite color?")
# print(f"My favourite color is {fav_color}")

# # Create a receipt
# customerName = input("Enter Customer's name: ")
# itemPrice = float(input("What is the cost of item: "))
# quantity = int(input("Enter Quantity: "))
# totalCost = itemPrice * quantity
# roundedCost = round(totalCost)



# print("Receipt")
# print("--------------------")
# print(f"Customer Name: {customerName}")
# print(f"Item Price: ${itemPrice}")
# print(f"Quantity: {quantity}")
# print(f"Total Cost: ${roundedCost}")

# #This is my additional code i've written
# print("We all live in a yellow submarine")


# String Examples
# str1='This is a string in Python'
# print(str1)
# str2="This is a string in Python"
# print(str2)
# str3='''This is a string in Python'''
# print(str3)
# str4="""This is a string in Python"""
# print(str4)
# #If you need to use single quotes in your string, then wrap it in double quotes. See the following example.
# my_string = "I'm a Python programmer!"
# print(my_string)
# otherString = 'The word "python" usually refers to a snake'
# print(otherString)
# tripleString = """Here's another way to embed "quotes" in a string"""
# print(tripleString)

# Access Characters in string

# s = 'Hello World!'
# print(s[0]) #H (character at index 0)

# print(s[2:5]) #llo (substring from index 2 to 4)

# print(s[3:]) #lo World! (substring from index 3 to the end) 

# print(s*2) #Hello World!Hello World! (repeating twice)

# print(s+'Everyone!') #Hello World!Everyone!  (string concatenation)

# print(s.lower()) #hello world! (lowercase)	

# print(s.replace('l','s')) #Hesso Worsd! (replace character(s)) 

# print(len(s)) #12 (length of a string)

# print(s.strip()) #remove leading/trailing whitespaces

# print(s.split(' ')) #['Hello', 'World!'] (split into substrings list)

# string2 = 4000
# print(type(string2))
# print(type(str(string2)))

#Convert Float to string

#initializing and declaring variable and value
# floatNumberOne=11.10
# floatNumberTwo = 2/5
# print(floatNumberOne)
# print(floatNumberTwo)
# # checking data type
# print(type(floatNumberOne))
# print(type(floatNumberTwo))
# # Converting float to String
# MyStringOne = str(floatNumberOne)
# MyStringTwo = str(floatNumberTwo)

# print("Floating point into String: ", MyStringOne)
# print("Floating point into String: ", MyStringTwo)
# # checking data type
# print(type(MyStringOne))
# print(type(MyStringTwo))


# mylist=[] # create a empty list
# print(mylist)
# # Create a list of strings.
# string_list = ["Hello", "Python", "World"]
# print(string_list)
# # Create a list of numbers.
# number_list = [3, 4, 5, 6, 8, 10]
# print(number_list)
# # Create a list of boolean values.
# boolean_list = [True, False, False, True]
# print(boolean_list)
# # Create a mixed list or list with heterogeneous data
# mixed_list = [3, 4, "Python", True]
# print(mixed_list)

# string = "Hello World!"
# print(list(string))
# print(string.split())

# list_numbers = [10,20,28,369,254,23,69]
# sorted_numbers = list_numbers.sort()
# print(sorted_numbers)

# # Create a list.
# my_list = [1, 2, 3, 4, 5]
# # Traverse the list with a for loop.
# for element in my_list:
#     print(element)
# # Traverse the list by accessing the
# # indexes with the range() and len() functions.
# for i in range(len(my_list)):
#     print(f"Index {i} contains: {my_list[i]}")
    
    
# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# for EachNumber in my_list:
#      print(EachNumber)   
     
# for EachNumber in my_list:          
#     for number in EachNumber:
#         print(number)


nums = [1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]
print(nums[0])