def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2000, 12, 31))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_days = [365,366,366,365]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	year = test_years[i]
	month = test_months[i]
	day = test_days[i]
	print(year, month, day, "-> ", end="")
	result = daysInMonth(year, month)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
