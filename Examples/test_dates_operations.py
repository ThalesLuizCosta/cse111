import datetime

# Import the functions from the other file
from dates_operations import get_current_date_time, create_date, create_time, calculate_time_difference, date_to_string, string_to_date, random_date, days_between_dates

# Test functions
def test_current_date_time():
    assert isinstance(get_current_date_time(), datetime.datetime), "get_current_date_time() should return a datetime object."

def test_create_date():
    assert create_date(2024, 2, 16) == datetime.date(2024, 2, 16), "create_date() should correctly create a date."

def test_create_time():
    assert create_time(12, 0, 0) == datetime.time(12, 0, 0), "create_time() should correctly create a time."

def test_time_difference():
    assert calculate_time_difference(datetime.time(12, 0, 0), datetime.time(14, 0, 0)) == datetime.timedelta(hours=2), "calculate_time_difference() should correctly calculate the difference between two times."

def test_date_to_string():
    assert date_to_string(datetime.date(2024, 2, 16)) == "2024-02-16", "date_to_string() should correctly convert a date to a string."

def test_string_to_date():
    assert string_to_date("2024-02-16") == datetime.date(2024, 2, 16), "string_to_date() should correctly parse a date from a string."

def test_random_date():
    random_date_generated = random_date()
    assert isinstance(random_date_generated, datetime.date), "random_date() should return a date object."
    assert datetime.date(1900, 1, 1) <= random_date_generated <= datetime.datetime.now().date(), "random_date() should return a date between 1900-01-01 and today."

def test_days_between_dates():
    assert days_between_dates(datetime.date(2024, 2, 16), datetime.date(2024, 2, 20)) == 4, "days_between_dates() should correctly calculate the number of days between two dates."

# Run the tests
test_current_date_time()
test_create_date()
test_create_time()
test_time_difference()
test_date_to_string()
test_string_to_date()
test_random_date()
test_days_between_dates()
