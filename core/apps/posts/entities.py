from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Post:
    id: int | None = field(default=None, kw_only=True)
    title: str
    content: str
    created_at: datetime
    user_id: int
