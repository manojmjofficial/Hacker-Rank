#Program to print the total of meal cost with tip and tax percent

def solve(meal_cost, tip_percent, tax_percent):
    tip= meal_cost*(tip_percent/100)
    tax= meal_cost*(tax_percent/100)
    total = meal_cost + tip + tax
    print(round(total))

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)
