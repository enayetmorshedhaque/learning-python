# Python String Methods

txt = "python is FUN!"

# capitalize() Converts the first character to upper case
print(txt.capitalize())

# casefold() Converts string into lower case
print(txt.casefold())

# center() Returns a centered string
fruit = "banana"
print(fruit.center(20))

# count() Returns the number of times a specified value occurs in a string
print(txt.count("python"))

# encode() Returns an encoded version of the string
a = 'My name is Ståle'
print(a.encode())

# endswith() Returns true if the string ends with the specified value
print(txt.endswith("!"))

# expandtabs() Sets the tab size of the string
b = "H\te\tl\tl\to"
print(b.expandtabs(2))

# find() Searches the string for a specified value and returns the position of where it was found
print(txt.find("FUN"))

# format() Formats specified values in a string
a = "The price is {price:.2f} dollars!"
print(a.format(price = 49))

b = "My name is {name}, and my age is {age}."
print(b.format(name="John", age = 36))

# index() Searches the string for a specified value and returns the position of where it was found
print(txt.index("!"))

# isalnum() Returns True if all characters in the string are alphanumeric
a = "Alpha32"
print(a.isalnum())

# isalpha() Returns True if all characters in the string are in the alphabet
a = "alphaX"
print(a.isalpha())

# isascii() Returns True if all characters in the string are ascii characters
a = "company123"
print(a.isascii())

# isdecimal() Returns True if all characters in the string are decimals
a = "1234"
print(a.isdecimal())

# isdigit() Returns True if all characters in the string are digits
print(a.isdigit())

# isidentifier() Returns True if the string is an identifier
a = "demo"
b = "demo123"
c = "123demo"
d = "123 demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# islower() Returns True if all characters in the string are lower case
a = "python is fun"
print(a.islower())

# isnumeric() Returns True if all characters in the string are numeric
a = "123456"
print(a.isnumeric())

# isprintable() Returns True if all characters in the string are printable
a = "Hello! Are you #1?"
print(a.isprintable())

# isspace() Returns True if all characters in the string are whitespaces
a = "     "
print(a.isspace())

# istitle() Returns True if the string follows the rules of a title
a = "Hello! And Welcome To My World."
print(a.istitle()) # The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

# isupper() Returns True if all characters in the string are upper case
print(txt.isupper())

# join() Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
print(" # ".join(myTuple))

# ljust() Returns a left justified version of the string
print(fruit.ljust(20), "is my favorite fruit")

# lower() Converts a string into lower case
print(txt.lower())

# lstrip() Returns a left trim version of the string
x = "       banana       "
print(x.lstrip(), "is my favorite fruit")

# maketrans() Returns a translation table to be used in translations
x = "Hello Sam!"
myTable = x.maketrans("S", "P")
print(x.translate(myTable)) # Have to learn more

# partition() Returns a tuple where the string is parted into three parts
a = "I could eat all the bananas!"
print(a.partition("bananas"))

# replace() Returns a string where a specified value is replaced with a specified value
print(a.replace("bananas", "apples"))

# rfind() Searches the string for a specified value and returns the last position of where it was found
a = "Mi casa, su casa."
print(a.rfind("casa"))

# rindex() Searches the string for a specified value and returns the last position of where it was found
print(a.rindex("casa"))

# rjust() Returns a right justified version of the string
print(fruit.rjust(20), "is my favorite fruit")

# rpartition() Returns a tuple where the string is parted into three parts
a = "I could eat bananas all day, bananas are my favorite fruit"
print(a.rpartition("bananas")) # The rpartition() method searches for the last occurrence of a specified string

# rsplit() Splits the string at the specified separator, and returns a list
fruits = "apple, banana, cherry"
print(fruits.rsplit(", "))

# rstrip() Returns a right trim version of the string
x = "       banana       "
print(x.rstrip(), "is my favorite fruit")

# split() Splits the string at the specified separator, and returns a list
print(fruits.split())

# splitlines() Splits the string at line breaks and returns a list
x = "Thank you for the music\nWelcome to the jungle"
print(x.splitlines())

# startswith() Returns true if the string starts with the specified value
x = "Howdy, Admin!"
print(x.startswith("Howdy"))

# strip() Returns a trimmed version of the string
x = "       banana       "
print(x.strip(), "is my favorite fruit")

# swapcase() Swaps cases, lower case becomes upper case and vice versa
msg = "Hello My Name Is PETER"
print(msg.swapcase())

# title() Converts the first character of each word to upper case
print(msg.title())

# translate() Returns a translated string
# use a dictionary with ascii codes to replace 83 (S) with 80 (P)
myDict = {83: 80}
txt = "Hello Sam"
print(txt.translate(myDict))

# upper() Converts a string into upper case
a = "THIS IS A LOWERCASE SENTENCE"
print(a.lower())

# zfill() Fills the string with a specified number of 0 values at the beginning
txt = "50"
print(txt.zfill(10))
