
# implicit type conversion
implicit_num = 1 + 1.0
print("Implicit adding -> ", implicit_num)

# explicit type conversion
explicit_num = 1 + int(1.0)
print("Explicit adding -> ", explicit_num)

# Lets throw a string in there
num_string = "10"

explicit_num_2 = 1 + int(num_string)
print("Explicit adding with a string -> ", explicit_num_2)

