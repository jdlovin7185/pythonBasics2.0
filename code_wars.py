def better_than_average(class_points, your_points):
    length = len(class_points)
    sum_of_points = 0
    for i in class_points:
        sum_of_points += i
    average = sum_of_points/length
    return your_points > average

        # print(i)
    # pass


scores = [100, 40, 34, 57, 29, 72, 57, 88]
your_score = 80

better_than_average(scores, your_score)
