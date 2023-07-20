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

Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:

1 -Nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx".

2 -Pedir la altura de la persona e informar si es bajo: menor a 140 cm, medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

3- Validar todos los datos.

4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

5- Una vez ingresada la cantidad se debe pedir por cada excursión 
el importe y el tipo de excursión (caminata  o vehículo). 
informar cual es el precio más caro, el más barato y el promedio

6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

'''

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):
        #1
        nombre = prompt("Ejercicio El tour", "Ingrese su nombre")
        while nombre == None or nombre.isdigit() or len(nombre) < 3: 
            alert("ERROR", "Ingrese un nombre valido")
            nombre = prompt("Ejercicio El tour", "Ingrese su nombre") 
        
        edad = prompt("Ejercicio El tour", "Ingrese su edad")
        while edad == None or not edad.isdigit():
            alert("ERROR", "Ingrese una edad valida")
            edad = prompt("Ejercicio El tour", "Ingrese su edad")
        else:
            edad = int(edad)
        
        genero = prompt("Ejercicio El tour", "Ingrese su género: 'M', 'F', 'Otro'")
        while genero == None or (genero != "M" and genero != "F" and genero != "Otro"):
            alert("ERROR", "Ingrese un género valida")
            genero = prompt("Ejercicio El tour", "Ingrese su género: 'M', 'F', 'Otro'")
            
        #2
        altura = (prompt("Ejercicio El tour", "Ingrese su altura en cm"))
        while altura == None or not altura.isdigit():
            alert("ERROR", "Ingrese una altura valida")
            altura = (prompt("Ejercicio El tour", "Ingrese su altura en cm"))
        else:
            altura = int(altura)
    
        if (altura < 140):
            mensaje_altura = "es bajo."
        elif (altura < 171):
            mensaje_altura = "es medio."
        elif (altura < 191):
            mensaje_altura = "es alto."
        else:
            mensaje_altura = "es muy alto"
        
        #4
        cantidad_exc = prompt("Ejercicio El Tour", "Ingrese cantidad de excursiones")
        while cantidad_exc == None or cantidad_exc.isalpha():
            cantidad_exc = prompt("Ejercicio El Tour", "Ingrese cantidad de excursiones")
        excursiones_int = int(cantidad_exc)
        
        #5
        contador_exc = 0
        
        precio_caro = None
        tipo_mas_caro = ""
        precio_barato = None
        tipo_mas_barato = ""
        promedio_precio = 0
        #6
        exc_caminata = 0
        exc_vehiculo = 0
        
        while contador_exc < excursiones_int:
            
            importe = prompt("Importe", "Ingrese su importe")
            while importe == None or importe.isdigit():
                importe = prompt("Importe", "Ingrese su importe")
            importe_int = int(importe)
            
            tipo_exc = prompt("Tipo de Excursión", "Ingrese el tipo de excursión")
            while tipo_exc != "caminata" or tipo_exc != "vehiculo":
                tipo_exc = prompt("Tipo de Excursión", "Ingrese el tipo de excursión")
            
            if precio_barato == None or importe_int < precio_barato:
                precio_barato = importe_int
                tipo_mas_barato = tipo_exc
        
            if precio_caro == None or importe_int > precio_caro:
                precio_caro = importe_int
                tipo_mas_caro = tipo_exc
            
            if tipo_exc == "caminata":
                exc_caminata += 1
            else:
                exc_vehiculo += 1    
            
            
            suma_precios = suma_precios + importe_int
            "actualizo el contador para seguir iterando de manera controlada"
            contador_exc += 1
   
        promedio_precio = suma_precios / excursiones_int
        
        if exc_caminata == exc_vehiculo:
            exc_seleccionada = f"Se seleccionó caminata y vehiculo la misma cantidad de veces"
        elif exc_caminata > exc_vehiculo:
            exc_seleccionada = "La excursión caminata fue más seleccionada que vehículo"
        else:
            exc_seleccionada = "La excursión vehículo fue más seleccionada que caminata"
        
        informe = f"La excursión más barata vale ${precio_barato} y es de tipo {tipo_mas_barato}\n\
            La excursión más cara vale ${precio_caro} y es de tipo {tipo_mas_caro}\n\
            El promedio de precios de las excursiones es de ${promedio_precio}\n\
            {exc_seleccionada}"
        mensaje= f"Usted es {nombre} tiene {edad} de edad y su género es {genero} y según su altura es {mensaje_altura}"
        
        alert("Ejercicio El tour", mensaje)
        alert("Informe", informe)
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()