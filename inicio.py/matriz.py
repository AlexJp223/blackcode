# Programa: Declaración y recorrido de una matriz 3x3
# Declaración de la matriz 3x3 con números enteros

matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
 
print("Valores de la matriz 3x3:")
for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")