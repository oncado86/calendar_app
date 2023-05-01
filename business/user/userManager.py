from business.user.iUserManager import IUserManager
from dataAccess.user.userDal import UserDal
from entity.user import User


class UserManager(IUserManager):
    """Kullanıcı işlemleriyle ilgili operasyonların bulunduğu sınıf.
    IUserManager arayüzünü uygular

    @see: IUserManager
    @category: Business, Manager"""

    def __init__(self) -> None:
        super().__init__()
        self._udal = UserDal()

    def insert(self, user: User) -> bool:
        """Veritabanına kullanıcı eklemeyi sağlar

        Args:
            user (User): kullanıcı verileri

        Returns:
            bool: ekleme durumu
        """
        try:
            self._udal.insert(user)
            return True
        except Exception:
            return False

    def update(self, user: User) -> bool:
        """Veritabanındaki kullanıcının bilgilerini güncellemeyi sağlar

        Args:
            user (User): kullanıcı bilgileri

        Returns:
            bool: ekleme durumu
        """
        try:
            self._udal.update(user)
            return True
        except Exception:
            return False

    def delete(self, user: User) -> bool:
        """Veritabanından kullanıcı silmeyi sağlar

        Args:
            user (User): kullanıcı verileri

        Returns:
            bool: silme durumu
        """
        try:
            self._udal.delete(user)
            return True
        except Exception:
            return False

    def get_user(self, u_id: int) -> User:
        """Veritabanından bir kullanıcıyı getirmeyi sağlar

        Args:
            u_id (int): kullanıcı id

        Returns:
            User | None: Kullanıcı varsa kullanıcı bilgilerini verir, kullanıcı yoksa None geri döner
        """
        return self._udal.get_user(u_id)

    def get_user_id(self, user_name: str) -> int:
        """Kullanıcının id bilgisini verir

        Args:
            user_name (str): kullanıcı adı

        Returns:
            int: kullanıcı id bilgisi | kullanıcı yoksa -1
        """
        user = User()
        user.user_name = user_name
        if self._udal.is_user(user):
            return self._udal.get_user_id(user.user_name)
        return -1

    def is_user(self, user: User) -> bool:
        """Kullanıcı adı ile kullanıcının veritabanına kayıtlı olup olmadığını kontrol etmeyi sağlar.

        Args:
            user (User): kullanıcı bilgileri

        Returns:
            bool: kayıt durumu
        """
        return self._udal.is_user(user)

    def get_all_users(self, uname="") -> list[User]:
        """Veritabanındaki tüm kullanıcıları verir

        Returns:
            list[User]: kullanıcı listesi
        """
        return self._udal.get_all_users(uname)
