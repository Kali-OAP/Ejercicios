"Class and objects"

#A class it's a container to save objects, also we can use it to create a "model" to create other objects or classes
#Objets are just elements with functions

class Car:
    marca = ""
    modelo = 0
    placa = ""
    data = input("Insert the marca: ")
    marca = data
    data = input("Insert the model: ")
    modelo = data
    data = input("Insert the placa: ")
    placa = data

taxi = Car()
print(f"La marca del taxi es: {taxi.marca}")
print(f"El modelo del taxi es: {taxi.modelo}")
print(f"La placa del taxi es: {taxi.placa}")

