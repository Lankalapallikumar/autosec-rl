import random
from models import Observation
from tasks import get_task_config
class AutoSecEnv:

    def __init__(self, task, max_steps=8):
        random.seed(42)
        self.task = task
        self.cfg = get_task_config(task)
        self.max_steps = max_steps

    def reset(self):
        self.steps = 0
        self.rewards = []
        self.alert_level = 0
        self.damage = 0
        self.blocked_users = 0

        self._update_state()
        return self._get_obs()

    def _update_state(self):
        t = self.cfg["type"]

        login_history = [random.randint(0, 5) for _ in range(5)]
        data_pattern = [random.randint(10, 300) for _ in range(5)]

        if t == "brute_force":
            login_history = [5, 10, 15, 20, 25]
            attack = "brute_force"

        elif t == "mixed":
            attack = random.choice(["normal", "attack"])

        elif t == "adaptive":
            if self.steps > 3:
                data_pattern = [300, 400, 500, 600, 700]
                attack = "stealth"
            else:
                attack = "transition"

        self.state = {
            "login_history": login_history,
            "data_pattern": data_pattern,
            "attack_type": attack,
            "ip_reputation": random.uniform(0.2, 0.9)
        }

    def _get_obs(self):
        session_score = sum(self.rewards) / len(self.rewards) if self.rewards else 0.0
        return Observation(
            **self.state,
            alert_level=self.alert_level,
            damage=self.damage,
            blocked_users=self.blocked_users,
            session_score=session_score
        )

    def step(self, action):
        self.steps += 1
        attack = self.state["attack_type"]
        data_sum = sum(self.state["data_pattern"])

        reward = 0

        # RL logic
        if attack in ["brute_force", "attack"]:
            if action["action_type"] == "block_ip":
                reward += 1
                self.alert_level += 1
            elif action["action_type"] == "monitor":
                reward += 0.3
            else:
                self.damage += 1
                reward -= 1

        elif attack == "normal":
            if action["action_type"] == "block_ip":
                self.blocked_users += 1
                reward -= 1
            elif action["action_type"] == "allow":
                reward += 1
            else:
                reward += 0.2

        elif attack == "transition":
            if action["action_type"] in ["monitor", "rate_limit"]:
                reward += 0.4
            else:
                reward -= 0.4

        elif attack == "stealth":
            if data_sum > 1500 and action["action_type"] in ["monitor", "rate_limit"]:
                reward += 0.8
            else:
                self.damage += 2
                reward -= 1

        # delayed penalty
        if self.damage > 2:
            reward -= 0.5

        self.rewards.append(reward)

        self._update_state()

        done = self.steps >= self.max_steps
        return self._get_obs(), reward, done, {}

    def state(self):
        return self.state
