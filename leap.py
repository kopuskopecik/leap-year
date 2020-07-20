# finding leap year
year = input("Please enter four digit numbers as a year: ")
while not year.isdigit() or len(year) != 4:
    year = input("Please enter a positive an integer exclude 1 and 0")
if (int(year) / 100) % 4 == 0:
    print(year, "is leap year")
else:
    print(year, "is not a leap year")