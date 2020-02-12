
from app_main import app
from tests import OhmTestCase


class Community(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Five of the most recent signups!" in response.data
            assert "Justin Bieber" in response.data
            assert "Elvis Presley" in response.data
            assert "+14086551234" in response.data
            assert "Chuck Norris" in response.data
            assert "+14086441234" in response.data
            assert "+14086441234" in response.data
