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

    def test_buscarRestaurant(self):

        api=ReusableForm()
        x = 'location=' + '-32.9545096' + ',' + '-60.6430954999999' + '&radius=500'
        y = 'restaurant'
        response=api.buscar(x, y)
        self.assertIsNotNone(response)

    def test_buscarHospital(self):

        api=ReusableForm()
        x = 'location=' + '-32.9545096' + ',' + '-60.6430954999999' + '&radius=500'
        y = 'hospital'
        response=api.buscar(x, y)
        self.assertIsNotNone(response)

    def test_buscarSupermercado(self):

        api=ReusableForm()
        x = 'location=' + '-32.9545096' + ',' + '-60.6430954999999' + '&radius=500'
        y = 'supermarket'
        response=api.buscar(x, y)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
