from api.v1.storage import db


class Anime(db.Model):
    __tablename__ = 'animes'

    id = db.Column(db.Integer, primary_key=True)
    canonical_title = db.Column(db.Text, unique=True, nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    rating = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(255), unique=True, nullable=False)
    anime_viewed_id = db.Column(db.Integer, db.ForeignKey('finished_anime.id'), nullable=False, unique=True)

    def __init__(self, canonical_title: str, synopsis: str, rating: str, image: str, anime_viewed_id: int):
        self.canonical_title = canonical_title
        self.synopsis = synopsis
        self.rating = rating
        self.image = image
        self.anime_viewed_id = anime_viewed_id

    def __repr__(self):
        return f'<Anime: {self.canonical_title}>'

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
            'canonical_title': self.canonical_title,
            'synopsis': self.synopsis,
            'rating': self.rating,
            'image': self.image
        }
