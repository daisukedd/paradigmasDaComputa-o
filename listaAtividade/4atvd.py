# bissexto -> 366 dias

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

user_input = int(input("Enter a year: "))
if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    next_leap_year = find_next_leap_year(user_input)
    print(f"{user_input} is not a leap year. The next leap year is {next_leap_year}.")