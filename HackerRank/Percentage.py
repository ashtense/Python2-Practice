def add_percentage(base_amount, percentage):
    return base_amount + (base_amount / 100) * percentage

meal_cost = 10.25
tip_percent = 17
tax_percent = 5

amount_after_tax = add_percentage(add_percentage(meal_cost, tip_percent), tax_percent)

print amount_after_tax
print round(amount_after_tax,0)
print int(round(amount_after_tax))
