# lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    service_tax = 0.07
    discount = .1
    adult_ticket = 37550
    child_ticket = adult_ticket * .3333333333
    sub_total = ((adult_ticket * no_of_adults) + (child_ticket * no_of_children))
    print("Sub total before tax -> ", sub_total)
    tax = sub_total * service_tax
    print("Tax at 7% -> ", tax)
    sub_total_after_tax = sub_total + tax
    print("Sub total after tax", sub_total_after_tax)
    discount_off = sub_total_after_tax * discount
    print("Holiday special discount off -> ", discount_off)
    total_ticket_cost += sub_total_after_tax - discount_off
    print("Your total is -> ", total_ticket_cost)
    print("Pay up, pay up, PAY UP")

    # Write your logic here

    return total_ticket_cost


# Provide different values for no_of_adults, no_of_children and test your program

calculate_total_ticket_cost(5, 2)

# child_ticket = 37550 * .333333
# print(child_ticket)