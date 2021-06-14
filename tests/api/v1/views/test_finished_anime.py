import json
import os
import unittest

from api.v1.app import app


class TestFinishedAnime(unittest.TestCase):
    new_anime = {
        'anime_name': 'naruto'
    }

    def setUp(self):
        from api.v1.storage import db

        self.app = app.test_client()

        db.create_all()

    def tearDown(self):
        os.remove('/tmp/test.db')

    def test_get_animes_empty_db(self):
        response = self.app.get('/api/v1/finished-anime/')

        want = []

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want, got)

    def test_post_anime_empty_db(self):
        response = self.app.post('/api/v1/finished-anime/', json=self.new_anime)

        want = {
            "is_published": False,
            "name": "naruto"
        }

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(want['is_published'], got['is_published'])
        self.assertEqual(want['name'], got['name'])

    def test_get_animes(self):
        self.app.post('/api/v1/finished-anime/', json=self.new_anime)

        response = self.app.get('/api/v1/finished-anime/')

        want = [
            {
                "is_published": False,
                "name": "naruto"
            }
        ]

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want[0]['is_published'], got[0]['is_published'])
        self.assertEqual(want[0]['name'], got[0]['name'])

    def test_get_anime(self):
        self.app.post('/api/v1/finished-anime/', json=self.new_anime)

        response = self.app.get('/api/v1/finished-anime/1')

        want = {
            "is_published": False,
            "name": "naruto"
        }

        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want['is_published'], got['is_published'])
        self.assertEqual(want['name'], got['name'])

    def test_put_anime(self):
        self.app.post('/api/v1/finished-anime/', json=self.new_anime)

        new_data = {
            'anime_name': 'naruto',
            "is_published": True,
        }

        self.app.put('/api/v1/finished-anime/1', json=new_data)

        response = self.app.get('/api/v1/finished-anime/')

        want = [
            {
                "is_published": True,
                "name": "naruto"
            }
        ]
        got = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(want[0]['is_published'], got[0]['is_published'])
        self.assertEqual(want[0]['name'], got[0]['name'])


if __name__ == '__main__':
    unittest.main()
