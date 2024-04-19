
def second_to_hour_minute_second(second):
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    return hour, minute, second


def korean_hour_minute_second(second):
    hour, minute, second = second_to_hour_minute_second(second)
    string = ''
    if second != 0:
        string += str(second)+'초'
    if minute != 0:
        string = str(minute)+'분'+string
    if hour != 0:
        string = str(hour)+'시간'+string
    return string