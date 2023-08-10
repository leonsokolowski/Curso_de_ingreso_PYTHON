import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K

1)
Un jugador de League of Legends tiene un fin de semana libre y va a jugar partidas hasta que se canse.
Para mejorar su jugabilidad, por cada partida jugada va a registrar:
- Modo de juego ("Normal", "Clasificatoria", "ARAM")
- Nombre del personaje que usó 
- La cantidad de asesinatos (No puede ser negativo)
- Muertes (No puede ser negativo)
- Asistencias. (No puede ser negativo, hasta 40)

De lo registrado, al jugador le interesa lo siguiente:

a) El modo de juego más jugado.
b) El personaje con el cual murió más.
c) El promedio de asistencias.
d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="LOL", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Datos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_mostrar_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los datos
        self.lista_de_modos_de_juego = ["normal", "aram", "clasificatoria", "aram", "normal", "normal"]
        self.lista_nombres_de_personajes = ["Yasuo", "Neeko", "Skarner", "Lux", "Lulu", "Yone"]
        self.lista_cantidades_de_asesinatos = [3, 10, 20, 13, 3, 25]
        self.lista_cantidades_de_muertes = [10, 3, 2, 7, 8, 1]
        self.lista_cantidades_de_asistencias = [6, 9, 10, 2, 26, 0]
        
        
    def btn_cargar_datos_on_click(self):
        continuar = True
        while continuar == True:
            
            modo_de_juego = prompt(None, "Ingrese el modo de juego jugado: Normal, Clasificatoria o ARAM")
            while modo_de_juego == None or modo_de_juego == "" or (modo_de_juego.lower() != "normal" and modo_de_juego.lower() != "clasificatoria" and modo_de_juego.lower() != "aram"):
                alert("ERROR", "Modo de juego inválido, ingreselo devuelta")
                modo_de_juego = prompt(None, "Ingrese el modo de juego jugado: Normal, Clasificatoria o ARAM")
            self.lista_de_modos_de_juego.append(modo_de_juego)
            
            nombre_de_personaje = prompt(None, "Ingrese el nombre de los personajes que jugó")
            while nombre_de_personaje == None or nombre_de_personaje == "":
                alert("ERROR", "Nombre de personaje inválido, ingreselo devuelta")
                nombre_de_personaje = prompt(None, "Ingrese el nombre de los personajes que jugó")
            self.lista_nombres_de_personajes.append(nombre_de_personaje)
                
            cantidad_asesinatos = prompt(None, "¿Cuántos asesinatos logró? (No pueden ser menos que 0)")
            while cantidad_asesinatos == None or cantidad_asesinatos == "" or int(cantidad_asesinatos) < 0:
                alert("ERROR", "Cantidad de asesinatos inválida, ingresela devuelta")
                cantidad_asesinatos = prompt(None, "¿Cuántos asesinatos logró? (No pueden ser menos que 0)")
            cantidad_asesinatos = int(cantidad_asesinatos)
            self.lista_cantidad_de_asesinatos.append(cantidad_asesinatos)
            
            cantidad_muertes = prompt(None, "¿Cuántos veces murió? (No pueden ser menos que 0)")
            while cantidad_muertes == None or cantidad_muertes == "" or int(cantidad_muertes) < 0:
                alert("ERROR", "Cantidad de muertes inválida, ingresela devuelta")
                cantidad_muertes = prompt(None, "¿Cuántos veces murió? (No pueden ser menos que 0)")
            cantidad_muertes = int(cantidad_muertes)
            self.lista_cantidad_de_muertes.append(cantidad_muertes)
            
            cantidad_asistencias = prompt(None, "¿Cuántos asistencias logró? (No pueden ser menos que 0 ni más que 40)")
            while cantidad_asistencias == None or cantidad_asistencias == "" or int(cantidad_asistencias) < 0 or int(cantidad_asistencias) > 40:
                alert("ERROR", "Cantidad de asistencias inválida, ingresela devuelta")
                cantidad_asistencias = prompt(None, "¿Cuántos asistencias logró? (No pueden ser menos que 0 ni más que 40)")
            cantidad_asistencias = int(cantidad_asistencias)
            self.lista_cantidad_de_asistencias.append(cantidad_asistencias)
            
            
            
            continuar = question(None, "¿Jugó más partidas?")
    
    def btn_mostrar_mostrar_on_click(self):
        largo_de_listas = len(self.lista_de_modos_de_juego)
        #a
        acumulador_modo_normal = 0
        acumulador_modo_clasificatoria = 0
        acumulador_modo_aram = 0
        #b
        mayor_cantidad_muertes = None
        nombre_personaje_con_mas_muertes = None
        #c
        contador_cantidad_partidas = 0
        acumulador_asistencias = 0
        #d
        mayor_cantidad_asesinatos = None
        nombre_personaje_con_mas_asesinatos = None
        modo_partida_mas_asesinatos = None
        
                
        for i in range (largo_de_listas):
            
            modo_de_juego = self.lista_de_modos_de_juego[i]
            nombre_personaje = self.lista_nombres_de_personajes[i]
            cantidad_de_asesinatos = self.lista_cantidades_de_asesinatos[i]
            cantidad_de_muertes = self.lista_cantidades_de_muertes[i]
            cantidad_de_asistencias = self.lista_cantidades_de_asistencias[i]
            
            #a
            match(modo_de_juego):
                case "normal":
                    acumulador_modo_normal += 1
                case "clasificatoria":
                    acumulador_modo_clasificatoria += 1
                case "aram":
                    acumulador_modo_aram += 1
            
            #b
            if mayor_cantidad_muertes == None or mayor_cantidad_muertes < cantidad_de_muertes:
                nombre_personaje_con_mas_muertes = nombre_personaje
                mayor_cantidad_muertes = cantidad_de_muertes
            
            #c
            contador_cantidad_partidas += 1
            acumulador_asistencias += cantidad_de_asistencias
            
            #d
            if mayor_cantidad_asesinatos == None or mayor_cantidad_asesinatos < cantidad_de_asesinatos:
                nombre_personaje_con_mas_asesinatos = nombre_personaje
                modo_partida_mas_asesinatos = modo_de_juego
                mayor_cantidad_asesinatos = cantidad_de_asesinatos
        
        #a
        if acumulador_modo_normal > acumulador_modo_clasificatoria and acumulador_modo_normal > acumulador_modo_aram:
            modo_mas_jugado = "Normal"
        elif acumulador_modo_clasificatoria > acumulador_modo_aram:
            modo_mas_jugado = "Clasificatoria"
        else:
            modo_mas_jugado = "ARAM"

        #c
        if contador_cantidad_partidas == 0:
            contador_cantidad_partidas = 1
        promedio_asistencias = acumulador_asistencias // contador_cantidad_partidas
        
        mensaje = f"El modo de juego más jugado fue {modo_mas_jugado}.\n\
                    El personaje con el que murió más fue {nombre_personaje_con_mas_muertes} con {mayor_cantidad_muertes} muertes.\n\
                    El promedio de asistencias es de {promedio_asistencias}\n\
                    El personaje con el que más asesinatos hizo fue {nombre_personaje_con_mas_asesinatos}, con {mayor_cantidad_asesinatos}. Fue en un {modo_partida_mas_asesinatos}"
        alert(None, mensaje)

        
        
        
        
        
            

                
            
            
            
            
                
        
 
if __name__ == "__main__":
    app = App()
    app.mainloop()