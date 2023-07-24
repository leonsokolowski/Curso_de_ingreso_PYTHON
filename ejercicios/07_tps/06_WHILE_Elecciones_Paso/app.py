'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        continuar = True
        nombre = ""
        edad = 0
        cantidad_votos = 0
        cantidad_votos_maxima = None #a
        nombre_candidato_maximo = None #a
        cantidad_votos_minima = None #b
        nombre_candidato_minimo = None #b
        edad_candidato_minimo = None #b
        acumulador_edades = 0 #c
        contador_candidatos = 0 #c
        acumulador_votos = 0 #d
        
        while continuar == True:
            nombre = prompt ("Nombre candidato", "Ingrese el nombre")
            
            edad = int(prompt ("Edad del candidato", "Ingrese la edad"))
            while edad < 25:
                alert ("ERROR", "Edad incorrecta. Debe ser mayor a 25")
                edad = int(prompt ("Edad del candidato", "Ingrese la edad"))
            acumulador_edades += edad  #c
            
            cantidad_votos = int(prompt ("Cantidad de votos", "Ingrese la cantidad de votos"))
            while cantidad_votos < 0:
                alert("ERROR", "Cantidad de votos incorrecta. No puede ser menor a 0")
                cantidad_votos = int(prompt ("Cantidad de votos", "Ingrese la cantidad de votos"))
            acumulador_votos += cantidad_votos
            
            #c
            contador_candidatos += 1
             
            #a 
            if cantidad_votos_maxima == None or cantidad_votos_maxima < cantidad_votos:
                cantidad_votos_maxima = cantidad_votos
                nombre_candidato_maximo = nombre
            
            #b
            if cantidad_votos_minima == None or cantidad_votos_minima > cantidad_votos:
                cantidad_votos_minima = cantidad_votos
                nombre_candidato_minimo = nombre
                edad_candidato_minimo = edad
            
            continuar = question("", "¿Desea ingresar otro candidato?")     

        #c
        promedio_edades = acumulador_edades // contador_candidatos
        
        mensaje = f"El nombre del candidato con más votos es {nombre_candidato_maximo}.\n\
            El nombre del candidato con menos votos es {nombre_candidato_minimo}, tiene {edad_candidato_minimo} años.\n\
            El promedio de las edades de los candidato es de {promedio_edades} años.\n\
            El total de votos fue de {acumulador_votos}."
        
        print(mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()