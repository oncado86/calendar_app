class DbTabes:
    """Veritabanı tablo verilerinin tutulduğu varlık sınıfı

    @category: Tool Class"""

    @property
    def users(self) -> str:
        """Kullanıcılar tablosunun ismini verir

        Returns:
            str: kullanıcılar tablo ismi
        """
        return "kullanicilar"

    @property
    def event_types(self) -> str:
        """Olay Tanımlamaları tablosunun ismini verir

        Returns:
            str: olay tanımlamaları tablo ismi
        """
        return "olay_tanimlamalari"

    @property
    def evets(self) -> str:
        """Olaylar tablosunun ismini verir

        Returns:
            str: olaylar tablo ismi
        """
        return "olaylar"

    @property
    def id(self) -> str:
        """Tablolar için 'id' verir

        Returns:
            str: id
        """
        return "id"

    @property
    def tc(self) -> str:
        """Kullanıcılar tablosunda 'tc_no' verir

        Returns:
            str: tc_no
        """
        return "tc_no"

    @property
    def name(self) -> str:
        """Tablolar için 'ad' verir

        Returns:
            str: ad
        """
        return "ad"

    @property
    def last_name(self) -> str:
        """Kullanıcılar tablosunda 'soyad' verir

        Returns:
            str: soyad
        """
        return "soyad"

    @property
    def u_name(self) -> str:
        """Kullanıcılar tablosunda 'kullanıcı_adi' verir

        Returns:
            str: kullanici_adi
        """
        return "kullanici_adi"

    @property
    def password(self) -> str:
        """Kullanıcılar tablosunda 'sifre' verir

        Returns:
            str: sifre
        """
        return "sifre"

    @property
    def phone_number(self) -> str:
        """Kullanıcılar tablosunda 'telefon' verir

        Returns:
            str: telefon
        """
        return "telefon"

    @property
    def email(self) -> str:
        """Kullanıcılar tablosunda 'eposta' verir

        Returns:
            str: eposta
        """
        return "eposta"

    @property
    def address(self) -> str:
        """Kullanıcılar tablosunda 'adres' verir

        Returns:
            str: adres
        """
        return "adres"

    @property
    def u_type(self) -> str:
        """Kullanıcılar tablosunda 'kullanici_tipi' verir

        Returns:
            str: kullanici_tipi
        """
        return "kullanici_tipi"

    @property
    def u_id(self) -> str:
        """Olaylar tablosunda 'kullanici_id' verir

        Returns:
            str: kullanici_id
        """
        return "kullanici_id"

    @property
    def e_id(self) -> str:
        """Olaylar tablosunda 'olay_id' verir

        Returns:
            str: olay_id
        """
        return "olay_id"

    @property
    def date(self) -> str:
        """Olaylar tablosunda 'tarih' verir

        Returns:
            str: tarih
        """
        return "tarih"

    @property
    def start(self) -> str:
        """Olaylar tablosunda 'baslangic' verir

        Returns:
            str: baslangic
        """
        return "baslangic"

    @property
    def finish(self) -> str:
        """Olaylar tablosunda 'bitis' verir

        Returns:
            str: bitis
        """
        return "bitis"
