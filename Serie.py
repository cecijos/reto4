class Serie:

    def __init__(self,titulo,numerotemporadas,genero,creador):
        self._titulo=titulo
        self._numerotemporadas=numerotemporadas
        self._genero=genero
        self._creador=creador
        self._entregado=False

    def get_titulo(self):
        return self._titulo


    def get_genero(self):
        return self._genero

    def get_numerotemporadas(self):
        return self._numerotemporadas

    def get_creador(self):

     return self._creador


    def set_titulo(self):
        self._titulo=titulo

    def set_genero(self):
       self._genero=genero

    def set_numerotemporadas(self):
        self._numerotemporadas=numerotemporadas

    def set_creador(self):
       self._creador=creador

    def entregar(self):
         self._entregado = True

    def devolver(self):
       self._entregado = False

    def estado1(self):
        return self._entregado

    def __str__(self):
        cadena = "La serie con mas horas se llama " + self._titulo + " y es de " + self._genero + " dirigida  por " + self._creador
        return cadena

class Videojuego:

    def __init__(self,titulo,genero,horasestimadas,cia):
        self._titulo=titulo
        self._genero=genero
        self._horasestimadas=horasestimadas
        self._entregado=False
        self._cia=cia


    def get_titulo(self):
        return self._titulo
    def get_genero(self):
        return self._genero

    def get_horasestimadas(self):
        return self._horasestimadas

    def get_cia(self):
        return self._cia

    def set_titulo(self):
        self._titulo=titulo

    def set_genero(self):
       self._genero=genero

    def set_horasestimadas(self):
       self._horasestimadas=horasestimadas

    def set_cia(self):
        self._cia=cia

    def entregar(self):
        self._entregado = True

    def devolver(self):
        self._entregado = False

    def estado1(self):
        return self._entregado

    def __str__(self):
        cadena = "El juego con mas horas se llama " + self._titulo + " y es de " + self._genero + " perteneciente a " + self._cia
        return cadena


