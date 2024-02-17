import datetime
import random

# Functions using datetime module
def get_current_date_time():
    return datetime.datetime.now()

def create_date(year, month, day):
    return datetime.date(year, month, day)

def create_time(hour, minute, second):
    return datetime.time(hour, minute, second)

def calculate_time_difference(time1, time2):
    return datetime.datetime.combine(datetime.date.today(), time2) - datetime.datetime.combine(datetime.date.today(), time1)

def date_to_string(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def string_to_date(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

def random_date(start_year=1900, end_year=datetime.datetime.now().year):
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)

    return start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

# Print the results of the functions
print("Current date and time:", get_current_date_time())
print("Created date:", create_date(2024, 2, 16))
print("Created time:", create_time(12, 0, 0))
print("Time difference:", calculate_time_difference(datetime.time(12, 0, 0), datetime.time(14, 0, 0)))
print("Date to string:", date_to_string(datetime.date(2024, 2, 16)))
print("String to date:", string_to_date("2024-02-16"))

# Generate a random date and calculate the number of days between it and a given date
random_date_result = random_date()
print("Random date:", random_date_result)
print("Number of days between the random date and 2024-02-16:", days_between_dates(random_date_result, datetime.date(2024, 2, 16)))
