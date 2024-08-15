# Python - Slicing Strings

a = "Hello, World!"
print(a[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character
print(a[:5])

# Slice To the End
# By leaving out the start index, the range will start at the first character
print(a[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
print(a[-5:-2])

# In Python, the last index in a slice (whether using positive or negative indexing) is always excluded from the result.