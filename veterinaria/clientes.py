class cliente :
#atribustos clientes
    nombre = 'alejandra lopez'
    direccion = 'Carrera 16#, Av. Colombia #21B-38'
    tipomascota = 'canino'
    sexomascota = 'hembra'
    telefono = '3186987896'

# metodos
    def alimentarmascota(self):
        print("le doy commida a mi mascota a las 8:00 am")
    def revisaranimal(self):
        print("llevo a revisar mi mascota")

    def perdircita(self):
        print("pedir una cita para verificar la salud de mi mascota")

elcliente=cliente()
elcliente.alimentarmascota()
elcliente.revisaranimal()
elcliente.perdircita()