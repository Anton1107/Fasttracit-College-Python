# https://en.wikipedia.org/wiki/Leap_year
year = int(input(" Enter the year: "))
month = int(input("Enter the month - int: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
	print(f"{year} is a leap year")
	if month == 1 or month == 3 or month == 5 or month == 7 \
		or month == 8 or month == 10 or month == 12:
		print("There are 31 days in this month ")
	elif month == 4 or month == 6 or month == 9 or month == 11:
		print("There are 30 days in this month ")
	elif month == 2:
		print("There are 29 days in this month ")
	else:
		print("Invalid month ")
elif year % 4 != 0 or year % 100 != 0 or year % 400 != 0:
	print(f"{year} is not a leap year")
	if month == 1 or month == 3 or month == 5 \
		or month == 7 or month == 8 or month == 10 or month == 12:
		print("There are 31 days in this month")
	elif month == 4 or month == 6 or month == 9 or month == 11:
		print("There are 30 days in this month ")
	elif month == 2:
		print("There are 28 days in this month ")
	else:
		print("Invalid month ")
else:
	print(" Invalid Year ")


if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print(f"{year} is a leap year")
		else:
			print(f"{year} is not a leap year")
	else:
		print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")
