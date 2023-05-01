class EventType:
    """Olay tanımlamalarının tutulduğu varlık sınıfı

    @category: Entity Class"""

    def __init__(self) -> None:
        """Olay tanımlamalarının tutulduğu varlık sınıfı

        @category: Entity Class"""

        self._id = -1
        self._name: str = ""

    @property
    def id(self) -> int:
        """Olay id bilgisini verir

        Returns:
            int: olay id
        """
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Olay id bilgisini ayarlar

        Args:
            value (int): olay id bilgisi
        """
        self._id = value

    @property
    def name(self) -> str:
        """Olay isim bilgisini verir

        Returns:
            str: olay isim bilgisi
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Olay isim bilgisini ayarlar

        Args:
            value (str): olay isim bilgisi
        """
        self._name = value
