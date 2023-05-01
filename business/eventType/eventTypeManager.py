from business.eventType.iEventTypeManager import IEventTypeManager
from dataAccess.eventType.eventTypeDal import EventTypeDal
from entity.eventType import EventType


class EventTypeManager(IEventTypeManager):
    """Olay Tanımlama işlemleriyle ilgili operasyonların bulunduğu sınıf.
    IEventTypeManager arayüzünü uygular

    @see: IEventTypeManager
    @category: Business, Manager"""

    def __init__(self) -> None:
        super().__init__()
        self._etdal = EventTypeDal()

    def insert(self, event_type: EventType) -> bool:
        """Veritabanına olay tipi eklemeyi sağlar

        Args:
            event_type (EventType): olay tipi

        Returns:
            bool: ekleme durumu
        """
        event_type.name = event_type.name.lower().title()
        try:
            self._etdal.insert(event_type)
            return True
        except Exception:
            return False

    def update(self, event_type: EventType):
        """Veritabanındaki olay tipi bilgilerini güncellemeyi sağlar

        Args:
            event_type (EventType): olay bilgileri

        Returns:
            bool: güncelleme durumu
        """
        event_type.name = event_type.name.lower().title()
        try:
            self._etdal.update(event_type)
            return True
        except Exception:
            return False

    def delete(self, event_type: EventType) -> bool:
        """Veritabanındaki olay tipini silmeyi sağlar

        Args:
            event_type (EventType): olay tipi bilgisi

        Returns:
            bool: silme durumu
        """
        try:
            if self._etdal.is_event_type(event_type.name):
                self._etdal.delete(event_type)
                return True
            return False
        except Exception:
            return False

    def get_event_type_id(self, event_type_name: str):
        """Olay tipinin id bilgisini getirir

        Args:
            event_name (str): olay adı

        Returns:
            int: kullanıcı id bilgisi | kullanıcı yoksa -1
        """
        e_type = EventType()
        e_type.name = event_type_name
        if self._etdal.is_event_type(e_type.name):
            return self._etdal.get_event_type_id(e_type.name)
        return -1

    def get_all_event_types(self, name="") -> list[EventType]:
        """Veritabanındaki tüm olay tiplerini verir

        Returns:
            list[EventType]: olay tipleri listesi
        """
        return self._etdal.get_all_event_types(name)

    def is_event_type(self, event_type_name: str) -> bool:
        """Etkinlik tipi adı ile etkinlik tipinin veritabanına kayıtlı olup olmadığını kontrol etmeyi sağlar.

        Args:
            event_type_name (User): etkinlik tibi adı

        Returns:
            bool: kayıt durumu
        """
        return self._etdal.is_event_type(event_type_name.lower().title())
