from utils import ingresar_vehiculos

# solicitar datos al usuario
print('===============================')
print('SISTEMA DE CONTROL DE VEHÍCULOS')
print('===============================')

c_vehiculos = input('Cuantos Vehiculos desea insertar:')
cant_vehiculos = int(c_vehiculos)

if cant_vehiculos >= 1:
    ingresar_vehiculos(cant_vehiculos)
    print('=================================')
else:
    print('Debes ingresar al menos un vehiculo te dicen!!!')