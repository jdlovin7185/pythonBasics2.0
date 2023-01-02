def calculate_sum(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total: ", total)
        avg = total / num_values
        print("Average: ", avg)
    except ZeroDivisionError:
        print("Can't divide by Zero my guy")
    except TypeError:
        print("Wrong data type, give data type was", type(expenditure))


try:
    list_of_values = [100, 200, 300, 400, 500]
    num_values = len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occurred")
except:
    print("Some error occurred")
