# Importar herramientas para clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):

    # Constructor de la clase Servicio
    def __init__(self, nombre, precio):

        # Atributos del servicio
        self.nombre = nombre
        self.precio = precio

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self):

        pass
    

# Clase que representa el servicio de salas
class ServicioSala(Servicio):

    # Constructor de ServicioSala
    def __init__(self, nombre, precio, horas):

        # Heredar atributos de Servicio
        super().__init__(nombre, precio)

        # Guardar horas reservadas
        self.horas = horas

    # Método para calcular costo total
    def calcular_costo(self):

        return self.precio * self.horas



# Clase que representa alquiler de equipos
class ServicioEquipo(Servicio):

    # Constructor de ServicioEquipo
    def __init__(self, nombre, precio, dias):

        # Heredar atributos de Servicio
        super().__init__(nombre, precio)

        # Guardar días de alquiler
        self.dias = dias

    # Método para calcular costo total
    def calcular_costo(self):

        return self.precio * self.dias
    


# Clase que representa asesorías especializadas
class ServicioAsesoria(Servicio):

    # Constructor de ServicioAsesoria
    def __init__(self, nombre, precio, horas):

        # Heredar atributos de Servicio
        super().__init__(nombre, precio)

        # Guardar horas de asesoría
        self.horas = horas

    #Método para calcular costo total
    def calcular_costo(self):

        return self.precio * self.horas
