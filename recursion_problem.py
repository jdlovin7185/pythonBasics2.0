def human_pyramid(no_of_people):
    if no_of_people == 1:
        return 1 * 50
    elif no_of_people == 0:
        return 0
    elif no_of_people < 0:
        return 0
    else:
        return no_of_people * 50 + human_pyramid(no_of_people - 2)


def find_maximum_people(max_weight):
    no_of_people = 0
    weight = 0

    print("Final weight -> ", weight)
    return no_of_people


# Provide different values for max_weight and test your program
max_people = find_maximum_people(1050)
print(max_people)
# print(human_pyramid(7))
