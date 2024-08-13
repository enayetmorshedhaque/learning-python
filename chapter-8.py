# Strings are array
# Square brackets can be used to access elements of the string.
a = "Hello World!"
print(a[11])

# Looping through string
for x in "Banana":
    print(x)

# String length
print(f"Length of `{a}` is: ", len(a))

# Check string
# To check if a certain phrase or character is present in a string, we can use the keyword `in`.
txt = "The best things in life are not free"
print("free" in txt)

# Check a certain phrase or character is present using `if` condition
if "free" in txt:
    print("'Free', is present")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.
print("expensive" not in txt)

# Check a certain phrase or character is NOT present using if condition
if "expensive" not in txt:
    print("'expensive', is not present")