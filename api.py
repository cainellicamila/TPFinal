import urllib
import requests

class api ():


    def get_coordinates(query, from_sensor=False):

        params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
            }

        url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAW6RodaGLs1B2EG9-2H7PED3GigrUvE6k&' + urllib.parse.urlencode(params)
        response = requests.get(url).json()
        if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
            print (query, latitude, longitude)

        else:
            latitude, longitude = None, None
            print (query, "<no results>")

        return latitude, longitude

    def buscar(x, y):
        googleGeocodeUrl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
        termino = "&type="+ y
        ubicacion = x
        APIKEY = '&key=AIzaSyAW6RodaGLs1B2EG9-2H7PED3GigrUvE6k'

        url = googleGeocodeUrl + ubicacion + termino + APIKEY
        print(url)

        url = googleGeocodeUrl + ubicacion + termino + APIKEY
        busquedajson = requests.get(url).json()

        resultados = []
        for b in busquedajson['results']:
            resultados.append((b['name'], b['vicinity']))

        return resultados
