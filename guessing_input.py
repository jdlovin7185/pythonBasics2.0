ticket_status = "Confirmed"
luggage_weight = 32
weight_limit = 30  # Weight limits for the airline
extra_luggage_charge = 0
if ticket_status == "Confirmed":
    if 0 < luggage_weight <= weight_limit:
        print("Check-in cleared")
    elif luggage_weight <= (weight_limit + 10):
        extra_luggage_charge = 300 * (luggage_weight - weight_limit)
    else:
        extra_luggage_charge = 500 * (luggage_weight - weight_limit)
    if extra_luggage_charge > 0:
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")
