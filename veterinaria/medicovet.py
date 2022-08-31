class medico:
    nombre ='maria lopez'
    especialidad = 'rayos x'
    celular = '3215968974'
    id = '987654321'
    disponibilidad= True
#metodos
    def medicodisponible(self):
        return self.disponibilidad

    def medicodisponiblidad2(self):
        if self.medicodisponible():
            print("el medico no esta disponible")
        else:
            print("el medicoesta dispobibke")

    def identificacionmedico(self):
        print("el numero de ID esta vigente ")


medicovet = medico()
medicovet.medicodisponible()
medicovet.medicodisponiblidad2 = False