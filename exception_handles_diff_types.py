def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total / num_values
        print("Average - ", avg)
    except ZeroDivisionError:
        print("You can't divide by zero bub")
    except TypeError:
        print("Wrong data type, must be an int")
    except:
        print("Something bad happened that isn't caught")


# will throw a type error
# list_of_values = [100, 200, 300, "400", 500]

list_of_values = [100, 200, 300, 400, 500]

# Will throw a ZeroDivision error
num_values = 0

calculate_expenditure(list_of_values)
