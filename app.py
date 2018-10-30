from flask import Flask, render_template, flash, request

from wtforms import Form, validators, StringField

from api import api

import csv


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    direccion = StringField('Ingrese direccion:', validators=[validators.required()])


    @app.route("/", methods=['GET', 'POST'])
    def InDirecc():

        form = ReusableForm(request.form)

        if request.method == 'GET':
            return render_template('InDirecc.html', form=form)

        if request.method == 'POST':
            direccion = request.form['direccion']

            query = direccion + ', Rosario, Santa Fe, Argentina'
            query = query.encode('utf-8')
            y = api.get_coordinates(query)

            print(y[0],y[1])

            lat = str(y[0])

            lon = str(y[1])

            x = 'location=' + str(lat) + ',' + str(lon) + '&radius=500'
            print(x)


            if request.form['submit_button'] == 'Buscar Restaurants':
                y= 'restaurant'

            elif request.form['submit_button'] == 'Buscar Hospitales':
                y='hospital'

            else:
                y='supermarket'

            resultados = api.buscar(x, y)
            flash(lat+lon)

            with open('ubicacionr.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Nombre'])
                    flash(row['Nombre'])


            return render_template('InDirecc.html', form=form, resultados=resultados)




if __name__ == "__main__":
    app.run()
