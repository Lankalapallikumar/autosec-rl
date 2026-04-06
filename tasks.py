import random

def get_task_config(task):
    random.seed(42)

    if task == "easy":
        return {"type": "brute_force"}
    elif task == "medium":
        return {"type": "mixed"}
    elif task == "hard":
        return {"type": "adaptive"}