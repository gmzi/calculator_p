from helpers import calculate_price, is_rounded, weeks_to_days, maturity_date, days_span
from html_parser import create_grid, create_grid_maturity, footer_html

class Response:
  def __init__(self, content, status, code):
    self.content = content
    self.status = status
    self.code = code
  
class Treasury:
  def calculate_and_parse(self, investment, high_rate, weeks, issue_date, reinvestments):
    days = weeks_to_days(weeks)
    price = calculate_price(high_rate, days)
    labels_values = calculate(investment, price, weeks, issue_date, reinvestments)
    html_markup = create_grid(labels_values) + footer_html()
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
    html_markup = create_grid_maturity(labels_values)
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
        maturity = maturity_date(issue_date, days)
        span = days_span(issue_date, maturity)
    else:
        maturity = "-*-"
        span = "-*-"
    
    f_price = "${:,.6f}".format(price)
    f_discount = "${:,.6f}".format(discount)
    f_total_interest = "${:,.2f}".format(total_interest_rounded)
    f_months_to_maturity = "{:,.2f}".format(months_to_maturity)
    f_investment = "${:,.2f}".format(investment)
    f_bills_I_can_buy_with_my_budget = "{:,}".format(int(bills_I_can_buy_with_my_budget))
    f_amount_to_be_debited = "${:,.2f}".format(amount_to_be_debited)
    f_day_interest = "${:,.6f}".format(day_interest)
    f_monthly_interest = "{:,.3f}%".format(monthly_interest)
    f_total_interest_monthly = "{:,.3f}%".format(total_interest_monthly)
    f_day_interest_by_year = "{:,.3f}%".format(day_interest_by_year)
        
    labels_values = [
        ("Price per 100:", f"{f_price}"),
        ("Discount:", f"{f_discount}"),
        ("Total interest if YTM[*]", f"{f_total_interest}"),
        ("Maturity date:", maturity),
        ("Months to maturity: ", f_months_to_maturity),
        ("Budget:", f"{f_investment}"),
        ("Bills Bought:", f"{f_bills_I_can_buy_with_my_budget}"),
        ("Amount to be Debited:", f"{f_amount_to_be_debited}"),
        ("Daily Interest annualized:", f"{f_day_interest}"),
        ("Monthly Interest:", f"{f_monthly_interest}"),
        ("Monthly Interest Summed Up:", f"{f_total_interest_monthly}"),
        ("Annualized interest[**]:", f"{f_day_interest_by_year} (-mind to divide it monthly-)"),
        ("Days:", str(days)),
        ("Days span:", str(span))
    ]

    return labels_values