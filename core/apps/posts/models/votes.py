from django.db import models


class Vote(models.Model):
    VOTE_CHOICES = (
        (1, "Like"),
        (-1, "Dislike"),
    )

    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="votes"
    )
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="votes"
    )
    vote_type = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ("user", "post")
