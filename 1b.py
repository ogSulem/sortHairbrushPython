''' Алгоритм сортировки расчёской '''

inp = input("Введите элементы массива через пробел: ").split() #просим пользователя ввести строку с элементами массива
msv = [int(i) for i in inp] #объявляем массив и заполняем его введёнными пользователям числами

def hairbrush(msv): # название функции
    step = len(msv) - 1 #объявляем переменную для шага сравнения, которая изначальна равна индексу последнего элемента массива
    swaps = 0 #объявляем переменную для счета перестановок
    while step >= 1: #запускаем цикл, который работает пока есть расстояние между элементами
        step = int(step) #округляем до целых шаг сравнения
        i = 0 #объявляем переменную для индекса первого элемента сравнения
        j = step #объявляем переменную для индекса второго элемента сравнения
        while j < len(msv): #запускаем цикл, который работает пока индекс второго элемента сравнения находится в пределах длины массива
            if msv[i] > msv[j]: #сравниваем элементы
                msv[i], msv[j] = msv[j], msv[i] #в случае выполнения условия меняем местами элементы
                swaps += 1 #увеличиваем количество перестановок
                print(f'{swaps} итерация: {" ".join([str(i) for i in msv])}') #выводим промежуточный массив
            i += 1 #увеличиваем индекс первого элемента сравнения
            j += 1 #увеличиваем индекс второго элемента сравнения
        step /= 1.247 #делим текущий шаг на оптимальное число, чтобы получить новый шаг сравнения

print(f'Исходный массив: {" ".join([str(i) for i in msv])}') #выводим исходный массив
rascheska(msv) #запускаем функцию сортировки, сортируем массив
print(f'Отсортированный массив: {" ".join([str(i) for i in msv])}') #выводим конечный массив