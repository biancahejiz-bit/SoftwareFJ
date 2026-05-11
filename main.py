from cliente import Cliente
from servicio import ServicioSala
from servicio import ServicioEquipo
from servicio import ServicioAsesoria
from reserva import Reserva

print("OPERACION 1")
cliente1 = Cliente("Bianca", "123")
servicio1 = ServicioSala("Sala VIP", 50000, 2)
reserva1 = Reserva(cliente1, servicio1)
reserva1.confirmar_reserva()

print("\nOPERACION 2")
cliente2 = Cliente("", "456")
servicio2 = ServicioEquipo("Proyector", 30000, 3)
reserva2 = Reserva(cliente2, servicio2)
reserva2.confirmar_reserva()

print("\nOPERACION 3")
cliente3 = Cliente("Carlos", "")
servicio3 = ServicioAsesoria("Python", 80000, 2)
reserva3 = Reserva(cliente3, servicio3)
reserva3.confirmar_reserva()

print("\nOPERACION 4")
cliente4 = Cliente("Laura", "789")
servicio4 = ServicioSala("Sala Premium", 100000, 5)
reserva4 = Reserva(cliente4, servicio4)
reserva4.confirmar_reserva()

print("\nOPERACION 5")
cliente5 = Cliente("Pedro", "111")
servicio5 = ServicioEquipo("Camara", 0, 2)
reserva5 = Reserva(cliente5, servicio5)
reserva5.confirmar_reserva()

print("\nOPERACION 6")
cliente6 = Cliente("Andres", "222")
servicio6 = ServicioAsesoria("Java", 70000, 3)
reserva6 = Reserva(cliente6, servicio6)
reserva6.confirmar_reserva()

print("\nOPERACION 7")
cliente7 = Cliente("", "")
servicio7 = ServicioSala("Sala Basica", 40000, 2)
reserva7 = Reserva(cliente7, servicio7)
reserva7.confirmar_reserva()

print("\nOPERACION 8")
cliente8 = Cliente("Maria", "333")
servicio8 = ServicioEquipo("Laptop", -10000, 2)
reserva8 = Reserva(cliente8, servicio8)
reserva8.confirmar_reserva()

print("\nOPERACION 9")
cliente9 = Cliente("Sofia", "444")
servicio9 = ServicioAsesoria("Redes", 90000, 0)
reserva9 = Reserva(cliente9, servicio9)
reserva9.confirmar_reserva()

print("\nOPERACION 10")
cliente10 = Cliente("David", "555")
servicio10 = ServicioSala("Sala Ejecutiva", 120000, 1)
reserva10 = Reserva(cliente10, servicio10)
reserva10.confirmar_reserva()
