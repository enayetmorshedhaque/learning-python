year = input("Enter a year: ")
year = int(year)

year_len = len(str(year))

if year_len != 4 and year < 0:
    print("Year cannot be negative")
elif year_len != 4:
    print("Year must have to be 4 digits")
elif year % 100 != 0 and year % 4 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0 and year % 4000 == 0:
    print("Leap Year")
else:
    print(year, "is not a Leap Year")