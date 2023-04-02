import itertools
import numpy as np


def check_isom(gr1, gr2):
    if len(gr1) != len(gr2) or len(gr1[0]) != len(gr2[0]):
        return False

    n = len(gr1)

    vertices = list(range(n))

    visited = set()

    # перебирання всіх можливих перестановок вершин
    for perm in itertools.permutations(vertices):
        if perm not in visited:
            visited.add(perm)  # додання нової перестановки до відвіданого набору

            # перевірка, чи є поточна перестановка дійсним ізоморфізмом
            mapping = {}
            is_valid = True
            for j in range(n):
                for k in range(n):
                    if gr1[j][k] != gr2[perm[j]][perm[k]]:
                        is_valid = False
                        break
                if not is_valid:
                    break
                mapping.setdefault(gr1[j][j], gr2[perm[j]][perm[j]])

                if mapping[gr1[j][j]] != gr2[perm[j]][perm[j]]:
                    is_valid = False
                    break
            if is_valid:
                return True

    return False  # графи не ізоморфні


# Головна функція для зчитування файлів і виводу результату
def main():
    with open('matr1.txt', 'r') as f:
        n = int(f.readline())
        gr1 = [[int(x) for x in f.readline().split()] for i in range(n)]
        matr1 = np.matrix(gr1)
        print(f"Матриця суміжності першого графа: \n{matr1}")

    with open('matr2.txt', 'r') as f:
        n = int(f.readline())
        gr2 = [[int(x) for x in f.readline().split()] for i in range(n)]
        matr2 = np.matrix(gr2)
        print(f"\nМатриця суміжності другого графа: \n{matr2}")

    # Перевірка чи графи ізоморфні
    if check_isom(gr1, gr2):
        print("\nГрафи ізоморфні.")
    else:
        print("\nГрафи не ізоморфні.")


if __name__ == "__main__":
    main()
