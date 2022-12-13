def change_num(num):
    print("The change inside the func before assignment\n", num)
    num += 10
    print("The change inside the func after assignment\n", num)


the_num = 15
change_num(the_num)

print("The change of the num outside of the func\n", the_num)

# it does not change because ints are immutable, this will also apply to float, strings, tuples, booleans
