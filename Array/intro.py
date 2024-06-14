# Arrays are used to store multiple values un one single variable
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Access the elements of an array
x = cars[0]
print(x)

# Modify the value of the first array item
cars[0] = "Toyota"
print(cars)

# Length of an Array
x = len(cars)
print(x)

# Looping array elements
for x in cars:
    print(x)

# Adding array elements
cars.append("Honda")
print(cars)

# Removing array elements
cars.pop(1)  # removing second element [removing by position]
print(cars)

cars.remove("BMW")  # removing by element
print(cars)

# Remove all elements
cars.clear()
print(cars)

# Copy a list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# Count the numer of times the value appears in the list
x = fruits.count("cherry")
print(x)

# Add the elements of a list (or any iterable), to th