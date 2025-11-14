def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
    # ketentuan
    if not a or not a[0]:
        return -1

    # dimensi
    m = len(a)      # baris a
    n = len(a[0])   # kolom b
    o = len(b)      # panjang vektor

    # pastikan kolom di a sama dengan panjang vektor b
    if o != n:
        return -1

    # buat list kosong untuk menyimpan hasil
    res = [0]*m
    
    # pertama looping ke baris dulu
    for i in range(m):
        res[i] = sum([a[i][j]*b[j] for j in range(n)])  # kedua looping ke kolom

    return res
