from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField
from api import api
from Datos.datos01 import Consulta
from Negocio.negocio import NegocioColsulta
import csv
from estadisticas import calcEst
from scipy import ndimage
from scipy import misc
import os

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):


    @app.route('/',  methods=['GET', 'POST'])

    def estad():
        form = ReusableForm(request.form)
        if request.method == 'GET':
            return render_template('Estadisticas.html', form=form)

        if request.method == 'POST':

            if request.form['button'] == 'Cant':
                if calcEst():

                    imag ='static/grafico.png'

                return render_template('Estadisticas.html', form=form, imageng=imag)

if __name__ == '__main__':
  app.run(port = 4998, debug=True)
