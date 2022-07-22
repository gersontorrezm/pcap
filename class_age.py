class Persona:
    def __init__(self, nombre, edad, ci) -> None:
        self.__nom = nombre
        self.__ed = edad
        self.__c = ci        
        pass
    
    def _mostrar(self):
        print("\nSu nombre es: ", self.__nom)
        print("Su edad es: ", self.__ed)
        print("Su CI es: ", self.__c)
        
    def _esMayor(self):
        if self.__ed >= 18:
            return True
        else:
            return False
        
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ci = input("Ingrese su CI: ")

objeto = Persona(nombre, edad, ci)
objeto._mostrar()

if objeto._esMayor():
    print("\nEs mayor de edad")
else:
    print("\nEs menor de edad")
