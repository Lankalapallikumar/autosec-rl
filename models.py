from pydantic import BaseModel
from typing import List, Literal

ActionType = Literal["allow", "block_ip", "monitor", "rate_limit"]

class Observation(BaseModel):
    login_history: List[int]
    data_pattern: List[int]
    ip_reputation: float
    attack_type: str
    alert_level: float
    damage: float
    blocked_users: int
    session_score: float

class Action(BaseModel):
    action_type: ActionType