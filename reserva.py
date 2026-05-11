from excepciones import ClienteInvalidoError

# Clase que representa una reserva en el sistema
class Reserva:

    # Constructor de la reserva
    def __init__(self, cliente, servicio):

        # Guardar el cliente asociado a la reserva
        self.cliente = cliente

        # Guardar el servicio asociado a la reserva
        self.servicio = servicio

        # Estado inicial de la reserva
        self.estado = "Pendiente"

    # Método para confirmar la reserva
    def confirmar_reserva(self):

        try:

            # Validar que el cliente sea válido
            if self.cliente.nombre is None:
                raise ClienteInvalidoError("Cliente inválido")

            # Calcular costo del servicio
            costo = self.servicio.calcular_costo()

            # Validar que el costo sea válido
            if costo <= 0:
                raise ValueError("Costo inválido")

            # Cambiar estado de la reserva
            self.estado = "Confirmada"

            # Mostrar información de la reserva
            print("Reserva confirmada")
            print("Cliente:", self.cliente.nombre)
            print("Servicio:", self.servicio.nombre)
            print("Costo:", costo)

            # Guardar evento en archivo de logs
            with open("logs.txt", "a") as archivo:
                archivo.write("Reserva confirmada correctamente\n")

        except (ClienteInvalidoError, ValueError) as error:

            # Mostrar el error
            print("Error en la reserva:", error)

            # Cambiar estado a cancelada
            self.estado = "Cancelada"

            # Guardar error en logs
            with open("logs.txt", "a") as archivo:
                archivo.write(f"Error en reserva: {error}\n")

        finally:

            # Mensaje final siempre se ejecuta
            print("Proceso de reserva finalizado")
