from api.v1.storage import db
from datetime import datetime


class AnimeViewed(db.Model):
    __tablename__ = 'finished_anime'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    finished_at = db.Column(db.DateTime, nullable=False)
    is_published = db.Column(db.Boolean)

    def __init__(self, anime_name: str):
        self.name = anime_name
        self.finished_at = datetime.now()
        self.is_published = False

    def __repr__(self) -> str:
        return f'<Anime viewed: {self.canonical_title}>'

    def save(self) -> None:
        """save the current instance in the database"""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as Err:
            raise Err

    def delete(self) -> None:
        """delete the current instance from the database"""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as Err:
            raise Err

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'finished_at': self.finished_at,
            'is_published': self.is_published
        }
