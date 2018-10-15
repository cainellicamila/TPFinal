import unittest
from flask_testing import TestCase
from app import app, ReusableForm
from flask import jsonify
@app.route("/ajax/")
def some_json():


    return jsonify(success=True)

class APITests(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

        return app

    def test_main_route_must_return_200(self):
        response = self.client.get("/")
        self.assertEquals(200, response.status_code)

    def test_direc(self):

        api=ReusableForm()
        query = 'Zeballos 1301' + ', Rosario, Santa Fe, Argentina'
        query = query.encode('utf-8')
        response=api.get_coordinates(query)
        self.assertIsNotNone(response)

    def test_buscar(self):

        api=ReusableForm()
        lat= '-32.9545096'
        lon= '-60.6430954999999'
        response=api.buscar(lat, lon)
        self.assertIsNotNone(response)






    '''
    def test_can_create_a_new_user(self):
        name = "test"
        lastname = "test123"
        data = '{"firstname":"%s", "lastname": "%s"}' %(name, lastname)

        response = self.client.get("/users")
        self.assertEquals(response.json["data"], [], "There is no users")

        response = self.client.post("/users", data=data, content_type='application/json')
        self.assertEquals(200, response.status_code)

        id_created = response.json['data']['id']

        # and works with a single record route
        response = self.client.get("/users/{0}".format(id_created))
        self.assertEquals(response.json['data']['id'], str(id_created))
        self.assertEquals(response.json['data']['firstname'], name)
        self.assertEquals(response.json['data']['lastname'], lastname)

    '''



if __name__ == '__main__':
    unittest.main()
