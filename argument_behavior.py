def add_to_list(the_list):
    print("This is the list before being appended\n", the_list)
    the_list.append(5)
    print("This is the list inside the function\n", the_list)


this_list = [1, 2, 3, 4]

add_to_list(this_list)
# list are mutable, this is why you can change it 
print("This is the list outside of function after it is called\n", this_list)
