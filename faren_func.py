def cal_far(fahrenheit):
    cel = ((fahrenheit - 32) * (5 / 9))
    return cel


def cal_celsius(celsius):
    far = ((celsius * 9/5) + 32)
    return far


celly = 56
fahren = 78
print(cal_far(fahren))
print(cal_celsius(celly))
