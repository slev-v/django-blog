from abc import (
    ABC,
    abstractmethod,
)

from core.apps.posts.exceptions import InvalidVoteTypeException, PostNotFoundException
from core.apps.posts.models import Vote, Post


class BaseVoteService(ABC):
    @abstractmethod
    def vote(self, post_id: int, user_id: int, vote_type: int) -> None: ...


class VoteService(BaseVoteService):
    def vote(self, post_id: int, user_id: int, vote_type: int) -> None:
        if vote_type not in [-1, 1]:
            raise InvalidVoteTypeException()

        try:
            Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise PostNotFoundException()

        vote, _ = Vote.objects.update_or_create(
            post_id=post_id,
            user_id=user_id,
            defaults={"vote_type": vote_type},
        )
        vote.save()
