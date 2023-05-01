from entity.user import User
from entity.eventType import EventType


class Event:
    """Olayların tutulduğu varlık sınıfı

    @category: Entity Class"""

    def __init__(self) -> None:
        self._id = -1
        self._user: User = User()
        self._event_type: EventType = EventType()
        self._date: str = ""
        self._start_time: str = ""
        self._finish_time: str = ""
        self._description: str = ""
        self._remember_time: int = 0

    @property
    def id(self) -> int:
        """Etkinlik id bilgisini verir

        Returns:
            int: etkinlik id bilgisi
        """
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Etkinlik id bilgisini ayarlar

        Args:
            value (int): etkinlik id bilgisi
        """
        self._id = value

    @property
    def user(self) -> User:
        """Kullanıcı bilgisini verir

        Returns:
            User: kullanıcı bilgisi
        """
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        """Kullanıcı bilgisini ayarlar

        Args:
            value (User): kullanıcı bilgisi
        """
        self._user = value

    @property
    def event_type(self) -> EventType:
        """etkinlik tipi bilgisini verir

        Returns:
            EventType: etkinlik tipi bilgisi
        """
        return self._event_type

    @event_type.setter
    def event_type(self, value: EventType) -> None:
        """etkinlik tipi bilgisini ayarlar

        Args:
            value (EventType): etkinlik tipi bilgisi
        """
        self._event_type = value

    @property
    def date(self) -> str:
        """Tarih bilgisini verir

        Returns:
            str: tarih bilgisi
        """
        return self._date

    @date.setter
    def date(self, value: str) -> None:
        """Tarih bilgisini ayarlar

        Args:
            value (str): tarih bilgisi
        """
        self._date = value

    @property
    def start_time(self) -> str:
        """Etkinlik başlangıç saati bilgisini verir

        Returns:
            str: başlangıç saati
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value: str) -> None:
        """Etkinlik başlangıç saat bilgisini ayarlar

        Args:
            value (str): başlangıç saati
        """
        self._start_time = value

    @property
    def finish_time(self) -> str:
        """Etkinlik bitiş saati bilgisini verir

        Returns:
            str: bitiş saati
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value: str) -> None:
        """Etkinlik bitiş saati bilgisini ayarlar

        Args:
            value (str): bitiş saati
        """
        self._finish_time = value

    @property
    def description(self) -> str:
        """Etkinlik açıklamasını verir

        Returns:
            str: etkinlik açıklaması
        """
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Etkinlik açıklamasını ayarlar

        Args:
            value (str): etkinlik açıklaması
        """
        self._description = value

    @property
    def remember_time(self) -> int:
        """Etkinlik için kaç dakika önce hatırlatılacağını verir

        Returns:
            int: etkinliği hatırlatma dakikası"""
        return self._remember_time

    @remember_time.setter
    def remember_time(self, value: int) -> None:
        """Etkinlik için kaç dakika önce hatırlatılacağını ayarlar

        Args:
            value (int): etkinlik hatırlatma dakikası
        """
        self._remember_time = value
