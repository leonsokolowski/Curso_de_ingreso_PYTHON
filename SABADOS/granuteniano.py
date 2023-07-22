import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
Nombre: León
Apellido: Sokolowski
Div: K

Cada televidente que vota deberá ingresar:

-Nombre del votante
-Edad del votante (debe ser mayor a 13)
-Género del votante (Masculino, Femenino, Otro)
-El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

A. El promedio de edad de las votantes de género Femenino 
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
C. Nombre del votante más joven qué votó a Gianni.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que debe dejar la casa (El que tiene más votos)

'''

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="GRAN UTENIANO", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):        
        #Entradas
        contador_femenino = 0
        acumulador_edad_femenino = 0
        contador_masculino = 0
        for a in range (0, 100, 1):
            nombre_votante = prompt("GRAN UTENIANO", "Ingrese su nombre")
            for index in range(0, 100, 1):
                        #inicio, fin, largo del paso
                if nombre_votante != None and nombre_votante != "" and nombre_votante.isalpha():
                    break    
                alert("ERROR", "Ingrese un nombre válido")
                nombre_votante = prompt("GRAN UTENIANO", "Ingrese su nombre") 
            
            edad = prompt("GRAN UTENIANO", "Ingrese su edad. Debe ser mayor a 13")
            for index in range(0, 100, 1):
                edad = int(edad)
                if edad != None and edad > 13:
                    break
                alert("ERROR", "Ingrese una edad válida")
                edad = prompt("GRAN UTENIANO", "Ingrese su edad. Debe ser mayor a 13")
                
            genero = prompt("GRAN UTENIANO", "Ingrese su genero: femenino, masculino u otro")
            for index in range(0, 100, 1):
                if genero == None or genero is not ("femenino" and "masculino" and "otro"):
                    alert("ERROR", "Ingrese un género válido")
                    genero = prompt("GRAN UTENIANO", "Ingrese su genero: femenino, masculino u otro")
                break     
                
            nombre_participante = prompt("GRAN UTENIANO", "Ingrese el nombre de quien quiere eliminar (Giovanni, Gianni o Facu)")
            for index in range(0, 100, 1):
                if nombre_participante == None or nombre_participante is not ("Giovanni" and "Gianni" and "Facu"):
                    alert("ERROR", "Ingrese un participante válido")
                    nombre_participante = prompt("GRAN UTENIANO", "Ingrese el nombre de quien quiere eliminar (Giovanni, Gianni o Facu)")
                break 
            
            match(genero):
                case "femenino":
                    contador_femenino += 1
                    acumulador_edad_femenino = acumulador_edad_femenino + edad
                case "masculino":
                    if edad > 24 and edad < 41 and nombre_participante == ("Giovanni" or "Facundo"):
                        contador_masculino += 1
                case "otro":
                    pass            
                    
            respuesta = question("Nominados", "¿Desea continuar?")
            if respuesta == False:
                break  
        
        #Procesos
        
        #A
        if contador_femenino == 0:
            promedio_edad_femenino = 0
        else:
            promedio_edad_femenino = acumulador_edad_femenino / contador_femenino
        mensaje = f"El promedio de edad de las votantes femeninas es de {promedio_edad_femenino}"
        alert("Promedio", mensaje)
        
        #B
        
        #Salidas
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()