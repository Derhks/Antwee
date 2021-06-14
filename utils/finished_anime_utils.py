import flask

from settings import URL_ANIMES, URL_MORE_DATA, ERROR_MESSAGE
from utils.utils import get


class RequestInfoAnime:
    anime_id = 0
    url = URL_ANIMES
    more_data = URL_MORE_DATA
    msg_error = ERROR_MESSAGE

    def __init__(self, anime: str):
        self.name = anime

    def search_anime_id(self, url: str) -> int:
        obtain_anime_data = get(url=url)
        next_page = True if 'next' in obtain_anime_data['links'] else False

        for idx in range(len(obtain_anime_data['data'])):
            slug = obtain_anime_data['data'][idx]['attributes']['slug']
            if slug == self.name:
                self.anime_id = obtain_anime_data['data'][idx]['id']
                break

        if next_page:
            if self.anime_id == 0:
                url_next_page = obtain_anime_data['links']['next']
                self.search_anime_id(url=url_next_page)

        return self.anime_id

    def get_anime_data(self, id_anime: int) -> dict:
        full_url = f'{self.url}/{id_anime}'

        return get(url=full_url)

    def get(self) -> dict:
        full_url = f'{self.url}?{self.more_data}'

        anime_number = self.search_anime_id(url=full_url)

        if anime_number == 0:
            flask.abort(404, self.msg_error)

        data = self.get_anime_data(id_anime=int(anime_number))

        return {
            'canonical_title': data['data']['attributes']['canonicalTitle'],
            'synopsis': data['data']['attributes']['synopsis'],
            'rating': data['data']['attributes']['averageRating'],
            'image': data['data']['attributes']['posterImage']['large']
        }
