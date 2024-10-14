# Ingresar vehiculos
def ingresar_vehiculos(cant_vehiculos):
    vehiculos =[]

    for item in range(cant_vehiculos):
        marca = input('Inserte la marca del automóvil:')
        modelo = input('Inserte el modelo:')
        num_ruedas = input('Inserte el número de ruedas:')
        velocidad = input('Inserte la velocidad en km/h:')
        cilindrada = input('Inserte el cilindraje en cc:')

        print(marca, modelo, num_ruedas, velocidad, cilindrada)
        a = [f'Datos del automovil {item +1}', marca, modelo, num_ruedas, velocidad, cilindrada]
        vehiculos.append(a)

    print("\nResultados finales:")
    for vehiculo in vehiculos:
        print(', '.join(map(str, vehiculo)))  # Mostrar sin comillas ni paréntesis

    return vehiculos