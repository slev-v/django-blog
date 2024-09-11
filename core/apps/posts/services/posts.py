from abc import (
    ABC,
    abstractmethod,
)

from core.apps.posts.exceptions import ForbiddenException, PostNotFoundException
from core.apps.posts.models import Post as PostModel
from core.apps.posts.entities import Post as PostEntity


class BasePostService(ABC):
    @abstractmethod
    def get(self, post_id: int) -> PostEntity: ...

    @abstractmethod
    def create(self, title: str, content: str, user_id: int) -> PostEntity: ...

    @abstractmethod
    def get_posts_by_user(self, user_id: int) -> list[PostEntity]: ...

    @abstractmethod
    def get_latest_posts(self) -> list[PostEntity]: ...

    @abstractmethod
    def update(self, post_id: int, title: str, content: str) -> PostEntity: ...

    @abstractmethod
    def delete(self, post_id: int) -> None: ...


class PostService(BasePostService):
    def get(self, post_id: int) -> PostEntity:
        try:
            post_model = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            raise PostNotFoundException()

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

    def get_latest_posts(self) -> list[PostEntity]:
        post_models = PostModel.objects.order_by("-created_at")
        return [post_model.to_entity() for post_model in post_models]

    def update(
        self, post_id: int, user_id: int, title: str, content: str
    ) -> PostEntity:
        try:
            post_model = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            raise PostNotFoundException()

        if user_id != post_model.user_id:
            raise ForbiddenException()

        post_model.title = title
        post_model.content = content
        post_model.save()

        return post_model.to_entity()

    def delete(self, post_id: int, user_id: int) -> None:
        try:
            post_model = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            raise PostNotFoundException()

        if user_id != post_model.user_id:
            raise ForbiddenException()

        post_model.delete()
