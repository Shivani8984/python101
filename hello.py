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

# Create a receipt
customerName = input("Enter Customer's name: ")
itemPrice = float(input("What is the cost of item: "))
quantity = int(input("Enter Quantity: "))
totalCost = itemPrice * quantity
roundedCost = round(totalCost)



print("Receipt")
print("--------------------")
print(f"Customer Name: {customerName}")
print(f"Item Price: ${itemPrice}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${roundedCost}")
