from . import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String,nullable=False, unique=True)

    def __init__(self, data):
        print(type(data))
        self.name = data.get('name')
        self.age = int(data.get('age'))

    def __str__(self):
        return '[name = ' + self.name + ' age = ' + str(self.age) + ']'

    def __repr__(self):
        return '{}'.format(self.id)

    @staticmethod
    def fetchAll():
        return UserModel.query.all()

    @staticmethod
    def fetchByID(userId):
        return UserModel.query.get(userId)

    def save(self):
        db.session.add(self)
        db.session.commit()