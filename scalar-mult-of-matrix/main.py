def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# dapatkan baris dan kolom
    row, col = len(matrix), len(matrix[0])
    # loop
    for i in range(row):
        for j in range(col):
            matrix[i][j] = matrix[i][j] * scalar
    
    return matrix