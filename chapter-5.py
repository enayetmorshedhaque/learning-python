# Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("--------------------")

# Create a variable inside a function, with the same name as the global variable

y = "awesome"

def myfunctwo():
  y = "fantastic"
  print("Python is " + y)

myfunctwo()

print("Python is " + y)

print("--------------------")

# If you use the global keyword, the variable belongs to the global scope

def myfuncthree():
  global z
  z = "fantastic"

myfuncthree()

print("Python is " + z)

print("--------------------")

# To change the value of a global variable inside a function, refer to the variable by using the global keyword

a = "awesome"

def myfuncfour():
  global a
  a = "fantastic"

myfuncfour()

print("Python is " + a)