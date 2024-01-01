from .db import db, environment, SCHEMA, add_prefix_for_prod

from sqlalchemy.schema import ForeignKey

class ForumPost(db.Model):
    __tablename__ = "forum_posts"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(), nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')))

    user = db.relationship('User', back_populates='posts')
    replies = db.relationship('Reply', back_populates='post', cascade="all, delete-orphan")

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'likes': self.likes
        }

        return data