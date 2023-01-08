""" Данная программа сравнивает пока что только две строки!!
    В программе бесконечный цикл, для выхода напишите "-1" )
    Выполнил: Климов Иван
"""

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
    return (m-d[m][n])/m

while 1>0:
    print("Введите первую строчку: ")
    a = input()  # ввод  строчки
    if a == "-1":
        break
    print("Введите вторую строчку: ")
    b = input()  # ввод  строчки

    # в будущем тут будет чтение файла как и было в ТЗ)

    print("совпадение строк:")
    print('%.2f' % levenshtein_distance(a, b))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~`")


#f = open(f"/Users/ivanklimov/Downloads/plagiat/{a}") #читайем нужные файлы при помощи f-строки
#w = open(f"/Users/ivanklimov/Downloads/plagiat/{b}")