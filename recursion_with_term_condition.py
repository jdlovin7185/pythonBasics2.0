def human_tower(no_of_people):
    # this is here so that the function isn't calling itself infinitely
    if no_of_people == 1:
        return 1 * 50
    else:
        return no_of_people * 50 + human_tower(no_of_people - 2)


print("Total weight of human tower -> ", human_tower(15))
