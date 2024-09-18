print("**** PROGRAMACION POO ****")
# definicion de clases
class Perro:
    # funciones de la clase
    def morder (self):
        print("el perro me mordio")
    def Datos_Perro(self,nombre,edad,color):
        print(f" Nombre: {nombre} \n edad: {edad} \n Color: {color}")


# zona de creacion de objeto
pitbull = Perro()



# zona de uso de objeto
pitbull.Datos_Perro("Bobi", 4 , "cafe")
pitbull.morder()