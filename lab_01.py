def time(x, y):
    # все падежи часа
    time_1 = ' час'
    time_2 = ' часа'
    time_3 = ' часов'
    # все интервалы дня
    day_time_1 = ' ночи'
    day_time_2 = ' утра'
    day_time_3 = ' дня'
    day_time_4 = ' вечера'
    #Все оканчания минуты
    minute_1 = ' минута'
    minute_2 = ' минуты'
    minute_3 = ' минут'
    if 0 <= x <= 12:
        if x == 1:
            if y == 0:
                return str(x) + time_1 + day_time_1 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_1 + ' ' + str(y) + minute_1 + day_time_1
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_1 + ' ' + str(y) + minute_2 + day_time_1
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_1 + ' ' + str(y) + minute_3 + day_time_1
        elif 1 < x < 5:
            if y == 0:
                return str(x) + time_2 + day_time_1 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_2 + ' ' + str(y) + minute_1 + day_time_1
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_2 + ' ' + str(y) + minute_2 + day_time_1
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_2 + ' ' + str(y) + minute_3 + day_time_1
        elif x == 5:
            if y == 0:
                return str(x) + time_3 + day_time_1 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_3 + ' ' + str(y) + minute_1 + day_time_1
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_3 + ' ' + str(y) + minute_2 + day_time_1
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_3 + ' ' + str(y) + minute_3 + day_time_1
        elif 5 < x < 12:
            if y == 0:
                return str(x) + time_3 + day_time_2 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_3 + ' ' + str(y) + minute_1 + day_time_2
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_3 + ' ' + str(y) + minute_2 + day_time_2
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_3 + ' ' + str(y) + minute_3 + day_time_2
        elif x == 12:
            if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                return str(x) + time_3 + ' ' + str(y) + minute_1 + day_time_3
            elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                return str(x) + time_3 + ' ' + str(y) + minute_2 + day_time_3
            elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                return str(x) + time_3 + ' ' + str(y) + minute_3 + day_time_3            
    elif 12 < x < 24:
        x = x - 12
        if x == 1:
            if y == 0:
                return str(x) + time_1 + day_time_3 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_1 + ' ' + str(y) + minute_1 + day_time_3
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_1 + ' ' + str(y) + minute_2 + day_time_3
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_1 + ' ' + str(y) + minute_3 + day_time_3
        elif 1 < x < 5:
            if y == 0:
                return str(x) + time_2 + day_time_3 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_2 + ' ' + str(y) + minute_1 + day_time_3
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_2 + ' ' + str(y) + minute_2 + day_time_3
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_2 + ' ' + str(y) + minute_3 + day_time_3
        elif x == 5:
            if y == 0:
                return str(x) + time_3 + day_time_3 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_3 + ' ' + str(y) + minute_1 + day_time_3
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_3 + ' ' + str(y) + minute_2 + day_time_3
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_3 + ' ' + str(y) + minute_3 + day_time_3
        elif 5 < x < 12:
            if y == 0:
                return str(x) + time_3 + day_time_4 + ' ровно'
            else:
                if y == 1 or y == 21 or y == 31 or y == 41 or y == 51:
                    return str(x) + time_3 + ' ' + str(y) + minute_1 + day_time_4
                elif 2 <= y <= 4 or 22 <= y <= 24 or 32 <= y <= 34 or 42 <= y <= 44 or 52 <= y <= 54:
                    return str(x) + time_3 + ' ' + str(y) + minute_2 + day_time_4
                elif 5 <= y <= 20 or 25 <= y <= 30 or 35 <= y <= 40 or 45 <= y <= 50 or 55 <= y <= 59:
                    return str(x) + time_3 + ' ' + str(y) + minute_3 + day_time_4


print("Введите время: Сначало часы, потом через пробел введите минуты ЦИФРАМИ!!!")

a_list = input().split()
if len(a_list) != 2:
    print("Вводи 2 числа!")
else:
    b_str = a_list[1]
    a_str = a_list[0]
    c = 0

    if (a_str.startswith('-') and int(a_str) == 0) or (b_str.startswith('-') and int(b_str) == 0) :
        print('Не пиши отрицательный ноль @$&%%')
        c += 1
    else:
        if str(a_str).isdigit() and str(b_str).isdigit():
            a, b = int(a_str), int(b_str)
            if (not (0 <= a < 24) or not (0 <= b < 60)) and c == 0:
                print('Будь внимательней, такого времени нет.')
                c += 1
            elif a == 0 and b == 0 and c == 0:
                print('Полночь')
            elif a == 12 and b == 0 and c == 0:
                print('Полдень')
            elif c == 0:
                print(time(a, b))
        else:
            c = 10
            print("Пиши цифрами @@#$%!!!")    