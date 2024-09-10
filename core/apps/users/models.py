from django.db import models
from django.contrib.auth.models import AbstractUser

from core.apps.users.entities import User as UserEntity
from core.apps.posts.models import Vote


class CustomUser(AbstractUser):
    def to_entity(self):
        return UserEntity(
            id=self.id,
            username=self.username,
            email=self.email,
        )

    def get_karma(self):
        return (
            Vote.objects.filter(post__user=self).aggregate(models.Sum("vote_type"))[
                "vote_type__sum"
            ]
            or 0
        )
