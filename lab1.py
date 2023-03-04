from matrix import *
import numpy as np

matr = np.matrix(G)
INF = 9999999
# selected буде true в іншому випадку false
selected = [0, 0, 0, 0, 0, 0, 0, 0]
# Встановити кількість ребер 0
no_edge = 0
# кількість ребер у мінімальному остовному дереві буде завжди менше ніж (V - 1), де V - кількість вершин у графі
# вибираємо 0-ту вершину та робимо її істинною
selected[0] = True
print("Алгоритм Прима")
print(f"Кількість вершин: {V}")
print(f"Матриця ваг: \n{matr}")
print("Ребро : Вага")
weight = 0  # Встановлюємо нульове значення для загальної ваги
while (no_edge < V - 1):
    # Для кожної вершини в множині S знаходимо всі суміжні вершини
    # Обчислюємо відстань від вершини, вибраної на кроці 1.
    # Якщо вершина вже є в наборі S, в такому разі відкидаємо її
    # Обираємо іншу вершину, найближчу до вибраної вершини на кроці 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    # Не в обраному і є ребро
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    weight += G[x][y]
    print(f" {str(x)}-{str(y)}  : {str(G[x][y])}")
    selected[y] = True
    no_edge += 1

print(f"Сумарна вага: {weight}")
