# Clase que representa un cliente
class Cliente:

    # Constructor de la clase cliente
    def __init__(self, nombre, documento):

        try:

            # Validar que el nombre no esté vacío
            if nombre == "":
                raise ValueError("El nombre no puede estar vacío")

            # Validar que el documento no esté vacío
            if documento == "":
                raise ValueError("El documento no puede estar vacío")

            # Guardar datos del cliente
            self.nombre = nombre
            self.documento = documento

        except ValueError as error:

            # Mostrar mensaje de error
            print("Error:", error)

            # Asignar valores inválidos
            self.nombre = None
            self.documento = None

    # Método para mostrar los datos del cliente
    def mostrar_datos(self):

        if self.nombre is not None:

            print("Nombre:", self.nombre)
            print("Documento:", self.documento)

        else:

            print("No se pueden mostrar datos inválidos")
