def get_precent(base_amount, percentage):
    return (base_amount / 100) * percentage


meal_cost = 10.25
tip_percent = 17
tax_percent = 5

tip_amount = get_precent(meal_cost, tip_percent)
tax_amount = get_precent(meal_cost, tax_percent)

amount_after_tax = meal_cost + tip_amount + tax_amount
print "The total meal cost is %d dollars." % round(amount_after_tax)
