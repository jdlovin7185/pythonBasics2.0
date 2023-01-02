# calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print(total)
    #     the except is very broad but will catch everything, the IDE will tell you to use a precise except clause
    except:
        print("Some error occured")
    print("Returning back from function.")


list_of_values = [100, 200, 300, "400", 500]
calculate_expenditure(list_of_values)
