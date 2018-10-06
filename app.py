import urllib

from flask import Flask, render_template, flash, request

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import requests

import csv


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    direccion = StringField('Direccion:', validators=[validators.required()])


    @app.route("/", methods=['GET', 'POST'])
    def InDirecc():

        form = ReusableForm(request.form)

        if request.method == 'GET':
            return render_template('InDirecc.html', form=form)

        if request.method == 'POST':
            direccion = request.form['direccion']

            query = direccion + ', Rosario, Santa Fe, Argentina'
            query = query.encode('utf-8')
            y = form.get_coordinates(query)

            print(y[0],y[1])

            lat = str(y[0])

            lon = str(y[1])

            x = 'location=' + str(lat) + ',' + str(lon) + '&radius=500'
            print(x)
            '''
            if form.validate():
            # Save the comment here.
                flash('Direccion ingresada: ' + direccion + lat + lon)
            else:
                flash('All the form fields are required. ')
            '''
            if request.form['submit_button'] == 'Buscar Restaurants':
                y= 'restaurant'

            elif request.form['submit_button'] == 'Buscar Hospitales':
                y='hospital'

            else:
                y='supermarket'

            resultados = form.buscar(x, y)
            flash(lat+lon)

            with open('ubicacionr.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Nombre'])
                    flash(row['Nombre'])

            '''
            for lugar in z ['results']:
                try:
                    flash('Lugar='+ + lugar['name'] + lugar['formatted_address'])

                except KeyError:
                    flash('NADA')
            '''
            return render_template('InDirecc.html', form=form, resultados=resultados)

    def get_coordinates(self, query, from_sensor=False):

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

    def buscar(self, x, y):
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


if __name__ == "__main__":
    app.run()
