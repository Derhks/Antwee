from flask import abort, jsonify, make_response, Response
from flask_restful import reqparse, Resource

from models.anime import Anime
from models.anime_viewed import AnimeViewed
from utils.finished_anime_utils import RequestInfoAnime
from utils.utils import check_boolean_string


parser = reqparse.RequestParser()
parser.add_argument(
    'anime_name',
    type=str,
    required=True,
    help="anime name cannot be blank!"
)


class FinishedAnime(Resource):

    @staticmethod
    def get():
        """
            Retrieves the list of all anime viewed objects
            ---
            tags:
              - anime_viewed
            responses:
              200:
                description: List of all anime viewed
                schema:
                  type: object
                  example: [{
                    "name": "string",
                    "finished_at": "string",
                    "is_published": boolean
                  }]
        """
        all_finished_anime = AnimeViewed.query.all()
        list_anime_viewed = []

        for anime_viewed in all_finished_anime:
            list_anime_viewed.append(anime_viewed.to_dict())

        return make_response(jsonify(list_anime_viewed), 200)

    @staticmethod
    def post():
        """
            Create an anime viewed
            ---
            tags:
              - anime_viewed
            parameters:
              - in: body
                name: finished_anime
                description: The anime viewed to create.
                schema:
                  type: object
                  required:
                    - anime_name
                  properties:
                    anime_name:
                      type: string
                      description: name of the anime viewed
            responses:
              201:
                description: Anime viewed created
                schema:
                    type: object
                    example: {
                      "name": "string",
                      "finished_at": "string",
                      "is_published": boolean
                    }
              400:
                description: Bad request, something is missing
        """
        data = parser.parse_args()
        new_anime_viewed = AnimeViewed(
            anime_name=data['anime_name']
        )
        new_anime_viewed.save()

        info_anime = RequestInfoAnime(data['anime_name'])
        anime_data = info_anime.get()
        anime = Anime(
            canonical_title=anime_data['canonical_title'],
            synopsis=anime_data['synopsis'],
            rating=anime_data['rating'],
            image=anime_data['image'],
            anime_viewed_id=new_anime_viewed.id
        )
        anime.save()

        return make_response(jsonify(new_anime_viewed.to_dict()), 201)


class FinishedAnimeId(Resource):
    @staticmethod
    def get(anime_viewed_id):
        """
            Retrieve an anime viewed
            ---
            tags:
              - anime_viewed
            parameters:
              - in: path
                name: anime_viewed_id
                required: true
                type: integer
                description: The ID of the finished anime to return.
            responses:
                200:
                  description: An AnimeViewed object.
                  schema:
                    type: object
                    example: {
                      "name": "string",
                      "finished_at": "string",
                      "is_published": boolean
                    }
                400:
                  description: The specified anime viewed ID is invalid. Is not a number.
                404:
                  description: The anime viewed with the ID {anime_viewed_id} was not found.
        """
        if isinstance(anime_viewed_id, int):
            anime_viewed = AnimeViewed.query.filter_by(id=anime_viewed_id).first()

            if not anime_viewed:
                abort(Response(f'An anime viewed with the ID {anime_viewed_id} was not found.', 404))

            return make_response(jsonify(anime_viewed.to_dict()), 200)
        else:
            abort(Response(f'The specified anime viewed ID is invalid. Is not a number.', 400))

    @staticmethod
    def put(anime_viewed_id):
        """
            Updates a anime viewed
            ---
            tags:
              - anime_viewed
            parameters:
              - in: path
                name: anime_viewed_id
                required: true
                type: integer
                description: The ID of the anime viewed to update
              - in: body
                name: anime viewed
                description: The anime viewed data to update
                schema:
                  type: object
                  required:
                    - anime_name
                    - is_published
                  properties:
                    anime_name:
                      type: string
                      description: name of the anime viewed
                    is_published:
                      type: boolean
                      description: True o False
            responses:
                200:
                  description: A AnimeViewed object updated.
                  schema:
                    type: object
                    example: {
                      "anime_name": "string",
                      "finished_at": timestamp,
                      "is_published": boolean
                    }
                400:
                  description: The specified anime viewed ID is invalid. Is not a number.
                404:
                  description: An anime viewed with the ID {anime_viewed_id} was not found.
        """
        parser.add_argument('is_published', required=False)

        anime_viewed = None

        if isinstance(anime_viewed_id, int):
            anime_viewed = AnimeViewed.query.filter_by(id=anime_viewed_id).first()

            if not anime_viewed:
                abort(Response(f'An anime viewed with the ID {anime_viewed_id} was not found.', 404))
        else:
            abort(Response(f'The specified anime viewed ID is invalid. Is not a number.', 400))

        data = parser.parse_args()

        anime_viewed.anime_name = data['anime_name']
        anime_viewed.is_published = check_boolean_string(data['is_published'])

        anime_viewed.save()

        return make_response(jsonify(anime_viewed.to_dict()), 200)

    @staticmethod
    def delete(anime_viewed_id):
        """
            Delete an anime viewed
            ---
            tags:
              - anime_viewed
            parameters:
              - in: path
                name: anime_viewed_id
                required: true
                type: integer
                description: The ID of the anime viewed to delete.
            responses:
                200:
                  description: Anime viewed deleted.
                  schema:
                    type: dict
                    example: {}
                400:
                  description: The specified anime viewed ID is invalid. Is not a number.
                404:
                  description: The anime viewed with the ID {anime_viewed_id} was not found.
        """
        if isinstance(anime_viewed_id, int):
            anime_viewed = AnimeViewed.query.filter_by(id=anime_viewed_id).first()

            if not anime_viewed:
                abort(Response(f'The anime viewed with the ID {anime_viewed_id} was not found.', 404))

            anime_viewed.delete()

            return make_response(jsonify({}), 200)
        else:
            abort(Response(f'The specified anime viewed ID is invalid. Is not a number.', 400))
