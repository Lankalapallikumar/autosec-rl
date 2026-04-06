def compute_score(rewards):
    if not rewards:
        return 0.0

    score = sum(rewards) / len(rewards)
    return max(0.0, min(1.0, score))