def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	# notes: matrix adalah kumpulan list (vektor)
    # dapatkan panjang kolom 
    n_col = len(matrix[0])
    # definisikan list kosong untuk simpan means
    means = []

    # gunakan if untuk mode yang digunakan
    if mode == 'row':
        # looping untuk tiap list di matrix
        for row in matrix:
            mean = sum(row) / len(row)
            means.append(mean)
    # iterasi di kolom
    else:
        for i in range(n_col):
            # dapatkan kolom secara sama dari ketiga list (urut)
            column = [row[i] for row in matrix]   # ini akan jalan di tiap elemen di list (vektor) dalam          matrix       
            mean = sum(column) / len(column)
            means.append(mean)


    return means  