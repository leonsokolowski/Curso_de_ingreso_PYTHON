import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K

2)
Se desea desarrollar un programa que permita al usuario ingresar el nombre, 
año emitido (inferior al 2000 ,Superior a 2000 e inferior a 2015 y superior al 2015), 
si es online u offline y costo (500 a 10000) 10 videojuegos.

Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="VideoJuegos 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Datos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_mostrar_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los datos
        self.lista_nombres = ["Borderlands", "Overwatch", "Pokemon", "Doom", "Apex Legends"]
        self.lista_años_emicion = [2009, 2018, 1997, 2016, 2019]
        self.lista_tipos = ["offline", "online", "offline", "offline", "online"]
        self.lista_costos = [1500, 7000, 2000, 4000, 501]

    def btn_cargar_datos_on_click(self):
        
        for i in range (10):
            nombre = prompt(None, "Ingrese el nombre del videojuego.")
            while nombre == None or nombre == "":
                alert("ERROR", "Nombre inválido, ingreselo devuelta")
                nombre = prompt(None, "Ingrese el nombre del videojuego.")
            self.lista_nombres.append(nombre)
            
            año_emicion = prompt(None, "Ingrese el año de emisión")
            while año_emicion == None or año_emicion == "" or int(año_emicion) < 1970 or int(año_emicion) > 2024:
                alert("ERROR", "Año de emción inválido, ingreselo devuelta")
                año_emicion = prompt(None, "Ingrese el año de emisión")
            año_emicion = int(año_emicion)
            self.lista_años_emicion.append(año_emicion)
            
            tipo = prompt(None, "Ingrese si es online u offline")
            while tipo == None or tipo == "" or tipo != "online" or tipo != "offline":
                alert("ERROR", "Tipo inválido, ingreselo devuelta.")
                tipo = prompt(None, "Ingrese si es online u offline")
            self.lista_tipos.append(tipo)

            costo = prompt(None, "Ingrese el costo del videojuego")
            while costo == None or costo == "" or int(costo) < 500 or int(costo) > 10000:
                alert("ERROR", "Costo inválido, ingreselo devuelta")
                costo = prompt(None, "Ingrese el costo del videojuego")
            costo = int(costo)
            self.lista_costos.append(costo)        
    
    def btn_mostrar_mostrar_on_click(self):
        largo_lista = len(self.lista_nombres)
        #a
        costo_videojuego_mas_caro = None
        costo_videojuego_mas_barato = None
        nombre_videojuego_mas_caro = None
        nombre_videojuego_mas_barato = None
        #b
        acumulador_costos_online = 0
        contador_juegos_online = 0
        #c
        costo_videojuego_mas_caro_pre_2015 = 0
        costo_videojuego_mas_barato_pre_2015 = 0
        nombre_videojuego_mas_caro_pre_2015 = 0
        nombre_videojuego_mas_barato_pre_2015 = 0
        #d
        contador_cantidad_total = 0
        contador_juegos_offline = 0
        #e
        contador_juegos_post_2015 = 0
        contador_juegos_pre_2015_post_2000 = 0
        contador_juegos_pre_2000 = 0
        
        for i in range (largo_lista):
            
            #d
            contador_cantidad_total += 1
            #a
            if costo_videojuego_mas_caro == None or costo_videojuego_mas_caro < self.lista_costos[i]:
                costo_videojuego_mas_caro = self.lista_costos[i]
                nombre_videojuego_mas_caro = self.lista_nombres[i]
            
            if costo_videojuego_mas_barato == None or costo_videojuego_mas_barato > self.lista_costos[i]:
                costo_videojuego_mas_barato == self.lista_costos[i]
                nombre_videojuego_mas_barato = self.lista_nombres[i]
            
            #b y d
            match(self.lista_tipos[i]):
                case "online":
                    acumulador_costos_online += self.lista_costos[i]
                    contador_juegos_online += 1
                case "offline":
                    contador_juegos_offline += 1
            
            #c
            if self.lista_años_emicion[i] > 2015:
                pass
            else:
                if costo_videojuego_mas_caro_pre_2015 == None or costo_videojuego_mas_caro_pre_2015 < self.lista_costos[i]:
                    costo_videojuego_mas_caro_pre_2015 = self.lista_costos[i]
                    nombre_videojuego_mas_caro_pre_2015 = self.lista_nombres[i]
                if costo_videojuego_mas_barato_pre_2015 == None or costo_videojuego_mas_barato_pre_2015 > self.lista_costos[i]:
                    costo_videojuego_mas_barato_pre_2015 = self.lista_costos[i]
                    costo_videojuego_mas_barato_pre_2015 = self.lista_nombres[i]
            
            #d
            if self.lista_años_emicion[i] > 2015:
                contador_juegos_post_2015 += 1
            elif self.lista_años_emicion[i] > 2000:
                contador_juegos_pre_2015_post_2000 += 1
            else:
                contador_juegos_pre_2000 += 1
                
                            
        #b
        if contador_juegos_online == 0:
            contador_juegos_online = 1
        promedio_costos_online = acumulador_costos_online // contador_juegos_online
        
        #d
        porcentaje_juegos_offline = (contador_juegos_offline / contador_cantidad_total) * 100
        
        #e
        if contador_juegos_post_2015 > contador_juegos_pre_2015_post_2000 and contador_juegos_post_2015 > contador_juegos_pre_2000:
            periodo_con_mas_juegos = "post 2015"
        elif contador_juegos_pre_2015_post_2000 > contador_juegos_pre_2000:
            periodo_con_mas_juegos = "post 2000, pre 2015"
        else:
            periodo_con_mas_juegos = "pre 2000"
        
        mensaje = f"El videojuego más caro es {nombre_videojuego_mas_caro} ({costo_videojuego_mas_caro} pesos) y el más barato es {nombre_videojuego_mas_barato}({costo_videojuego_mas_barato} pesos).\n\
        El promedio de los costos de los videojuegos online es de {promedio_costos_online} pesos.\n\
        El videojuego más caro emitido antes de 2015 es {nombre_videojuego_mas_caro_pre_2015} ({costo_videojuego_mas_caro_pre_2015} pesos) y el más barato es {nombre_videojuego_mas_barato_pre_2015}({costo_videojuego_mas_barato_pre_2015} pesos).\n\
        Los videojuegos offline ingresados son un {porcentaje_juegos_offline}% del total de videojuegos ingresados\n\
        El periodo de tiempo con más video juegos ingresados es el de {periodo_con_mas_juegos}."
        print(mensaje)
        #alert(None, mensaje)
        
            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()