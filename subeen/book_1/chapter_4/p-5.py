saarc = ['Bangladesh', 'Afghanistan', 'Bhutan', 'Nepal', 'India', 'Pakistan', 'Sri Lanka']

country = input("Enter the name of the country: ")

if country.title() in saarc:
    print(country.title(), " is a member of saarc")
else:
    print(country.title(), " is not a member of saarc")

print("program terminated")