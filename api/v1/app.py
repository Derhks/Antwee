from flasgger import Swagger
from flask import Flask, render_template
from flask_restful import Api


app = Flask(__name__)
api = Api(app, prefix='/api/v1/')
swagger = Swagger(app)


# Start of endpoint initialization
from api.v1.views.finished_anime import FinishedAnime, FinishedAnimeId
from api.v1.views.animes import Animes, AnimeId


api.add_resource(FinishedAnime, '/finished-anime/')
api.add_resource(FinishedAnimeId, '/finished-anime/<int:anime_viewed_id>')
api.add_resource(Animes, '/animes/')
api.add_resource(AnimeId, '/animes/<int:anime_id>')
# End of endpoint initialization

# Start Test
from models.anime import Anime


@app.route('/anime-list/', methods=['GET'], strict_slashes=False)
def anime_list():
    all_animes = Anime.query.all()
    list_animes = []

    for anime in all_animes:
        list_animes.append(anime.to_dict())

    return render_template('animes.html', list_animes=list_animes)
# End Test


if __name__ == '__main__':
    app.run()
