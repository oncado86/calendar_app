from dataAccess.event.eventDal import EventDal
from business.event.iEventManager import IEventManager
from entity.event import Event
from entity.user import User


class EventManager(IEventManager):
    """Olay Tanımlama işlemleriyle ilgili operasyonların bulunduğu sınıf.
    IEventTypeManager arayüzünü uygular

    @see: IEventTypeManager
    @category: Business, Manager"""

    def __init__(self) -> None:
        super().__init__()
        self._edal = EventDal()

    def insert(self, event: Event) -> bool:
        """Veritabanına olay eklemeyi sağlar

        Args:
            event (Event): olay

        Returns:
            bool: ekleme durumu
        """
        try:
            self._edal.insert(event)
            return True
        except Exception:
            return False

    def update(self, event: Event) -> bool:
        """Veritabanındaki olay bilgisini güncellemeyi sağlar

        Args:
            event (Event): olay bilgisi

        Returns:
            bool: güncelleme durumu
        """
        try:
            self._edal.update(event)
            return True
        except Exception:
            return False

    def delete(self, event: Event) -> bool:
        """Veritabanındaki olayı silmeyi sağlar

        Args:
            event (Event): olay bilgisi

        Returns:
            bool: silme durumu
        """
        try:
            self._edal.delete(event)
            return True
        except Exception:
            return False

    def get_all_events(self, user: User, date: str, description="") -> list[Event]:
        """Veritabanındaki tüm olayları verir

        Args:
            user (User): kullanıcı bilgisi

        Returns:
            list[Event]: admin girişinde tüm etkinlikler | kullanıcı girişinde kullanıcının etkinlikleri
        """

        return self._edal.get_all_events(user, date, description)

    def get_event_id(self, date: str, start: str, finish: str) -> int:
        """Veritabanında kayıtlı olan olayın id bilgisini verir

        Args:
            date (str): olay tarihi
            start (str): olay başlangıç saati
            finish (str): olay bitiş saati

        Returns:
            int: olay id"""
        return self._edal.get_event_id(date, start, finish)

    def is_event(self, event: Event) -> bool:
        """Olay bilgilerini veritabanı ile kıyaslayıp, veritabanında istenilen tarih ve saatte kayıt olup olmadığını kontrol etmeni sağlar

        Args:
            event (Event): olay bilgileri

        Returns:
            bool: olay durumu
        """
        return self._edal.is_event(event)
