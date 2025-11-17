def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	# dapatkan baris dan kolom a
    m, n = len(a), len(a[0])

    # inisialisasi matriks kosong
    # dengan n row, m col (kebalikan dari a)
    a_transposed = [[0] * m for _ in range(n)]

    # kita sudah ada matriks kosong, dengan keadaan sudah di transpose
    # lets fill dengan loop
    for i in range(n):      # baris
        for j in range(m):  # kolom
            a_transposed[i][j] = a[j][i]
    return a_transposed


# sejatinya matriks adalah list dalam list (list pertama baris, di dalam list ada berapa kolom)
# len(a) -> ada berapa list di list (baris). tiap baris di a itu juga punya dimensi, karena dia vektor
# maka ... x 1. jika kita akses a[0] bisa dapet banyak kolom

# ALTERNATE
# def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
#     if not a or not a[0]:
#         return []
#     m, n = len(a), len(a[0])
#     return [[a[j][i] for j in range(m)] for i in range(n)]