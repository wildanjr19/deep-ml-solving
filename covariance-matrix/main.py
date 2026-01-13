def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # dapatkan baris dan kolom
    n_features, n_observations = len(vectors), len(vectors[0])

    # hitung mean untuk setiap fitur
    means = [sum(observations) / len(observations) for observations in vectors]

    # calculate kovarians
    covariance_matrix = [[0] * n_features for i in range(n_features)]

    for i in range(n_features):
        for j in range(i, n_features):
            # dapatkan mean dari means
            mean_i, mean_j = means[i], means[j]
            covariance_sum = sum(
                [(obs_i - mean_i) * (obs_j - mean_j) for obs_i, obs_j in zip(vectors[i], vectors[j])]
            )
            covariance = covariance_sum / (n_observations - 1)

            covariance_matrix[i][j] = covariance
            covariance_matrix[j][i] = covariance
    return covariance_matrix