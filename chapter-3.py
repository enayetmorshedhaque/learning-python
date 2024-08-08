# Python has if...elif...else conditions too

# Take age as input from user
age = input("Enter Your Age: ");

if(float(age) < 0):
    print("Negative numbers are not allowed");
elif(float(age) >= 0 and float(age) < 10):
    print("You are infrant");
elif (float(age) > 10 and float(age) < 18):
    print("You are teenage");    
elif(float(age) >=18 and float(age) <= 65):
    print("You are adult")
else:
    print("You are oldage");

# float(age) explanation: age = input() makes the input string,
# as there is text inside the input() function.
# so, while checking age with 18, which is an integer, throws error.
# that's why we have typecasted the string to integer by using the float(age) typecaster.
