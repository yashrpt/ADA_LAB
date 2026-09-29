
from typing import List

def strassen_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not compatible")

    n = max(len(A), len(A[0]), len(B), len(B[0]))
    size = 1

    while size < n:
        size *= 2

    def pad(M, size):
        return [
            row + [0] * (size - len(row))
            for row in M
        ] + [[0] * size for _ in range(size - len(M))]

    A = pad(A, size)
    B = pad(B, size)

    def add(X, Y):
        return [
            [X[i][j] + Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    def subtract(X, Y):
        return [
            [X[i][j] - Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    def strassen(X, Y):
        n = len(X)

        if n == 1:
            return [[X[0][0] * Y[0][0]]]

        mid = n // 2

        A11 = [row[:mid] for row in X[:mid]]
        A12 = [row[mid:] for row in X[:mid]]
        A21 = [row[:mid] for row in X[mid:]]
        A22 = [row[mid:] for row in X[mid:]]

        B11 = [row[:mid] for row in Y[:mid]]
        B12 = [row[mid:] for row in Y[:mid]]
        B21 = [row[:mid] for row in Y[mid:]]
        B22 = [row[mid:] for row in Y[mid:]]

        M1 = strassen(add(A11, A22), add(B11, B22))
        M2 = strassen(add(A21, A22), B11)
        M3 = strassen(A11, subtract(B12, B22))
        M4 = strassen(A22, subtract(B21, B11))
        M5 = strassen(add(A11, A12), B22)
        M6 = strassen(subtract(A21, A11), add(B11, B12))
        M7 = strassen(subtract(A12, A22), add(B21, B22))

        C11 = add(subtract(add(M1, M4), M5), M7)
        C12 = add(M3, M5)
        C21 = add(M2, M4)
        C22 = add(subtract(add(M1, M3), M2), M6)

        C = []

        for i in range(mid):
            C.append(C11[i] + C12[i])

        for i in range(mid):
            C.append(C21[i] + C22[i])

        return C

    result = strassen(A, B)

    return [
        row[:len(B[0])]
        for row in result[:len(A)]
    ]


r1 = int(input("Enter rows of matrix A: "))
c1 = int(input("Enter columns of matrix A: "))

A = []
print("Enter matrix A:")
for i in range(r1):
    A.append(list(map(int, input().split())))

r2 = int(input("Enter rows of matrix B: "))
c2 = int(input("Enter columns of matrix B: "))

B = []
print("Enter matrix B:")
for i in range(r2):
    B.append(list(map(int, input().split())))

result = strassen_multiply(A, B)

print("Product matrix:")
for row in result:
    print(*row)