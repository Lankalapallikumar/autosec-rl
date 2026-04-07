def compute_score(rewards):
    if not rewards:
        return 0.01  # minimum safe value

    # normalize rewards to 0–1
    avg = sum(rewards) / len(rewards)

    # scale assuming reward range roughly [-1.5, 1]
    normalized = (avg + 1.5) / 2.5

    # 🔥 CLAMP STRICTLY BETWEEN (0,1)
    epsilon = 0.01

    if normalized <= 0:
        return epsilon
    if normalized >= 1:
        return 1 - epsilon

    return normalized
