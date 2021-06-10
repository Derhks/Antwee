from flasgger import Swagger
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


# Start of endpoint initialization
from api.v1.views.finished_anime import FinishedAnime, FinishedAnimeId
from api.v1.views.animes import Animes, AnimeId


api.add_resource(FinishedAnime, '/finished-anime/')
api.add_resource(FinishedAnimeId, '/finished-anime/<int:anime_viewed_id>')
api.add_resource(Animes, '/animes/')
api.add_resource(AnimeId, '/animes/<int:anime_id>')
# End of endpoint initialization


if __name__ == '__main__':
    app.run()
