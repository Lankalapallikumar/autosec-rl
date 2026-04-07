from fastapi import FastAPI
from env import AutoSecEnv

app = FastAPI()

env_instance = None


# 🔥 ADD THIS (IMPORTANT)
@app.get("/")
def home():
    return {"message": "AutoSec-RL Environment Running"}


@app.post("/reset")
def reset(task: str = "easy"):
    global env_instance
    env_instance = AutoSecEnv(task)
    obs = env_instance.reset()
    return {"observation": obs.dict()}


@app.post("/step")
def step(action: dict):
    global env_instance
    obs, reward, done, info = env_instance.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    global env_instance
    return {"state": env_instance.state()}