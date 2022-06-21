from app import db

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_data = db.Column(db.Text, index=True, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('favourites', lazy=True))

    def __repr__(self):
        return '<Favourite %r>' % (self.id)
