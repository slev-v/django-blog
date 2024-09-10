from abc import (
    ABC,
    abstractmethod,
)

from core.apps.posts.models import Vote


class BaseVoteService(ABC):
    @abstractmethod
    def vote(self, post_id: int, user_id: int, vote_type: int) -> None: ...


class VoteService(BaseVoteService):
    def vote(self, post_id: int, user_id: int, vote_type: int) -> None:
        vote, _ = Vote.objects.update_or_create(
            post_id=post_id,
            user_id=user_id,
            defaults={"vote_type": vote_type},
        )
        vote.save()
