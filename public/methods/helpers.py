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

def maturity_date(issue_date, days_to_maturity, reinvestments=0):
    issue_date_obj = datetime.strptime(issue_date, '%Y-%m-%d')

    total_days = days_to_maturity

    if reinvestments > 0:
       periods_to_count = reinvestments + 1
       total_days = days_to_maturity *  periods_to_count

    # Calculate maturity date
    maturity_date_obj = issue_date_obj + timedelta(days=total_days)

    # Convert maturity date back to string
    return maturity_date_obj.strftime('%m/%d/%Y')