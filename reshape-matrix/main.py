import numpy as np

# alternatif 1
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# dapatkan m dan n
    m_old, n_old = len(a), len(a[0])
    m_new, n_new = new_shape[0], new_shape[1]
	
    # ketentuan
    if m_old * n_old != m_new * n_new:
        return []

    # jadikan array
    arr_a = np.array(a)
    # kita reshape sesuai target
    reshaped_matrix = arr_a.reshape(new_shape)
    
    return reshaped_matrix