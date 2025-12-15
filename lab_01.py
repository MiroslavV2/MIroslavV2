def word(x, y):
    if x <= 12:
        if x % 10 == 1 and x != 11:
            x = 'час'
        elif x % 10 > 1 and x % 10 <5 and x != 12:
            x = 'часа'
        else:
            x = 'часов'
    elif x > 12:
        x = x - 12
        if x % 10 == 1 and x != 11:
            x = 'час'
        elif x % 10 > 1 and x % 10 <5:
            x = 'часа'
        else:
            x = 'часов'
    if y % 10 == 1 and y != 11:
        y = 'минута'
    elif y % 10 > 1 and y % 10 < 5 and y != 12 and y != 13 and y != 14:
        y = 'минуты'
    else:
        y = 'минут'
    return x, y

def Time_of_day(x):
    if 0 <= x < 6:
        x = 'ночи'
    elif 6 <= x < 12:
        x = 'утра'
    elif 12 <= x < 18:
        x = 'дня'
    else:
        x = 'вечера'
    return x

def Time(x, y):
    if x > 12:
        x = x - 12
        return x, y
    return x, y



input_list = input().split()
if len(input_list) != 2:
    print("Вводи 2 числа!")
else:
    minute_str = input_list[1]
    hour_str = input_list[0]
    c = 0

    if (hour_str.startswith('-') and int(hour_str) == 0) or (minute_str.startswith('-') and int(minute_str) == 0) :
        print('Не пиши отрицательный ноль @$&%%')
        c += 1
    else:
        if str(hour_str).isdigit() and str(minute_str).isdigit():
            hour, minute = int(hour_str), int(minute_str)
            if (not (0 <= hour < 24) or not (0 <= minute < 60)) and c == 0:
                print('Будь внимательней, такого времени нет.')
                c += 1
            elif hour == 0 and minute == 0 and c == 0:
                print('Полночь')
            elif hour == 12 and minute == 0 and c == 0:
                print('Полдень')
            else:
                Hour_word, Minute_word = word(hour, minute)
                Hour_time_day = Time_of_day(hour)
                Hour_time, Minute_time = Time(hour, minute)
                if minute == 0:
                    print(str(Hour_time) + ' ' + str(Hour_word) + ' ' + str(Hour_time_day) + ' ' + 'ровно')
                else:
                    print(str(Hour_time) + ' ' + str(Hour_word) + ' ' + str(Minute_time) + ' ' + str(Minute_word) + ' ' + str(Hour_time_day))