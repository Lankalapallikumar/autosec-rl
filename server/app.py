from fastapi import FastAPI, HTTPException
from env import AutoSecEnv
import uvicorn

app = FastAPI()

env_instance = None


# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "AutoSec-RL Environment Running"}


# ✅ Reset
@app.post("/reset")
def reset(task: str = "easy"):
    global env_instance
    try:
        env_instance = AutoSecEnv(task)
        obs = env_instance.reset()
        return {
            "observation": obs.dict() if hasattr(obs, "dict") else obs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ✅ Step
@app.post("/step")
def step(action: dict):
    global env_instance

    if env_instance is None:
        raise HTTPException(status_code=400, detail="Call /reset first")

    try:
        obs, reward, done, info = env_instance.step(action)
        return {
            "observation": obs.dict() if hasattr(obs, "dict") else obs,
            "reward": reward,
            "done": done,
            "info": info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ✅ State
@app.get("/state")
def state():
    global env_instance

    if env_instance is None:
        raise HTTPException(status_code=400, detail="Call /reset first")

    try:
        return {"state": env_instance.state()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 🔥 REQUIRED FOR OPENENV (VERY IMPORTANT)
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# 🔥 REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
