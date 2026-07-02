# PRACTICE ACTIVITY 385.2.1 - List Excercises- Basic

# Initial guest list
guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Initial list:", guests)

# 1. Add Frank to the end
guests.append("Frank") 
print(guests)

# 2. Add Grace to the front
guests.insert(0, "Grace") 
print(guests)

# 3. Replace Charlie with Chuck
guests.remove("Charlie") 
print(guests)
guests.insert(3, "Chuck") 
print(guests)

# 4. Remove the person at index 3 (Check the list after previous steps!)
guests.remove("Chuck")

# 5. Print the final list and the total number of guests currently attending.
print("Final list:", guests)
total_no_of_guests = len(guests)
print(f"Total number of guests: {total_no_of_guests}")