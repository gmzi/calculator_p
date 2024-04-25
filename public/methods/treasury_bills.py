from helpers import calculate_price, is_rounded, weeks_to_days, maturity_date, format_currency, format_percentage, format_int
from html_parser import create_table, create_table_maturity

class Response:
  def __init__(self, content, status, code):
    self.content = content
    self.status = status
    self.code = code
  
class Treasury:
  """A class to greet people."""
  def hello(self, name):
    return Response(f"Hello, {name}!", "success", 200)
  
  def format_input(self, num, decimal_places):
     formatted_input = format_currency(num, decimal_places)
     return formatted_input
  
  def calculate_and_parse(self, investment, high_rate, weeks, issue_date, reinvestments):
    days = weeks_to_days(weeks)
    price = calculate_price(high_rate, days)
    labels_values = calculate(investment, price, weeks, issue_date, reinvestments)
    html_markup = create_table(labels_values)
    return html_markup
  
  def maturity(self, weeks, issue_date, reinvestments):
    days = weeks_to_days(weeks)
    months_to_maturity = round(days / 30, 2)
    maturity_date_w_reinvestments = maturity_date(issue_date, days, reinvestments)
    labels_values = [
        ("Maturity date:", maturity_date_w_reinvestments),
        ("Months to maturity: ", "{:,.2f}".format(months_to_maturity)),
        ("Days:", str(days))
    ]
    html_markup = create_table_maturity(labels_values)
    return html_markup

def calculate(investment, price, weeks, issue_date=False, reinvestments=0):
    # these are the calculations for one period, don't touch them:
    discount_raw = 100 - price
    discount = round(discount_raw, 7)
    days = weeks_to_days(weeks)
    day_interest = discount / days
    bills_I_can_buy_with_my_budget = investment / 100
    amount_to_be_debited = round(bills_I_can_buy_with_my_budget * price, 2)

    if not is_rounded(bills_I_can_buy_with_my_budget):
        labels_values = [
          ("invalid amount: ", "please remember investment must be divisible by 100"),
        ]
        return labels_values
    
    total_interest =  bills_I_can_buy_with_my_budget * day_interest * days

    total_interest_rounded = round(total_interest, 2)
    day_interest_by_year = round(day_interest * 360, 3)
    # --------------------------------------------------------------
    months_to_maturity = round(days / 30, 2)
    monthly_interest = discount / months_to_maturity
    total_interest_monthly = months_to_maturity * monthly_interest

    if issue_date:
        maturity_initial = maturity_date(issue_date, days)
        maturity_with_reinvestments = maturity_date(issue_date, days, reinvestments)
    else:
        maturity_initial = "-*-"
        maturity_with_reinvestments = "-*-"
    
    f_price = format_currency(price, 6)
    f_discount = format_currency(discount, 6)
    f_total_interest = format_currency(total_interest_rounded, 2)
    f_months_to_maturity = "{:,.2f}".format(months_to_maturity)
    f_investment = format_currency(investment, 2)
    f_bills_I_can_buy_with_my_budget = format_int(int(bills_I_can_buy_with_my_budget))
    f_amount_to_be_debited = format_currency(amount_to_be_debited, 2)
    f_day_interest = format_currency(day_interest, 6)
    f_monthly_interest = format_percentage(monthly_interest, 3)
    f_total_interest_monthly = format_percentage(total_interest_monthly, 3)
    f_day_interest_by_year = format_percentage(day_interest_by_year, 3)
        
    labels_values = [
        ("Price per 100:", f"{f_price}"),
        ("Discount:", f"{f_discount}"),
        ("Total interest if YTM[*]", f"{f_total_interest}"),
        ("Maturity date:", maturity_initial),
        (f"Maturity date with {reinvestments} reinvestments: ", maturity_with_reinvestments ),
        ("Months to maturity: ", f_months_to_maturity),
        ("Budget:", f"{f_investment}"),
        ("Bills Bought:", f"{f_bills_I_can_buy_with_my_budget}"),
        ("Amount to be Debited:", f"{f_amount_to_be_debited}"),
        ("Daily Interest annualized:", f"{f_day_interest}"),
        ("Monthly Interest:", f"{f_monthly_interest}"),
        ("Monthly Interest Summed Up:", f"{f_total_interest_monthly}"),
        ("Annualized interest[**]:", f"{f_day_interest_by_year} (-mind to divide it monthly-)"),
        ("Days:", str(days))
    ]

    return labels_values