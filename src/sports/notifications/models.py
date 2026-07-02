from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class NotificationType(Enum):
    GOAL = "goal"
    RED_CARD = "red_card"
    YELLOW_CARD = "yellow_card"
    KICKOFF = "kickoff"
    HALFTIME = "halftime"
    FULLTIME = "fulltime"
    SUBSTITUTION = "substitution"
    FAVORITE = "favorite"
    SYSTEM = "system"


@dataclass(slots=True)
class Notification:
    notification_type: NotificationType

    title: str
    message: str

    fixture_id: int | None = None

    timestamp: datetime = datetime.now()

    read: bool = False