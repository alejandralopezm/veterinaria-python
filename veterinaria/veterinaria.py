class Veterinaria:
#atributos veterinaria
    nombre ='VETERINARIA SANA SANA'
    direccion = ' Cll14a #7a31'
    servicios =True
    serv1 = 'rayos x'
    serv2 = 'hospitalizacion'
    serv3 = 'toma de muestras '

#Metodos acciones que hace la clases veterinaria

    def atencionanimal(self):
      print("Respetar a los animales es una obligación")

    def operaranimales (self):
        print("en esta veterinaria se operantodo tipo de animal domenstico ")

    def rayosxanimal(self,):
        print("el animal necesita rayos x de las costillas")

mi_veterinaria =Veterinaria()
mi_veterinaria.atencionanimal()
mi_veterinaria.operaranimales()
mi_veterinaria.rayosxanimal()

