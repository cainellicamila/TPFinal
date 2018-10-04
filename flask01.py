from flask import Flask, render_template, flash, request

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import urllib
import urllib.request
import urllib.parse
import json
from urllib.request import urlopen

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

        #print (form.errors)
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
            form.buscar(x)

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
        return render_template('InDirecc.html', form=form)

    def get_coordinates(self, query, from_sensor=False):

        params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
            }

        url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.parse.urlencode(params)
        json_response = urllib.request.urlopen(url)
        response = json.loads(json_response.read())
        if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
            print (query, latitude, longitude)

        else:
            latitude, longitude = None, None
            print (query, "<no results>")

        return latitude, longitude


    def buscar (self, x):

        googleGeocodeUrl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
        termino = "&type="+ "restaurant"
        ubicacion = x
        APIKEY = '&key='+'AIzaSyAW6RodaGLs1B2EG9-2H7PED3GigrUvE6k'

        url = googleGeocodeUrl + ubicacion + termino + APIKEY
        print(url)

        url = googleGeocodeUrl + ubicacion + termino + APIKEY
        json_response = urllib.request.urlopen(url)
        busqueda = json_response.read().decode('utf-8')
        busquedajson = json.loads(busqueda)
        #i=0
        archivolugares = open('ubicacionr.csv','w')
        archivolugares.write('Nombre'+','+'Longitud'\
        +','+'Latitud'+','+'Direccion'+','+'\n')
        for lugar in busquedajson['results']:
            try:
                '''
                self.list.insert(i,lugar['name'])
                print(lugar['name'])
                i=+1
                self.list.insert(i,lugar['vicinity'])
                print(lugar['vicinity'])
                i=+1
                
                print(lugar['name'])
                print(lugar['geometry']['location'])
                print(lugar['formatted_address'])
                '''
                archivolugares.write(lugar['name']+','+str(lugar['geometry']['location']['lng'])\
                +','+str(lugar['geometry']['location']['lat'])+','+lugar['vicinity']+','+'\n')


            except KeyError as e:
                print(e)
                archivolugares.write(lugar['name']+','+str(lugar['geometry']['location']['lng'])\
                +','+str(lugar['geometry']['location']['lat'])+','+lugar['vicinity']+','+'\n')
        archivolugares.close()



if __name__ == "__main__":
    app.run()
