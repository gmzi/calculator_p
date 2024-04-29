from helpers import calculate_price, is_rounded, weeks_to_days, maturity_date, days_span
from html_parser import create_grid, create_grid_maturity, balances_grid

class Compound_Interest:
    def calculate_and_parse(self, investment, interest_rate, years, compound_frequency):
        data = calculate_compounding(investment, interest_rate, years, compound_frequency)
        grid_1 = create_grid(data["labels_values"])
        grid_2 = balances_grid(data["balances"])
        return grid_1 + grid_2


def calculate_compounding(
    initial_investment,
    annual_interest_rate,
    years,
    compounding_periods_per_year ):

    r = annual_interest_rate / 100
    n = compounding_periods_per_year
    t = years

    # ending_value = initial_investment * ((1 + r / n) ** (n * t))

    balances = {}
    balance = initial_investment
    balances[0] = balance

    for year in range(1, years + 1):
        balance *= (1 + r / n) ** (n)
        balances[year] = balance

    ending_value = balance
    income = ending_value - initial_investment
    total_return = (income / initial_investment) * 100
    annualized_total_return = total_return / years

    formatted_income = "${:,.2f}".format(income)
    formatted_total_return = "{:,.2f}%".format(total_return)
    formatted_annualized_total_return = "{:,.2f}%".format(annualized_total_return)
    formatted_ending_value = "${:,.2f}".format(ending_value)
    formatted_balances = {}
    for year, balance in balances.items():
        formatted_balances[year] = "${:,.2f}".format(balance)
    
    labels_values = [
        ("Income: ", f"{formatted_income}"),
        ("Total Return: ", f"{formatted_total_return}"),
        ("Annualized total return: ", f"{formatted_annualized_total_return}"),
        ("Ending value: ", f"{formatted_ending_value}")
    ]

    return {
        "labels_values": labels_values, 
        "balances": formatted_balances
        }
