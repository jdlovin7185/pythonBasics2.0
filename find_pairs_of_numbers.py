def find_pairs_of_numbers(num_list, n):
    length = len(num_list)
    match = 0
    i = 0
    j = 1
    while i < len(num_list):
        # print(num_list[i])
        # if j == length:
        #     break
        for j in range(len(num_list)):
            if j == length:
                break
            elif num_list[i] == num_list[j]:
                continue
            elif num_list[i] + num_list[j] == n:
                match += 1
                # print("The 2 numbers being added together ", num_list[i], " and ", num_list[j], " = ", num_list[i] + num_list[j])
            j += 1
        i += 1
    return int(match/2)


# num_list = [1, 2, 4,  5, 6]
num_list = [1, 2, 7, 4, 5, 6, 0, 3]
# num_list = [3, 4, 1, 8, 5, 9, 0, 6]
n = 6
print(find_pairs_of_numbers(num_list, n))
