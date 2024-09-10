from abc import (
    ABC,
    abstractmethod,
)

from core.apps.posts.models import Post as PostModel
from core.apps.posts.entities import Post as PostEntity


class BasePostService(ABC):
    @abstractmethod
    def get(self, post_id: int) -> PostEntity: ...

    @abstractmethod
    def create(self, title: str, content: str, user_id: int) -> PostEntity: ...

    @abstractmethod
    def get_posts_by_user(self, user_id: int) -> list[PostEntity]: ...


class PostService(BasePostService):
    def get(self, post_id: int) -> PostEntity:
        post_model = PostModel.objects.get(id=post_id)
        return post_model.to_entity()

    def create(self, title: str, content: str, user_id: int) -> PostEntity:
        post_model = PostModel.objects.create(
            title=title,
            content=content,
            user_id=user_id,
        )
        return post_model.to_entity()

    def get_posts_by_user(self, user_id: int) -> list[PostEntity]:
        post_models = PostModel.objects.filter(user_id=user_id)
        return [post_model.to_entity() for post_model in post_models]
