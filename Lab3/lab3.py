import numpy as np

N = 6

def read_matrix():
    matr = np.zeros((N, N), dtype=int)
    print("Матриця ваг:")
    try:
        with open("l3-1.txt", "r") as f:
            for i in range(N):
                matr[i] = [int(x) for x in f.readline().split()]
                print(*matr[i], sep="\t")
    except FileNotFoundError:
        print("Невірний формат файлу або його не знайдено.")
    return matr

def connectivity_matrix(matr):
    con_matr = np.zeros((N, N), dtype=int)
    print("\nМатриця зв'язностi:")
    for i in range(N):
        for j in range(N):
            if matr[i][j] > 0:
                con_matr[i][j] = 1
            else:
                con_matr[i][j] = matr[i][j]
            print(con_matr[i][j], end="\t")
        print()
    return con_matr

def hamilton(k, con_matr, c, path, v0):
    q1 = 0
    for v in range(N):
        if con_matr[v][path[k-1]] or con_matr[path[k-1]][v]:
            if k == N and v == v0:
                q1 = 1
            elif c[v] == -1:
                c[v] = k
                path[k] = v
                k1 = k + 1
                q1 = hamilton(k1, con_matr, c, path, v0)
                if not q1:
                    c[v] = -1
            else:
                continue
    return q1

def if_hamilton(con_matr, c, path, v0):
    print("\nГамiльтонiв цикл:")
    for j in range(N):
        c[j] = -1
    path[0] = v0
    c[v0] = v0

    if hamilton(1, con_matr, c, path, v0):
        pass
    else:
        print("Рішення відсутні")

    return path

def output(matr, path):
    weight = 0
    print(" Ребро : Вага ")
    for i in range(N):
        if i == N-1:
            print(f" {path[i]+1} - {path[0]+1} : {matr[path[i]][path[0]]}")
            weight += matr[path[i]][path[0]]
        else:
            print(f" {path[i]+1} - {path[i+1]+1} : {matr[path[i]][path[i+1]]}")
            weight += matr[path[i]][path[i+1]]
    print("\n Загальна вага шляху:", weight, "\n")

def main():
    matr = read_matrix()
    con_matr = connectivity_matrix(matr)

    c = np.zeros(N, dtype=int) - 1
    path = np.zeros(N, dtype=int)
    v0 = 0

    if_hamilton(con_matr, c, path, v0)
    output(matr, path)

if __name__ == '__main__':
    main()
