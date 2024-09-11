from dataclasses import dataclass


from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class PostNotFoundException(ServiceException):
    @property
    def message(self):
        return "Post not found"


@dataclass(eq=False)
class UnauthorizedAccessException(ServiceException):
    @property
    def message(self):
        return "You are not authorized to perform this action"


@dataclass(eq=False)
class InvalidVoteTypeException(ServiceException):
    @property
    def message(self):
        return "Invalid vote type"


@dataclass(eq=False)
class ForbiddenException(ServiceException):
    @property
    def message(self):
        return "You are not allowed to perform this action"
