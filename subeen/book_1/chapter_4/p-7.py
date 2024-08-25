year = 2024

if year % 100 != 0 and year % 4 == 0:
    print("Leap Year")
elif year % 100 == 0 and year % 4000 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")