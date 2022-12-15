def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func is None:
        the_sum = 0
        for i in list_of_num:
            the_sum += i
        return the_sum
    elif filter_func is even:
        return even(list_of_num)
    elif filter_func is odd:
        return odd(list_of_num)


def even(data):
    even_sum = 0
    for i in data:
        if i % 2 == 0:
            # print(i)
            even_sum += i
    return even_sum


def odd(data):
    odd_sum = 0
    for i in data:
        if i % 2 != 0:
            # print(i)
            odd_sum += i
    return odd_sum


sample_data = range(1, 11)

# print(even(sample_data))
print(sum_of_numbers(sample_data, odd))

