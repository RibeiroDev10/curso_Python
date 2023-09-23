class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        # connection = Connection() - exemplo do que está acontecendo na linha abaixo
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

c1 = Connection.create_with_auth('Rafael', '1234')
print(c1.user, c1.password)