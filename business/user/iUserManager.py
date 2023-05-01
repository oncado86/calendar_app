from abc import abstractmethod as interface
from entity.user import User


class IUserManager:
    """Kullanıcı iş katmanı için gerekli olan metotların imzalarını tutar

    @category: Manager, Business"""

    @interface
    def insert(self, user: User):
        raise NotImplementedError("This is not implemented 'insert' from IUserManager")

    @interface
    def update(self, user: User):
        raise NotImplementedError("This is not implemented 'update' from IUserManager")

    @interface
    def get_user(self, user_name: str):
        raise NotImplementedError(
            "This is not implemented 'get_user' from IUserManager"
        )

    @interface
    def get_user_id(self, user_name: str):
        raise NotImplementedError(
            "This is not implemented 'get_user_id' from IUserManager"
        )

    @interface
    def is_user(self, user_name: str):
        raise NotImplementedError("This is not implemented 'is_user' from IUserManager")
