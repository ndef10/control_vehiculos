class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada 


class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puesto):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puesto = num_puesto 

    def __str__(self):
        return (f'Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc Puestos: {self.num_puesto}')

class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga 

    def __str__(self):
        return (f'Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas {self.velocidad} km/h, {self.cilindrada} cc Carga: {self.peso_carga} kg')


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo): #usar true o false para mejorar
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo
        
    
    def __str__(self):
        return (f'Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas Tipo: {self.tipo}')


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, nro_radio, cuadro, motor ): 
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.nro_radio = nro_radio
        self.cuadro = cuadro 
        self.motor = motor
    
    def __str__(self):
        return (f'Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas Tipo: {self.tipo}, {self.nro_radio}, {self.cuadro},{self.motor}')






  







# Verificar la relación  de instancias
def mostrar_relacion(motocicleta):

    if isinstance(motocicleta, Vehiculo):
        print(f'Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}') #true
    else:
        print(f'Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}')

    if isinstance(motocicleta, Automovil):
        print(f'Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}') #false
    else:
        print(f'Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}')

    if isinstance(motocicleta, AutomovilParticular):
        print(f'Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, AutomovilParticular)}') #false
    else:
        print(f'Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, AutomovilParticular)}')

    if isinstance(motocicleta, AutomovilCarga):
        print(f'Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, AutomovilCarga)}') #false
    else:
        print(f'Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, AutomovilCarga)}')

    if isinstance(motocicleta, Bicicleta):
        print(f'Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}') #true
    else:
        print(f'Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}')

    if isinstance(motocicleta, Motocicleta):
        print(f'Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}') #true
    else:
        print(f'Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}')

   


# ===============================
# instanciar y mostrar resultados
# ===============================
def mostrar_resultados():
    particular = AutomovilParticular('Ford', 'Fiesta', 4, 180, 500, 5)
    print(particular)
    carga = AutomovilCarga('Daft Trucks', 'G 38', 10, 120, 1000, 20000) 
    print(carga)
    bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'carrera')
    print(bicicleta)
    motocicleta = Motocicleta('BMW', 'F800s', 2, 'Deportiva', '2T', 'Doble Viga', 21)
    print(motocicleta)

    print('====================================')

    mostrar_relacion(motocicleta)

mostrar_resultados() 








































