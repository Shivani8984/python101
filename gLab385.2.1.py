# Working with Lists and Functions 


# # Creating a list with mixed data types
tools = ["Laptop", "Monitor", "Keyboard", "Mouse"]

# # Accessing elements by position (0-based)
print(tools[0])
print(tools[-1])

# Slicing: [Start : Stop] - Note: Stop index is exclusive
sub_list = tools[1:3]
print(sub_list) 

# Changing a value at a specific index
tools[2] = "Webcam"
print(tools)

# Use append() to add to the end of the list
tools.append("Keyboard")
tools.append("Desk")
print(tools)

# Use insert() to add at a specific index
tools.insert(1, "Headphones")
print(tools)


# Use remove() to delete a specific value by name
tools.remove("Keyboard")
print(tools)

# Using the len() function to see total count
total_items = len(tools)
print(total_items)


original_list = [1, 2, 3]

# new_reference points to the same list object
new_reference = original_list

# Modify the list through the new reference
new_reference.append(4)

print("Original List:", original_list)
print("New Reference:", new_reference)
print(original_list == new_reference)


original_list = ["A", "B", "C"]

# Create a true copy of the list
copied_list = original_list.copy()

# Modify the copied list
copied_list.append(4)

print("Original List:", original_list)
print("Copied List:", copied_list)
print(original_list == copied_list)


furniture_list1 = ["table", "chair", "lamp"]

# This creates another reference, not a copy
furniture_list_append = furniture_list1

furniture_list_append.append("armoire")

print("---------- furniture----------")
print(furniture_list1)
print("---------- furniture_list_append----------")
print(furniture_list_append)


# Using .reverse() and .extend() methods
def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in chronological order.
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists combined in chronological order.
    return recent_last

# Assign the two lists to the two variables to be passed to the record_profit_years() function.
recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

# Call the record_profit_years() function and pass the two lists as  parameters.
print(record_profit_years(recent_first, recent_last))

# another example to better understand 

# Initial to-do list
tasks = ["write report", "email client", "update website"]

# New tasks coming from another source
new_tasks = ["fix bug", "team meeting"]

# Add the new tasks to the existing list
tasks.extend(new_tasks)

print("After extend:", tasks)

# Reverse the order of tasks (maybe you want to start from the newest)
tasks.reverse()

print("After reverse:", tasks)
