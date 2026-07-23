---
title: AutoSec-RL
emoji: 🔐
colorFrom: blue
colorTo: purple
sdk: docker
app_file: inference.py
pinned: false
---

# 🔐 AutoSec-RL: Adaptive Cybersecurity RL Environment

## 🚀 Overview

AutoSec-RL is a **real-world reinforcement learning environment** designed to simulate decision-making in cybersecurity systems.

The environment mimics how a Security Operations Center (SOC) detects and responds to threats under uncertainty.

---

## 🎯 Problem

Modern cybersecurity faces:

- Evolving attack strategies  
- False positives  
- Delayed detection of stealth attacks  

Traditional rule-based systems fail to adapt.

👉 This environment enables training and evaluation of intelligent agents to solve these challenges.

---

## 🧠 Why Reinforcement Learning?

This is not a static classification problem.

✔ Actions affect future states  
✔ Rewards are delayed  
✔ Sequential decisions matter  

👉 Hence, it is a true RL environment.

---

## ⚙️ Environment Design

### 🔍 Observation Space

Each step includes:

- `login_history` → login attempts pattern  
- `data_pattern` → network usage behavior  
- `attack_type` → hidden threat  
- `alert_level` → system alert state  
- `damage` → accumulated system damage  
- `blocked_users` → tracking false positives  
- `session_score` → performance metric  

---

### 🎮 Action Space

Agent chooses one:

- `allow`  
- `block_ip`  
- `monitor`  
- `rate_limit`  

---

### 🎯 Reward Function

- ✅ +1 → correct action  
- ⚠️ partial reward → safe monitoring  
- ❌ penalty → wrong decisions  
- ⏳ delayed penalty → accumulated damage  

---

## 🧪 Tasks

| Task | Description |
|------|------------|
| 🟢 Easy | Brute-force attack detection |
| 🟡 Medium | Mixed traffic (normal + suspicious) |
| 🔴 Hard | Stealth adaptive attack |

---

## 🤖 Agent

Hybrid approach:

- LLM (Hugging Face Router)
- Rule-based fallback

👉 Ensures robustness + real reasoning

---

## 🔁 RL Loop

```
Observation → Action → Reward → Next State
```

---

## ▶️ How to Run

### Install dependencies

```
pip install -r requirements.txt
```

---

### Set environment variable

Create `.env`:

```
HF_TOKEN=your_token_here
```

---

### Run

```
python inference.py
```

---

## 📊 Output Format

```
[START] task=easy ...
[STEP] step=1 action=block_ip reward=1.00 ...
[END] success=true score=0.85 ...
```

---

## 🐳 Docker

```
docker build -t autosec .
docker run autosec
```

---

## 🌍 Deployment

This project is deployed using Hugging Face Spaces (Docker-based).

---

## 📈 Baseline Performance

| Task | Score |
|------|------|
| Easy | ~1.00 |
| Medium | ~0.6–0.8 |
| Hard | ~0.5–0.7 |

---

## 💡 Highlights

- Real-world cybersecurity simulation  
- True RL dynamics  
- LLM + fallback hybrid agent  
- Fully reproducible  
- Hackathon compliant  

---

## 🏁 Conclusion

AutoSec-RL provides a realistic benchmark for evaluating intelligent agents in cybersecurity decision-making.

---

## 👤 Author
Developed for Meta PyTorch OpenEnv Hackathon.
