import json
import os
import unittest

from api.v1.app import app


class TestAnimes(unittest.TestCase):
    synopsis = "Raku Ichijou, a first-year student at Bonyari High School, " \
               "is the sole heir to an intimidating yakuza family."
    new_anime = {
        "anime_viewed_id": 1,
        "canonical_title": "Nisekoi",
        "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
        "rating": "76.84",
        "synopsis": synopsis
    }

    def setUp(self):
        from api.v1.storage import db

        self.app = app.test_client()

        db.create_all()

    def tearDown(self):
        os.remove('/tmp/test.db')

    def test_get_animes_empty_db(self):
        response = self.app.get('/api/v1/animes/')

        want = []

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)

    def test_post_anime_empty_db(self):
        response = self.app.post('/api/v1/animes/', json=self.new_anime)

        want = {
            "canonical_title": "Nisekoi",
            "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
            "rating": "76.84",
            "synopsis": "Raku Ichijou, a first-year student at Bonyari High School, "
                        "is the sole heir to an intimidating yakuza family."
        }

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(want, got)

    def test_get_animes(self):
        self.app.post('/api/v1/animes/', json=self.new_anime)

        response = self.app.get('/api/v1/animes/')

        want = [
            {
                "canonical_title": "Nisekoi",
                "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
                "rating": "76.84",
                "synopsis": "Raku Ichijou, a first-year student at Bonyari High School, "
                            "is the sole heir to an intimidating yakuza family."
            }
        ]

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)

    def test_get_anime(self):
        self.app.post('/api/v1/animes/', json=self.new_anime)

        response = self.app.get('/api/v1/animes/1')

        want = {
            "canonical_title": "Nisekoi",
            "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
            "rating": "76.84",
            "synopsis": "Raku Ichijou, a first-year student at Bonyari High School, "
                        "is the sole heir to an intimidating yakuza family."
        }

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)

    def test_put_anime(self):
        self.app.post('/api/v1/animes/', json=self.new_anime)

        new_data = {
            'anime_viewed_id': 1,
            "canonical_title": "Nisekoi",
            "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
            "rating": "83",
            "synopsis": "Raku Ichijou, a first-year student at Bonyari High School, "
                        "is the sole heir to an intimidating yakuza family."
        }

        response = self.app.put('/api/v1/animes/1', json=new_data)

        want = {
            "canonical_title": "Nisekoi",
            "image": "https://media.kitsu.io/anime/poster_images/7821/large.jpg?1597694867",
            "rating": "83",
            "synopsis": "Raku Ichijou, a first-year student at Bonyari High School, "
                        "is the sole heir to an intimidating yakuza family."
        }

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
