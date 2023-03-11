from matrix import *
import numpy as np

matr = np.matrix(graph)
print(f"Матриця ваг: \n{matr}\n")


def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i, l):
            w_sum += graph[i][j]
    return w_sum

print(f"Загальна вага маршруту листоноші без дублювання шляхів: {sum_edges(graph)}")

#Розв'язок алгоритмом Дейкстри
def dijkstra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if (i == source):
            shortest[source] = 0  # граф вигляду [source][source]
        else:
            if (graph[source][i] == 0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if (shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i

    if (source == dest):
        return 0
    # Початок алгоритму Дейкстра
    selected.append(ind)
    while (ind != dest):
        for i in range(l):
            if i not in selected:
                if (graph[ind][i] != 0):
                    # Перевірка чи дистанція мусить бути оновлена
                    if ((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000

        for j in range(l):
            if j not in selected:
                if (shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]


# Знаходження непарних вершин по індексам

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != 0):
                degrees[i] += 1

    print(f"\nК-сть степенів для кожної вершини по індексам: {degrees}")
    odds = [i for i in range(len(degrees)) if degrees[i] % 2 != 0]
    print('Непарні вершини по індексам:', odds)
    return odds


# Функція що генерує унікальні пари по індексам
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds) - 1):
        pairs.append([])
        for j in range(i + 1, len(odds)):
            pairs[i].append([odds[i], odds[j]])

    return pairs


# Кінцевий вигляд скомпільованої функції
def Postman_task(graph):
    odds = get_odd(graph)
    if (len(odds) == 0):
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs) + 1) // 2

    pairings_sum = []

    def get_pairs(pairs, done=[], final=[]):

        if (pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])

            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if (i[1] not in val):
                    f.append(i)
                else:
                    continue

                if (len(f) == l):
                    pairings_sum.append(f)
                    return
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:], val, f)

        else:
            get_pairs(pairs[1:], done, final)

    get_pairs(pairs)
    min_sums = []

    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            s += dijkstra(graph, i[j][0], i[j][1])
        min_sums.append(s)

    added_dis = min(min_sums)
    postman_dis = added_dis + sum_edges(graph)
    return postman_dis


print('\nЗагальна вага маршруту листоноші з дубльованими шляхами становить:', Postman_task(graph))
