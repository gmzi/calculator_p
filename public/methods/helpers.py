import time
from datetime import datetime, timedelta


def calculate_price(high_rate, days):
   face_value = 100
   high_rate_percentage = high_rate / 100
   price = face_value * ( 1 - (high_rate_percentage * days) / 360)
   rounded_price = round(price, 6)
   return rounded_price

def reverse_and_normalize(string):
    # Replace the parentheses with negative symbol
    modified_str = string.replace("(", "-").replace(")", "")
    # Split the string into individual elements
    elements = modified_str.split()
    # Convert each element to a float
    reversed_float_numbers = [float(element) for element in elements][::-1]
    return reversed_float_numbers


def is_rounded(number):
    # Check if the number is a float
    if not isinstance(number, float):
        return False
    return abs(number - int(number)) < 1e-6


def weeks_to_days(weeks):
    if weeks == 4:
        return 28
    elif weeks == 8:
        return 56
    elif weeks == 13:
        return 91
    elif weeks == 17:
        return 119
    elif weeks == 26:
        return 182
    elif weeks == 52:
        return 364
    else:
        return 0

def maturity_date(issue_date, days, reinvestments=0):
    issue_date_parts = issue_date.split('-')
    year = int(issue_date_parts[0])
    month = int(issue_date_parts[1])
    day = int(issue_date_parts[2])

    issue_timestamp = time.mktime((year, month, day, 0, 0, 0, 0, 0, -1))

    total_days = days

    if reinvestments > 0:
        periods_to_count = reinvestments + 1
        total_days *= periods_to_count

    maturity_timestamp = issue_timestamp + total_days * 24 * 60 * 60

    # Format the maturity date to MM-DD-YYYY
    formatted_maturity_date = time.strftime(
        "%m/%d/%Y", time.localtime(maturity_timestamp))

    return formatted_maturity_date

def format_currency(amount, decimal_places):
    integer_part, decimal_part = str(amount).split('.')
    integer_formatted = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            integer_formatted = ',' + integer_formatted
        integer_formatted = digit + integer_formatted

    decimal_part = decimal_part[:decimal_places]
    return '${}.{}'.format(integer_formatted, decimal_part)


def format_percentage(amount, decimal_places):
    integer_part, decimal_part = str(amount).split('.')
    integer_formatted = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            integer_formatted = ',' + integer_formatted
        integer_formatted = digit + integer_formatted
    decimal_part = decimal_part[:decimal_places]
    return '{}.{}%'.format(integer_formatted, decimal_part)


def format_int(amount):
    integer_part = str(amount)
    integer_formatted = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            integer_formatted = ',' + integer_formatted
        integer_formatted = digit + integer_formatted
    return '{}'.format(integer_formatted)
