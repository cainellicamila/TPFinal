from Datos.datos01 import Consulta
from Datos.datos02 import DatosConsulta

class NegocioColsulta(object):

    def __init__(self):
        self.datos=DatosConsulta()


    def alta (self,con):
        try:
            self.datos.alta(con)
            print('Si')
            return True
        except:
            print('No')
            return False

    def cant_elecc(self,elecc):
        try:
            num = self.datos.cant_elecc(elecc)
            return num
        except:
            return None

    def todos (self):
        todos=self.datos.todos()
        return todos

    def borrar_todos(self):
        try:
            self.datos.borrar_todos()
            return True
        except:
            return False
