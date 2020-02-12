
from app_main import app
from tests import OhmTestCase


class DashboardTest(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/dashboard')
            assert "Ready to begin assessment" in response.data
            assert "Read the README.md file for further instructions" in response.data
            assert "Points:" in response.data
            assert "test@test.com" in response.data
            assert "Dashboard" in response.data
            assert "Community" in response.data
