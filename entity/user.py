class User:
    """Kullanıcı verilerinin tutulduğu varlık sınıfı

    @category: Entity Class"""

    def __init__(self) -> None:
        """Kullanıcı verilerinin tutulduğu varlık sınıfı

        @category: Entity Class"""
        self._id = -1
        self._tc: str = ""
        self._first_name: str = ""
        self._last_name: str = ""
        self._user_name: str = ""
        self._password: str = ""
        self._email: str = ""
        self._phone: str = ""
        self._address: str = ""
        self._user_type: str = ""

    @property
    def id(self) -> int:
        """Kullanıcı id bilgisini  verir

        Returns:
            int: kullanıcı id bilgisi
        """
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Kullanıcı id bilgisini ayarlar

        Args:
            value (int): kullanıcı id bilgisi
        """
        self._id = value

    @property
    def tc(self) -> str:
        """Kullanıcı TC bilgisini verir

        Returns:
            str: kullanıcı TC bilgisi
        """
        return self._tc

    @tc.setter
    def tc(self, value: str) -> None:
        """Kullanıcı TC bilgisini ayarlar

        Args:
            value (str): kullanıcı TC bilgisi
        """
        self._tc = value

    @property
    def first_name(self) -> str:
        """Kullanıcı isim bilgisini ayarlar

        Args:
            value (str): kullanıcı isim bilgisi
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Kullanıcı isim bilgisini verir

        Args:
            value (str): kullanıcı isim bilgisi
        """
        self._first_name = value

    @property
    def last_name(self) -> str:
        """Kullanıcı soyad bilgisini verir

        Returns:
            str: kullanıcı soyad bilgisi
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Kullanıcı soyad bilgisini ayarlar

        Args:
            value (str): kullanıcı soyad bilgisi
        """
        self._last_name = value

    @property
    def user_name(self) -> str:
        """Kullanıcının kullanıcı adını verir

        Returns:
            str: kullanıcı adı
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value: str) -> None:
        """Kullanıcının kullanıcı adını ayarlar

        Args:
            value (str): kullanıcı adı
        """
        self._user_name = value

    @property
    def password(self) -> str:
        """Kullanıcının şifresini verir

        Returns:
            str: kullanıcı şifresi
        """
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        """Kullanıcının şifre bilgisini ayarlar

        Args:
            value (str): kullanıcı şifresi
        """
        self._password = value

    @property
    def email(self) -> str:
        """Kullanıcının e-posta bilgisini verir

        Returns:
            str: kullanıcı e-posta bilgisi
        """
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Kullanıcının e-posta bilgisini ayarlar

        Args:
            value (str): kullanıcı e-posta bilgisi
        """
        self._email = value

    @property
    def phone(self) -> str:
        """Kullanıcının telefon numarasını verir

        Returns:
            str: kullanıcı telefon numarası
        """
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        """Kullanıcının telefon numarasını ayarlar

        Args:
            value (str): kullanıcı telefon numarası
        """
        self._phone = value

    @property
    def address(self) -> str:
        """Kullanıcının adres bilgisini verir

        Returns:
            str: kullanıcı adres bilgisi
        """
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        """Kullanıcının adres bilgisini ayarlar

        Args:
            value (str): kullanıcı adres bilgisi
        """
        self._address = value

    @property
    def user_type(self) -> str:
        """Kullanıcının kullanıcı tipini verir

        Returns:
            str: kullanıcı tipi
        """
        return self._user_type

    @user_type.setter
    def user_type(self, value="1") -> None:
        """Kullanıcının kullanıcı tipini ayarlar

        Args:
            value (str, optional): kullanıcı tipi. Defaults to "1".
        """
        self._user_type = value
