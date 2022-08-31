class mascota:
#atributos de a mascota
    nombremascota = 'florecita'
    peso = '16 kilos'
    edad = '1 año'
    enfermo = False
    dueno = 'alejandra lopez'
    tamanomascota = 'mediano '
    observacion = 'se ingresa a la mascota para que se apliquen las vacunas correspondientes '
#metodos

    def tipoenfermedad(self):
        print("el perro tiene una fractura en la pata derecha")

    def estadosalud(self):
        return self.enfermo

    def estadosalud2(self):
        if self.estadosalud():
            print("la mascota esta enferma ")
        else:
            print("la mascota no esta enferma")


mimascota = mascota()
mimascota.estadosalud()
mimascota.estadosalud2= True