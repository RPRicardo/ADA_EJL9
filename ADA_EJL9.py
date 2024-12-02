def triangulo_pascal(numRows):
    # Inicializar el triángulo vacío
    triangulo = []

    # Construir cada fila
    for i in range(numRows):
        # Inicializar la nueva fila con todos 1's
        row = [1] * (i + 1)
        
        # Calcular los valores internos de la fila
        for j in range(1, i):  # Los extremos siempre son 1, no se calculan
            row[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        
        # Añadir la fila al triángulo
        triangulo.append(row)
    
    return triangulo


numRows = 15
pascalT = triangulo_pascal(numRows)
#print("El triangulo de pascal es:",pascalT)
print("El triangulo de pascal es:")
# en "triangulo"
for fila in pascalT:
    print(" ".join(map(str, fila)))
