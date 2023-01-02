balance = 1000
amount = 300


def take_card():
    print("Take the card out of the ATM")


try:
    if balance >= int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")

except TypeError:
    print("Type error occurred")
except ValueError:
    print("Value error occurred")
except:
    print("Some error occurred")
finally:
    take_card()
