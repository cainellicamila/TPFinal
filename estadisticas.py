from Datos.datos01 import Consulta
from Negocio.negocio import NegocioColsulta
import pylab as pl
import matplotlib.pyplot as plt

def calcEst ():

    c = NegocioColsulta()

    todos=c.todos()
    for i in todos:
        print(i.id_consulta,'', i.eleccion)

    elecc1= 'hospital'
    elecc2= 'restaurant'
    elecc3= 'supermarket'

    print(c.cant_elecc(elecc1))
    print(c.cant_elecc(elecc2))
    print(c.cant_elecc(elecc3))
    cants=[c.cant_elecc(elecc1), c.cant_elecc(elecc2), c.cant_elecc(elecc3)]
    print(cants)

    labels = 'Hospitales', 'Restaurantes', 'Supermercados'
    colors = ['yellowgreen', 'lightcoral', 'lightskyblue']

    plt.title('Porcentaje de consultas por tipo:')
    plt.pie(cants, labels=labels, autopct= '%.1f%%', colors=colors, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.savefig('static/grafico.png')

    plt.show()

    plt.clf()

    return True

