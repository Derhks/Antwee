from flask import abort, jsonify, make_response, Response
from flask_restful import reqparse, Resource
from models.anime import Anime


parser = reqparse.RequestParser()
parser.add_argument(
    'canonical_title',
    type=str,
    required=True,
    help="canonical title cannot be blank!"
)
parser.add_argument(
    'synopsis',
    type=str,
    required=True,
    help="synopsis cannot be blank!"
)
parser.add_argument(
    'rating',
    type=str,
    required=True,
    help="rating cannot be blank!"
)
parser.add_argument(
    'image',
    type=str,
    required=True,
    help="image cannot be blank!"
)
parser.add_argument(
    'anime_viewed_id',
    type=int,
    required=True,
    help="anime_viewed_id cannot be blank!"
)


class Animes(Resource):

    @staticmethod
    def get():
        """
            Retrieves the list of all anime objects
            ---
            tags:
              - anime
            responses:
              200:
                description: List of all anime
                schema:
                  type: object
                  example: [{
                    "canonical_title": "string",
                    "synopsis": "string",
                    "rating": "string",
                    "image": "string"
                  }]
        """
        all_animes = Anime.query.all()
        list_animes = []

        for anime in all_animes:
            list_animes.append(anime.to_dict())

        return make_response(jsonify(list_animes), 200)

    @staticmethod
    def post():
        """
            Create an anime
            ---
            tags:
              - anime
            parameters:
              - in: body
                name: anime
                description: The anime to create.
                schema:
                  type: object
                  required:
                    - canonical_title
                    - synopsis
                    - rating
                    - image
                    - anime_viewed_id
                  properties:
                    canonical_title:
                      type: string
                      description: canonical title of the anime
                    synopsis:
                      type: string
                      description: synopsis of the anime
                    rating:
                      type: string
                      description: rating of the anime
                    image:
                      type: string
                      description: image link
                    anime_viewed_id:
                      type: integer
                      description: viewed anime id
            responses:
              201:
                description: Anime created
                schema:
                    type: object
                    example: {
                      "canonical_title": "string",
                      "synopsis": "string",
                      "rating": "string",
                      "image": "string"
                    }
              400:
                description: Bad request, something is missing
        """
        data = parser.parse_args()

        new_anime = Anime(
            canonical_title=data['canonical_title'],
            synopsis=data['synopsis'],
            rating=data['rating'],
            image=data['image'],
            anime_viewed_id=data['anime_viewed_id']
        )
        new_anime.save()

        return make_response(jsonify(new_anime.to_dict()), 201)


class AnimeId(Resource):
    @staticmethod
    def get(anime_id):
        """
            Retrieve an anime
            ---
            tags:
              - anime
            parameters:
              - in: path
                name: anime_id
                required: true
                type: integer
                description: The ID of the anime to return.
            responses:
                200:
                  description: An Anime object.
                  schema:
                    type: object
                    example: {
                      "canonical_title": "string",
                      "synopsis": "string",
                      "rating": "string",
                      "image": "string"
                    }
                400:
                  description: The specified anime ID is invalid. Is not a number.
                404:
                  description: The anime with the ID {anime_id} was not found.
        """
        if isinstance(anime_id, int):
            anime = Anime.query.filter_by(id=anime_id).first()

            if not anime:
                abort(Response(f'The anime with the ID {anime_id} was not found.', 404))

            return make_response(jsonify(anime.to_dict()), 200)
        else:
            abort(Response(f'The specified anime ID is invalid. Is not a number.', 400))

    @staticmethod
    def put(anime_id):
        """
            Updates an anime
            ---
            tags:
              - anime
            parameters:
              - in: path
                name: anime_id
                required: true
                type: integer
                description: The ID of the anime to update
              - in: body
                name: anime
                description: The anime data to update
                schema:
                  type: object
                  required:
                    - canonical_title
                    - synopsis
                    - rating
                    - image
                    - anime_viewed_id
                  properties:
                    canonical_title:
                      type: string
                      description: canonical title of the anime
                    synopsis:
                      type: string
                      description: synopsis of the anime
                    rating:
                      type: string
                      description: rating of the anime
                    image:
                      type: string
                      description: image link
                    anime_viewed_id:
                      type: integer
                      description: viewed anime id
            responses:
                200:
                  description: An Anime object updated.
                  schema:
                    type: object
                    example: {
                      "canonical_title": "string",
                      "synopsis": "string",
                      "rating": "string",
                      "image": "string"
                    }
                400:
                  description: The specified anime ID is invalid. Is not a number.
                404:
                  description: The anime with the ID {anime_id} was not found.
        """
        anime = None

        if isinstance(anime_id, int):
            anime = Anime.query.filter_by(id=anime_id).first()

            if not anime:
                abort(Response(f'An anime viewed with the ID {anime_id} was not found.', 404))
        else:
            abort(Response(f'The specified anime viewed ID is invalid. Is not a number.', 400))

        data = parser.parse_args()

        anime.canonical_title = data['canonical_title']
        anime.synopsis = data['synopsis']
        anime.rating = data['rating']
        anime.image = data['image']
        anime.anime_viewed_id = data['anime_viewed_id']

        anime.save()

        return make_response(jsonify(anime.to_dict()), 200)

    @staticmethod
    def delete(anime_id):
        """
            Delete an anime
            ---
            tags:
              - anime
            parameters:
              - in: path
                name: anime_id
                required: true
                type: integer
                description: The ID of the anime to delete.
            responses:
                200:
                  description: Anime deleted.
                  schema:
                    type: dict
                    example: {}
                400:
                  description: The specified anime ID is invalid. Is not a number.
                404:
                  description: The anime with the ID {anime_id} was not found.
        """
        if isinstance(anime_id, int):
            anime = Anime.query.filter_by(id=anime_id).first()

            if not anime:
                abort(Response(f'The anime with the ID {anime_id} was not found.', 404))

            anime.delete()

            return make_response(jsonify({}), 200)
        else:
            abort(Response(f'The specified anime ID is invalid. Is not a number.', 400))
