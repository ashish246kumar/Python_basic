# List
print("********************LIST EXAMPLE************************")
fruits: list = ["apple", "guava", "banana", "grapes", "mango"]

# Adding "coconut" to the list
fruits.append("coconut")

# Removing "grapes" from the list
fruits.remove("grapes")

# Removing the last element of the list (default pop behavior)
fruits.pop()

# Counting occurrences of "apple" in the list
print(fruits.count("apple"))

# Accessing the first element in the list (index 0)
print(fruits[0])

# Accessing the last element in the list using negative index (-1)
print(fruits[-1])
print("********************TUPLE EXAMPLE************************")

# Tuple
coordinates: tuple = (10, 20, 30,"ak")

# Printing the tuple of coordinates
print("\nTuple of coordinates:", coordinates)

# Getting the index of the first occurrence of 10 in the tuple
print(coordinates.index(10))

# Accessing the second element of the tuple (index 1)
print(coordinates[3])
print("********************SET EXAMPLE************************")

# Set
unique_number: set = {1, 2, 3, 4, 4, 5}  # Duplicates are automatically removed in a set

# Printing the set of unique numbers
print("\nSet of unique numbers:", unique_number)

# Printing the length of the set
print(f"length of set {len(unique_number)}")

# Adding a duplicate element (it won't be added since sets only allow unique values)
unique_number.add(2)
print(f"length of set after adding duplicate element {len(unique_number)}")

# Updating the set with another set (set2)
set2 = {7, 8, 8, 9, 5}
unique_number.update(set2)

# Printing the updated set
print(unique_number)

# Calculating the difference between unique_number and set2
result = unique_number.difference(set2)
print(f"unique_number.difference:-{result}")

# Removing the element 4 from the set (if it exists)
unique_number.discard(4)

# Printing the set after discarding 4
print(unique_number)

# Clearing all elements from the set
unique_number.clear()

# Printing the empty set
print(unique_number)

# Checking if 3 is present in the set (returns False since the set is now empty)
print(3 in unique_number)
print("********************DICTIONARY EXAMPLE************************")

# Dictionary
dict1: dict = {"name": "Rahul", "age": 20, "city": "Delhi"}

# Printing the dictionary
print("\nDictionary of details:", dict1)

# Accessing the value of the "name" key
print(dict1.get("name"))

# Getting all the keys in the dictionary
print(dict1.keys())

# Getting all the values in the dictionary
print(dict1.values())

# Modifying the value of the "city" key
dict1["city"] = "Gurugram"

# Removing the "age" key from the dictionary
dict1.pop("age")

# Printing the modified dictionary
print(dict1)

# Printing "Person details"
print("Person details")

# Iterating over the dictionary and printing each key-value pair
for key, value in dict1.items():
    print(key, value)
