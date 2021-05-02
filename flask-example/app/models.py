from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

    def hash_password(self, password):
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
