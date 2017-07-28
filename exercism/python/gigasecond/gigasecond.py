from datetime import date, timedelta

def add_gigasecond(birthday):
    # gigasecond = timedelta(seconds = 10**9)
    # giga_age = birthday + gigasecond
    # return giga_age

    ##### refactor #####
    return birthday + timedelta(seconds = 1e9)

##### to solve with raw_input from user: #####
# def add_gigasecond(birthday):
    # year = input("Enter your birth year (YYYY): ")
    # month = input("Enter your birth month (MM): ")
    # day = input("Enter your birth date (DD): ")
    #
    # birthday = date(year, month, day)
    # gigasecond = timedelta(seconds = 10**9)
    # giga_age = birthday + gigasecond
    # return giga_age
