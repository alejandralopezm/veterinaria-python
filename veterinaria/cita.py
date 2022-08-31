class cita:
#atributos
    fecha = '30/08/2022'
    hora='13:30'
    nombremascota = 'florecita'
    dueno = 'alejandra lopez'
    motivo = 'toma de muestra'

#metodos
    def agendarcita(self):
        print("agendar una cita para diagnoticas enfermedad en una mascota")

    def cancelarcita(self):
        print("la cita para diagnosticar  a la mascota ha sido cancelada")

    def reagendarcita (self):
        print("se reasigna una nueva cita para diagnosticar una mascota")

lacita = cita()
lacita.agendarcita()
lacita.cancelarcita()
lacita.reagendarcita()
