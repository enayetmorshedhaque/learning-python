# String Concatenation
# To concatenate, or combine, two strings you can use the + operator
a = 'Hello'
b = 'World'
print(a + " " + b)

# F-Strings
age = 36
txt = f"My name is Shawon. I am {age} years old."
print(txt)

# Placeholders and Modifiers
# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 59
text = f'The price is {price:.2f} dollars'
print(text)

# A placeholder can contain Python code, like math operations
text = f'The price is {59 * 29} dollars'
print(text)