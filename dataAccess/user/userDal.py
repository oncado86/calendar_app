from dataAccess.dbHelper.sqliteDbHelper import SqliteDbHelper as db_helper
from entity.user import User


class UserDal(db_helper):
    """Kullanıcı veri erişim katmanı ile ilgili operasyonların bulunduğu sınıf.
    SqLiteDbHelper sınıfından miras alır

    @see: SqliteDbHelper
    @category: Data Access"""

    def __init__(self) -> None:
        super().__init__()

    def insert(self, user: User) -> None:
        """Veritabanına kullanıcı eklemeyi sağlar

        Args:
            user (User): kullanıcı bilgileri
        """
        self.query = f"INSERT INTO {self.tbl_values.users}({self.tbl_values.tc}, {self.tbl_values.name}, {self.tbl_values.last_name}, {self.tbl_values.u_name}, {self.tbl_values.password}, {self.tbl_values.phone_number}, {self.tbl_values.email}, {self.tbl_values.address}, {self.tbl_values.u_type}) VALUES('{user.tc}', '{user.first_name}', '{user.last_name}', '{user.user_name}', '{user.password}','{user.phone}','{user.email}','{user.address}','{user.user_type}')"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def update(self, user: User) -> None:
        """Veritabanındaki bir kullanıcının bilgilerini güncellemeyi sağlar.

        Args:
            user (User): kullanıcı bilgileri
        """
        self.query = f"UPDATE {self.tbl_values.users} SET {self.tbl_values.tc} = '{user.tc}', {self.tbl_values.name} = '{user.first_name}', {self.tbl_values.last_name} = '{user.last_name}', {self.tbl_values.u_name} = '{user.user_name}', {self.tbl_values.password} = '{user.password}', {self.tbl_values.phone_number} = '{user.phone}', {self.tbl_values.email} = '{user.email}', {self.tbl_values.address} = '{user.address}', {self.tbl_values.u_type} = '{user.user_type}' WHERE {self.tbl_values.id} = {user.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def get_user(self, u_id: int) -> User:
        """Veritabanından kullanıcı ismi ile bir kullanıcının verilerini getirmeyi sağlar.

        Args:
            id (int): kullanıcı id

        Returns:
            user: ilgili kullanıcının bilgileri
        """
        self.query = f"SELECT * FROM {self.tbl_values.users} WHERE {self.tbl_values.id} = '{u_id}'"

        user = User()
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            values = im.fetchall()

            for value in values:
                user.id = value[0]
                user.tc = value[1]
                user.first_name = value[2]
                user.last_name = value[3]
                user.user_name = value[4]
                user.password = value[5]
                user.phone = value[6]
                user.email = value[7]
                user.address = value[8]
                user.user_type = value[9]
            return user

    def get_user_id(self, user_name: str):
        """Veritabanından kullanıcı adı ile kullanıcının id bilgisini getirmeyi sağlar.

        Args:
            user_name (str): kullanıcı adı

        Returns:
            int: kullanıcı id
        """
        self.query = f"SELECT {self.tbl_values.id} FROM {self.tbl_values.users} WHERE {self.tbl_values.u_name} = '{user_name}'"
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            return im.fetchone()[0]

    def is_user(self, user: User) -> bool:
        """Kullanıcı adı ile kullanıcının veritabanına kayıtlı olup olmadığını kontrol etmeyi sağlar.

        Args:
            user (User): kullanıcı bilgileri

        Returns:
            bool: kayıt durumu
        """
        self.query = f"SELECT COUNT(*) as 'cnt' FROM {self.tbl_values.users} WHERE {self.tbl_values.u_name} = '{user.user_name}' OR {self.tbl_values.tc} = '{user.tc}'"

        count = 0
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            count = im.fetchone()[0]
        return count > 0

    def delete(self, user: User):
        """Veritabanından bir kullanıcıyı silmeyi sağlar.

        Args:
            user (User): kullanıcı verileri
        """
        self.query = f"DELETE FROM {self.tbl_values.users} WHERE {self.tbl_values.id} = {user.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def get_all_users(self, uname="") -> list[User]:
        """Veritabanındaki tüm kullanıcıları bir liste halinde verir.

        Returns:
            list[User]: kullanıcı listesi
        """
        self.query = (
            f"SELECT * FROM {self.tbl_values.users} WHERE {self.tbl_values.u_name} LIKE '%{uname}%' ORDER BY {self.tbl_values.u_name}"
        )

        user_list: list[User] = []
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            rows = im.fetchall()
            for row in rows:
                user: User = User()
                user.id = row[0]
                user.tc = row[1]
                user.first_name = row[2]
                user.last_name = row[3]
                user.user_name = row[4]
                user.password = row[5]
                user.phone = row[6]
                user.email = row[7]
                user.address = row[8]
                user.user_type = row[9]
                user_list.append(user)

        return user_list
