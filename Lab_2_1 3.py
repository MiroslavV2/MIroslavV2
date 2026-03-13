import random

def sort_vibor(input_massiv):
    len_mass = len(input_massiv)
    count_comparison = 0
    count_permutation = 0
    for i in range(len_mass):
        min_indx = i
        for j in range(i + 1, len_mass):
            if input_massiv[j] < input_massiv[min_indx]:
                min_indx = j
            count_comparison += 1
        input_massiv[i], input_massiv[min_indx] = input_massiv[min_indx], input_massiv[i]
        count_permutation += 1

    return "Выбором", count_comparison, count_permutation, input_massiv

def sort_bubble(input_massiv):
    len_mass = len(input_massiv)
    count_comparison = 0
    count_permutation = 0
    cnt = 0
    for i in range(len_mass - 1):
        for j in range(len_mass - i - 1):
            count_comparison += 1
            if input_massiv[j] > input_massiv[j + 1]:
                input_massiv[j], input_massiv[j + 1] = input_massiv[j + 1], input_massiv[j]
                cnt += 1
        if cnt == 0:
            break
        count_permutation, cnt = count_permutation + cnt, 0
    return "Пузырьком", count_comparison, count_permutation, input_massiv

def sort_rekyrs(input_massiv):
    if len(input_massiv) <= 1:
        return "Рекурсией", 0, 0, input_massiv

    sred_zn = input_massiv[len(input_massiv) // 2]
    left = []
    middle = []
    right = []
    comparison = 0

    for i in input_massiv:
        comparison += 1
        if i < sred_zn:
            left.append(i)
        elif i == sred_zn:
            middle.append(i)
        else:
            right.append(i)

    _, comp_left, perm_left, sorted_left = sort_rekyrs(left)
    _, comp_right, perm_right, sorted_right = sort_rekyrs(right)

    total_comparison = comparison + comp_left + comp_right
    total_permutation = perm_left + perm_right

    return "Рекурсией", total_comparison, total_permutation, sorted_left + middle + sorted_right



def proverka_massiva(s):
    if not s or s.isspace():
        return False
    parts = s.split()
    for part in parts:
        if not (part.replace("-", "", 1).isdigit() and part.count("-") <= 1):
            return False
    return True



def proverka_indeksa(s, end):
    if not s or s.isspace():
        return False
    s = s.strip()
    if not (s.replace("-", "", 1).isdigit() and s.count("-") <= 1):
        return False
    num = int(s)
    return 0 <= num <= end


def vivod(lst):
    lst_s, lst_b, lst_m = lst.copy(), lst.copy(), lst.copy()
    srt_s, srt_b, srt_m = sort_vibor(lst_s), sort_bubble(lst_b), sort_rekyrs(lst_m)
    print("Сортировка выбором:", (srt_s[3]))
    print("Сортировка пузырьком:", (srt_b[3]))
    print("Сортировка рекурсией:", (srt_m[3]))
    lst_form = ["Сортировка", "Количество сравнений", "Количество перестановок"]
    otv = [lst_form, srt_s, srt_b, srt_m]
    print()
    for i in range(4):
        for j in range(3):
            print(str(otv[i][j]).ljust(27), end="")
        print()

def main():
    print("Выберите режим работы:")
    print("1: Демонстративный")
    print("2: Интерактивный")
    Prov = False
    while not Prov:
        a = input()
        if a != '1' and a != '2':
            print("Вводи 1 или 2")
        else:
            Prov = True
    if a == '1':
        massiv = [random.randint(0, 999) for _ in range(100)]
        print("Заданный массив")
        print(*massiv)
        print(vivod(massiv))
    elif a == "2":
        massiv = list()
        number = 0
        while number != 9:
            print()
            print("Выберите действие:")
            print("1: Ввести массив или ввести заново")
            print("2: Вывести массив")
            print("3: Изменить массив")
            print("4: Сортировка выбором")
            print("5: Сортировка пузырьком")
            print("6: Сортировка рекурсией")
            print("7: Вывод таблицы сравнения сортировок")
            print("8: @#%$")
            print("9: Выход")
            number = input()
            while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7" and number != "8" and number != "9":
                print("Вводить только цыфры не равные 0(Для не умных:1, 2, 3, 4, 5, 6, 7, 8, 9)")
                number = input()

            if number == "1":
                print("Введите числа для массива на строке, через пробел:")
                massiv = input()
                while massiv == 0:
                    print("Введите числа для массива")
                    massiv = input()
                massiv = list(map(int, massiv.split()))
                print("Вы ввели новый массив")
            elif number == "2":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    print("Используемый массив")
                    print(*massiv)
            elif number == "3":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    print("Выберите действие:")
                    print("1 - Изменить элемент массива")
                    print("2 - Изменить часть массива")
                    izmen = input()
                    while izmen != '1' and izmen != '2':
                        print("Вводи только 1 или 2")
                        izmen = input()

                    if izmen == "1":
                        print("Введите номер элемента, начиная с 0 и заканчивая " + str((len(massiv)) - 1) + ":")
                        ind = input()
                        end = len(massiv) - 1
                        while not proverka_indeksa(ind, end):
                            print("Введите номер элемента, начиная с 0 и заканчивая " + str((len(massiv)) - 1) + ":")
                            ind = input()
                        print("Введите элемент(целое число):")
                        ch = input()
                        while not (ch.replace("-", "", 1).isdigit() and ch.count("-") <= 1):
                            print("Введите элемент(целое число):")
                            ch = input()
                        massiv[int(ind)] = int(ch)
                        print("Вы успешно изменили массив!")

                    elif izmen == "2":
                        end = len(massiv) - 1
                        print("Введите номер начального элемента (от 0 до " + str(end) + "):")
                        first = input()
                        while not proverka_indeksa(first, end):
                            print("Введите номер начального элемента (от 0 до " + str(end) + "):")
                            first = input()
                        first = int(first)
                        print("Введите номер конечного элемента (от " + str(first) + " до " + str(end) + "):")
                        last = input()
                        while not proverka_indeksa(last, end) or int(last) < first:
                            if int(last) < first:
                                print("Конечный элемент должен быть больше или равен начальному!")
                            print("Введите номер конечного элемента (от " + str(first) + " до " + str(end) + "):")
                            last = input()
                        last = int(last)
                        print("Введите новую часть массива (" + str(
                            last - first + 1) + " целых чисел на одной строке, через пробел):")
                        part = input()
                        valid = False
                        while not valid:
                            if not proverka_massiva(part):
                                print("Введите целые числа для изменения части массива на одной строке, через пробел:")
                                part = input()
                                continue
                            parts = part.split()
                            if len(parts) != (last - first + 1):
                                print("Нужно ввести ровно " + str(last - first + 1) + " чисел!")
                                print("Введите целые числа для изменения части массива на одной строке, через пробел:")
                                part = input()
                                continue
                            valid = True
                        part = list(map(int, part.split()))
                        massiv[first:(last + 1)] = part
                        print("Вы успешно изменили массив!")

            elif number == "4":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    massiv_copy_vibor = massiv.copy()
                    massiv_sort_vibor = sort_vibor(massiv_copy_vibor)
                    print("После сортировки выбором:", *(massiv_sort_vibor[3]))
                    print("Количество сравнений:", massiv_sort_vibor[1])
                    print("Количество перестановок:", massiv_sort_vibor[2])
            elif number == "5":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    massiv_copy_bubble = massiv.copy()
                    massiv_sort_bubble = sort_bubble(massiv_copy_bubble)
                    print("После сортировки пузырьком:", *(massiv_sort_bubble[3]))
                    print("Количество сравнений:", massiv_sort_bubble[1])
                    print("Количество перестановок:", massiv_sort_bubble[2])
            elif number == "6":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    massiv_copy_rekyrs = massiv.copy()
                    _, comp_massiv_sort_rekyrs, perm_massiv_sort_rekyrs, massiv_sort_rekyrs = sort_rekyrs(massiv_copy_rekyrs)
                    print("После сортировки рекурсией:", *massiv_sort_rekyrs)
                    print("Количество сравнений:", comp_massiv_sort_rekyrs)
                    print("Количество перестановок:", perm_massiv_sort_rekyrs)

            elif number == "7":
                if len(massiv) == 0:
                    print("Нет массива")
                else:
                    vivod(massiv)
            elif number == "8":
                print("Чего смотришь? Думал что тут что-то интересное? " + "\u2721\uFE0F")

if __name__ == "__main__":
    main()
