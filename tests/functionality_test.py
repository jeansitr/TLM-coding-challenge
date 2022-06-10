from urllib import response
from jsninjify import create_app

class TestRoute:
    app = create_app() 

class TestIndex(TestRoute):
    def test_get(self):
        # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.get('/')

            assert response.status_code == 200
            assert b"JS-Ninjify" in response.data
    
class TestNinjify(TestRoute):
    def test_get(self):
        # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.get('/ninjify?x=python')

            print(response.json)

            assert response.status_code == 200
            assert response.json['ninjaname'] is not None
    
    def test_bad_get(self):
        # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.get('/ninjify?x=asdfasdfa')

            print(response.json)

            assert response.status_code == 400
            assert response.json['error'] is not None

    def test_bad_get(self):
        # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.post('/ninjify')

            print(response.json)

            assert response.status_code == 501
            assert response.json['error'] is not None

class TestSecret(TestRoute):
    def test_get(self):
        # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.get('/secret')

            assert response.status_code == 200
            assert b"<b>code</b>" in response.data

    def test_get_bad_code(self):
         # Create a test client using the Flask application
        with self.app.test_client() as client:
            response = client.get('/secret?code=asdfasf')

            assert response.status_code == 200
            assert b"you weren't a ninja..." in response.data
        