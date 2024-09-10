from django.db import models

from core.apps.users.models import CustomUser
from core.apps.posts.entities import Post as PostEntity


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def to_entity(self) -> PostEntity:
        return PostEntity(
            id=self.id,
            title=self.title,
            content=self.content,
            created_at=self.created_at,
            user_id=self.user_id,
        )
