def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle, right)

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# проверка что все является числами
def int_verify(str_in):
    try:
        #если число то возращаем int
        str_int = int(str_in)
        return str_int
    except ValueError:
        #тут не число
        print(f"Значение '{str_in}' невозможно преобразовать в целое число")
        return None
# запрашиваем у пользователя ввод последовательности цифр и преобразуем в список
str = input("Введите целые неповторяющиеся числа через пробел: ").split()
#создаем list с цифрами
num = list(map(int_verify, str))

set = list(set(num))
#преобразуем list в множество set
#и сравниваем их длины
if len(num) != len(set):
    print("Имеются повторяющиеся числа!")
    exit()
# ввод числа от пользователя
str = input("Введите целое число: ")
cfr = int_verify(str)
if not cfr:
    print("Число введено неверно!")
    exit()
# проверка присутствия введенной цифры в list num
if cfr not in num:
    print("Элемент не найден!")
    exit()
sort_num=merge_sort(num)
print (sort_num)
if min(sort_num) >= cfr or max(sort_num) < cfr:
    print('Число меньше либо равно минимальному или больше максимального')
else:
    print(binary_search(sort_num, cfr, 0, len(sort_num)))

