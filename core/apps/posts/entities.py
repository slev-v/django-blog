from dataclasses import dataclass, field
from datetime import datetime

from core.apps.users.entities import User


@dataclass
class Post:
    id: int | None = field(default=None, kw_only=True)
    title: str
    content: str
    created_at: datetime
    user: User
    reputation: int
