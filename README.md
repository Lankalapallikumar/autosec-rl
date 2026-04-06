\# 🔐 AutoSec-RL: Adaptive Cybersecurity Reinforcement Learning Environment



\## 🚀 Overview



AutoSec-RL is a \*\*real-world reinforcement learning environment\*\* that simulates decision-making in a Security Operations Center (SOC). 



The environment challenges an AI agent to \*\*detect and respond to cyber threats\*\* under uncertainty, balancing security risks and false positives through sequential decision-making.



\---



\## 🎯 Problem Statement



Modern cybersecurity systems struggle with:



\- Evolving attack patterns (adaptive attackers)

\- High false positive rates

\- Delayed detection of stealth threats



Traditional rule-based systems fail to handle these complexities.



👉 \*\*Our solution\*\*: A reinforcement learning environment where agents learn to make \*\*context-aware, sequential decisions\*\*.



\---



\## 🧠 Why Reinforcement Learning?



Unlike static classification tasks, this environment:



\- Maintains \*\*state across time\*\*

\- Introduces \*\*delayed consequences\*\*

\- Requires \*\*trade-offs between actions\*\*



👉 Actions affect future states and rewards, making it a \*\*true RL problem\*\*.



\---



\## ⚙️ Environment Design



\### 🔍 Observation Space



Each step provides:



\- `login\_history` → login attempt patterns

\- `data\_pattern` → network/data usage behavior

\- `attack\_type` → hidden attack signal

\- `alert\_level` → system alert state

\- `damage` → accumulated system damage

\- `blocked\_users` → false positive tracking

\- `session\_score` → performance metric



\---



\### 🎮 Action Space



Agent chooses one action:



\- `allow` → allow traffic

\- `block\_ip` → block suspicious IP

\- `monitor` → observe activity

\- `rate\_limit` → restrict traffic



\---



\### 🎯 Reward Function



Designed for \*\*dense and meaningful feedback\*\*:



\- ✅ +1 → correct detection

\- ⚠️ partial reward → safe monitoring

\- ❌ penalties → wrong actions

\- ⏳ delayed penalty → accumulated damage



\---



\## 🧪 Tasks (Difficulty Progression)



| Task | Description | Challenge |

|------|------------|----------|

| 🟢 Easy | Brute-force attack detection | Obvious patterns |

| 🟡 Medium | Mixed traffic classification | Avoid false positives |

| 🔴 Hard | Adaptive stealth attacks | Requires sequential reasoning |



\---



\## 🤖 Agent Design



We use a \*\*hybrid agent\*\*:



\- LLM-based reasoning (Hugging Face Router)

\- Rule-based fallback (robustness)



👉 Ensures:

\- Real reasoning capability

\- No failure due to API limits



\---



\## 🔁 RL Interaction Loop

\# 🔐 AutoSec-RL: Adaptive Cybersecurity Reinforcement Learning Environment



\## 🚀 Overview



AutoSec-RL is a \*\*real-world reinforcement learning environment\*\* that simulates decision-making in a Security Operations Center (SOC). 



The environment challenges an AI agent to \*\*detect and respond to cyber threats\*\* under uncertainty, balancing security risks and false positives through sequential decision-making.



\---



\## 🎯 Problem Statement



Modern cybersecurity systems struggle with:



\- Evolving attack patterns (adaptive attackers)

\- High false positive rates

\- Delayed detection of stealth threats



Traditional rule-based systems fail to handle these complexities.



👉 \*\*Our solution\*\*: A reinforcement learning environment where agents learn to make \*\*context-aware, sequential decisions\*\*.



\---



\## 🧠 Why Reinforcement Learning?



Unlike static classification tasks, this environment:



\- Maintains \*\*state across time\*\*

\- Introduces \*\*delayed consequences\*\*

\- Requires \*\*trade-offs between actions\*\*



👉 Actions affect future states and rewards, making it a \*\*true RL problem\*\*.



\---



\## ⚙️ Environment Design



\### 🔍 Observation Space



Each step provides:



\- `login\_history` → login attempt patterns

\- `data\_pattern` → network/data usage behavior

\- `attack\_type` → hidden attack signal

\- `alert\_level` → system alert state

\- `damage` → accumulated system damage

\- `blocked\_users` → false positive tracking

\- `session\_score` → performance metric



\---



\### 🎮 Action Space



Agent chooses one action:



\- `allow` → allow traffic

\- `block\_ip` → block suspicious IP

\- `monitor` → observe activity

\- `rate\_limit` → restrict traffic



\---



\### 🎯 Reward Function



Designed for \*\*dense and meaningful feedback\*\*:



\- ✅ +1 → correct detection

\- ⚠️ partial reward → safe monitoring

\- ❌ penalties → wrong actions

\- ⏳ delayed penalty → accumulated damage



\---



\## 🧪 Tasks (Difficulty Progression)



| Task | Description | Challenge |

|------|------------|----------|

| 🟢 Easy | Brute-force attack detection | Obvious patterns |

| 🟡 Medium | Mixed traffic classification | Avoid false positives |

| 🔴 Hard | Adaptive stealth attacks | Requires sequential reasoning |



\---



\## 🤖 Agent Design



We use a \*\*hybrid agent\*\*:



\- LLM-based reasoning (Hugging Face Router)

\- Rule-based fallback (robustness)



👉 Ensures:

\- Real reasoning capability

\- No failure due to API limits



\---



\## 🔁 RL Interaction Loop

\# 🔐 AutoSec-RL: Adaptive Cybersecurity Reinforcement Learning Environment



\## 🚀 Overview



AutoSec-RL is a \*\*real-world reinforcement learning environment\*\* that simulates decision-making in a Security Operations Center (SOC). 



The environment challenges an AI agent to \*\*detect and respond to cyber threats\*\* under uncertainty, balancing security risks and false positives through sequential decision-making.



\---



\## 🎯 Problem Statement



Modern cybersecurity systems struggle with:



\- Evolving attack patterns (adaptive attackers)

\- High false positive rates

\- Delayed detection of stealth threats



Traditional rule-based systems fail to handle these complexities.



👉 \*\*Our solution\*\*: A reinforcement learning environment where agents learn to make \*\*context-aware, sequential decisions\*\*.



\---



\## 🧠 Why Reinforcement Learning?



Unlike static classification tasks, this environment:



\- Maintains \*\*state across time\*\*

\- Introduces \*\*delayed consequences\*\*

\- Requires \*\*trade-offs between actions\*\*



👉 Actions affect future states and rewards, making it a \*\*true RL problem\*\*.



\---



\## ⚙️ Environment Design



\### 🔍 Observation Space



Each step provides:



\- `login\_history` → login attempt patterns

\- `data\_pattern` → network/data usage behavior

\- `attack\_type` → hidden attack signal

\- `alert\_level` → system alert state

\- `damage` → accumulated system damage

\- `blocked\_users` → false positive tracking

\- `session\_score` → performance metric



\---



\### 🎮 Action Space



Agent chooses one action:



\- `allow` → allow traffic

\- `block\_ip` → block suspicious IP

\- `monitor` → observe activity

\- `rate\_limit` → restrict traffic



\---



\### 🎯 Reward Function



Designed for \*\*dense and meaningful feedback\*\*:



\- ✅ +1 → correct detection

\- ⚠️ partial reward → safe monitoring

\- ❌ penalties → wrong actions

\- ⏳ delayed penalty → accumulated damage



\---



\## 🧪 Tasks (Difficulty Progression)



| Task | Description | Challenge |

|------|------------|----------|

| 🟢 Easy | Brute-force attack detection | Obvious patterns |

| 🟡 Medium | Mixed traffic classification | Avoid false positives |

| 🔴 Hard | Adaptive stealth attacks | Requires sequential reasoning |



\---



\## 🤖 Agent Design



We use a \*\*hybrid agent\*\*:



\- LLM-based reasoning (Hugging Face Router)

\- Rule-based fallback (robustness)



👉 Ensures:

\- Real reasoning capability

\- No failure due to API limits



\---



\## 🔁 RL Interaction Loop

\# 🔐 AutoSec-RL: Adaptive Cybersecurity Reinforcement Learning Environment



\## 🚀 Overview



AutoSec-RL is a \*\*real-world reinforcement learning environment\*\* that simulates decision-making in a Security Operations Center (SOC). 



The environment challenges an AI agent to \*\*detect and respond to cyber threats\*\* under uncertainty, balancing security risks and false positives through sequential decision-making.



\---



\## 🎯 Problem Statement



Modern cybersecurity systems struggle with:



\- Evolving attack patterns (adaptive attackers)

\- High false positive rates

\- Delayed detection of stealth threats



Traditional rule-based systems fail to handle these complexities.



👉 \*\*Our solution\*\*: A reinforcement learning environment where agents learn to make \*\*context-aware, sequential decisions\*\*.



\---



\## 🧠 Why Reinforcement Learning?



Unlike static classification tasks, this environment:



\- Maintains \*\*state across time\*\*

\- Introduces \*\*delayed consequences\*\*

\- Requires \*\*trade-offs between actions\*\*



👉 Actions affect future states and rewards, making it a \*\*true RL problem\*\*.



\---



\## ⚙️ Environment Design



\### 🔍 Observation Space



Each step provides:



\- `login\_history` → login attempt patterns

\- `data\_pattern` → network/data usage behavior

\- `attack\_type` → hidden attack signal

\- `alert\_level` → system alert state

\- `damage` → accumulated system damage

\- `blocked\_users` → false positive tracking

\- `session\_score` → performance metric



\---



\### 🎮 Action Space



Agent chooses one action:



\- `allow` → allow traffic

\- `block\_ip` → block suspicious IP

\- `monitor` → observe activity

\- `rate\_limit` → restrict traffic



\---



\### 🎯 Reward Function



Designed for \*\*dense and meaningful feedback\*\*:



\- ✅ +1 → correct detection

\- ⚠️ partial reward → safe monitoring

\- ❌ penalties → wrong actions

\- ⏳ delayed penalty → accumulated damage



\---



\## 🧪 Tasks (Difficulty Progression)



| Task | Description | Challenge |

|------|------------|----------|

| 🟢 Easy | Brute-force attack detection | Obvious patterns |

| 🟡 Medium | Mixed traffic classification | Avoid false positives |

| 🔴 Hard | Adaptive stealth attacks | Requires sequential reasoning |



\---



\## 🤖 Agent Design



We use a \*\*hybrid agent\*\*:



\- LLM-based reasoning (Hugging Face Router)

\- Rule-based fallback (robustness)



👉 Ensures:

\- Real reasoning capability

\- No failure due to API limits



\---



\## 🔁 RL Interaction Loop

\# 🔐 AutoSec-RL: Adaptive Cybersecurity Reinforcement Learning Environment



\## 🚀 Overview



AutoSec-RL is a \*\*real-world reinforcement learning environment\*\* that simulates decision-making in a Security Operations Center (SOC). 



The environment challenges an AI agent to \*\*detect and respond to cyber threats\*\* under uncertainty, balancing security risks and false positives through sequential decision-making.



\---



\## 🎯 Problem Statement



Modern cybersecurity systems struggle with:



\- Evolving attack patterns (adaptive attackers)

\- High false positive rates

\- Delayed detection of stealth threats



Traditional rule-based systems fail to handle these complexities.



👉 \*\*Our solution\*\*: A reinforcement learning environment where agents learn to make \*\*context-aware, sequential decisions\*\*.



\---



\## 🧠 Why Reinforcement Learning?



Unlike static classification tasks, this environment:



\- Maintains \*\*state across time\*\*

\- Introduces \*\*delayed consequences\*\*

\- Requires \*\*trade-offs between actions\*\*



👉 Actions affect future states and rewards, making it a \*\*true RL problem\*\*.



\---



\## ⚙️ Environment Design



\### 🔍 Observation Space



Each step provides:



\- `login\_history` → login attempt patterns

\- `data\_pattern` → network/data usage behavior

\- `attack\_type` → hidden attack signal

\- `alert\_level` → system alert state

\- `damage` → accumulated system damage

\- `blocked\_users` → false positive tracking

\- `session\_score` → performance metric



\---



\### 🎮 Action Space



Agent chooses one action:



\- `allow` → allow traffic

\- `block\_ip` → block suspicious IP

\- `monitor` → observe activity

\- `rate\_limit` → restrict traffic



\---



\### 🎯 Reward Function



Designed for \*\*dense and meaningful feedback\*\*:



\- ✅ +1 → correct detection

\- ⚠️ partial reward → safe monitoring

\- ❌ penalties → wrong actions

\- ⏳ delayed penalty → accumulated damage



\---



\## 🧪 Tasks (Difficulty Progression)



| Task | Description | Challenge |

|------|------------|----------|

| 🟢 Easy | Brute-force attack detection | Obvious patterns |

| 🟡 Medium | Mixed traffic classification | Avoid false positives |

| 🔴 Hard | Adaptive stealth attacks | Requires sequential reasoning |



\---



\## 🤖 Agent Design



We use a \*\*hybrid agent\*\*:





\- LLM-based reasoning (Hugging Face Router)

\- Rule-based fallback (robustness)



👉 Ensures:

\- Real reasoning capability

\- No failure due to API limits



\---



\## 🔁 RL Interaction Loop

Environment → Observation → Agent → Action → Reward → Next State



This loop continues across multiple steps, simulating real-world system evolution.



\---



\## 🧪 Running the Project



\### 1️⃣ Install dependencies



\---



\### 2️⃣ Set environment variables



Create `.env` file:

HF\_TOKEN=your\_huggingface\_token



\---



\### 3️⃣ Run inference



\---



\## 📊 Output Format



The system prints structured logs:

\[START] task=easy ...

\[STEP] step=1 action=block\_ip reward=1.00 ...

\[END] success=true score=0.85 ...



👉 This ensures reproducible evaluation.



\---



\## 🐳 Docker Support



Build and run:

docker build -t autosec .

docker run autosec



\---



\## 🌍 Deployment



The environment is deployable as a \*\*Hugging Face Space\*\* with full container support.



\---



\## 📈 Baseline Performance



| Task | Score |

|------|------|

| Easy | \~1.00 |

| Medium | \~0.6–0.8 |

| Hard | \~0.5–0.7 |



\---



\## 💡 Key Highlights



\- ✅ Real-world cybersecurity simulation  

\- ✅ True RL dynamics (stateful + delayed reward)  

\- ✅ LLM-powered agent  

\- ✅ Robust fallback mechanism  

\- ✅ Fully reproducible evaluation  



\---



\## 🏁 Conclusion



AutoSec-RL bridges the gap between \*\*static classification\*\* and \*\*real-world decision-making\*\*, providing a powerful benchmark for evaluating intelligent agents in cybersecurity.



\---



\## 👤 Author



Developed as part of the Meta PyTorch OpenEnv Hackathon.

