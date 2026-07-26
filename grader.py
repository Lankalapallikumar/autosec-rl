def compute_score(rewards):
    if not rewards:
        return 0.01  # minimum safe value
    avg = sum(rewards) / len(rewards)

    # scale assuming reward range roughly [-1.5, 1]
    normalized = (avg + 1.5) / 2.5
    epsilon = 0.01

    if normalized <= 0:
        return epsilon
    if normalized >= 1:
        return 1 - epsilon

    return normalized
