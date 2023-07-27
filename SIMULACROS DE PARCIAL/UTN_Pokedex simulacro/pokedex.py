import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K

# El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
# algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

Realizar:
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []
        self.lista_poder_pokemones = []
        self.lista_tipo_pokemones = []

    def btn_cargar_pokedex_on_click(self):
        
        for pokedex in range (10):
            
            nombre = prompt(None, "¿Quién es ese Pokemon?")
            while nombre == None or nombre == "":
                alert("ERROR", "Nombre inválido, vuelva a ingresarlo")
                nombre = prompt(None, "¿Quién es ese Pokemon?")
            self.lista_nombre_pokemones.append(nombre)
            
            tipo = prompt(None, "¿De qué tipo es este Pokemon?")
            tipo = tipo.lower()
            while tipo == None or tipo == "" or (tipo != "agua" and tipo != "tierra" and tipo != "psiquico" and tipo != "fuego" and tipo != "electrico"):
                alert("ERROR", "Tipo inválido, vuelva a ingresarlo.")
                tipo = prompt(None, "¿De qué tipo es este Pokemon?")
            self.lista_tipo_pokemones.append(tipo)
            
            poder = prompt(None, "Nivel de poder de este Pokemon:")
            while poder == None or poder == "" or int(poder) < 50 or int(poder) > 200:
                alert("ERROR", "Poder inválido, vuelva a ingresarlo.")
                poder = prompt(None, "Nivel de poder de este Pokemon:")
            poder= int(poder)
            self.lista_poder_pokemones.append(poder)
                
    
    def btn_mostrar_pokedex_on_click(self):
        
        largo_pokedex = len(self.lista_nombre_pokemones)
        #0
        contador_tipo_fuego = 0
        #1
        contador_tipo_electrico = 0
        #6 y 7
        contador_tipo_agua = 0
        contador_tipo_tierra = 0
        contador_tipo_psiquico = 0
        #2
        nombre_pokemon_mas_poderoso = None
        tipo_pokemon_mas_poderoso = None
        poder_pokemon_mas_poderoso = None
        #3
        nombre_pokemon_menos_poderoso = None
        tipo_pokemon_menos_poderoso = None
        poder_pokemon_menos_poderoso = None
        #4
        contador_pokemones_poder_mas_100 = 0
        #5
        contador_pokemones_poder_menos_100 = 0
        #8
        acumulador_poder_total = 0
        contador_total = 0
        #9
        acumulador_poder_electrico = 0
        contador_poder_electrico = 0
        
        for i in range (largo_pokedex):
            
            #0, 1, 6 y 7 y 9
            match(self.lista_tipo_pokemones[i]):
                case "fuego":
                    contador_tipo_fuego += 1
                case "electrico":
                    contador_tipo_electrico += 1
                    acumulador_poder_electrico += self.lista_poder_pokemones[i]
                    contador_poder_electrico += 1
                case "agua":
                    contador_tipo_agua += 1
                case "tierra":
                    contador_tipo_tierra += 1
                case "psiquico":
                    contador_tipo_psiquico += 1
                
            #2
            if poder_pokemon_mas_poderoso == None or poder_pokemon_mas_poderoso < self.lista_poder_pokemones[i]:
                nombre_pokemon_mas_poderoso = self.lista_nombre_pokemones[i]
                tipo_pokemon_mas_poderoso = self.lista_tipo_pokemones[i]
                poder_pokemon_mas_poderoso = self.lista_poder_pokemones[i]
            
            #3
            if poder_pokemon_menos_poderoso == None or poder_pokemon_menos_poderoso > self.lista_poder_pokemones[i]:
                nombre_pokemon_menos_poderoso = self.lista_nombre_pokemones[i]
                tipo_pokemon_menos_poderoso = self.lista_tipo_pokemones[i]
                poder_pokemon_menos_poderoso = self.lista_poder_pokemones[i]
            
            #4
            if self.lista_poder_pokemones[i] > 100:
                contador_pokemones_poder_mas_100 += 1
            #5
            else:
                contador_pokemones_poder_menos_100 += 1
            
            #6
            if contador_tipo_agua > contador_tipo_fuego and contador_tipo_agua > contador_tipo_tierra and contador_tipo_agua > contador_tipo_electrico and contador_tipo_agua > contador_tipo_psiquico:
                tipo_con_mas_pokemones = "Agua"
            elif contador_tipo_fuego > contador_tipo_tierra and contador_tipo_fuego > contador_tipo_electrico and contador_tipo_fuego > contador_tipo_psiquico:
                tipo_con_mas_pokemones = "Fuego"
            elif contador_tipo_tierra > contador_tipo_electrico and contador_tipo_tierra > contador_tipo_psiquico:
                tipo_con_mas_pokemones = "Tierra"
            elif contador_tipo_electrico > contador_tipo_psiquico:
                tipo_con_mas_pokemones = "Eléctrico"
            else:
                tipo_con_mas_pokemones = "Psiquico"
            
            #7
            if contador_tipo_agua < contador_tipo_fuego and contador_tipo_agua < contador_tipo_tierra and contador_tipo_agua < contador_tipo_electrico and contador_tipo_agua < contador_tipo_psiquico:
                tipo_con_menos_pokemones = "Agua"
            elif contador_tipo_fuego < contador_tipo_tierra and contador_tipo_fuego < contador_tipo_electrico and contador_tipo_fuego < contador_tipo_psiquico:
                tipo_con_menos_pokemones = "Fuego"
            elif contador_tipo_tierra < contador_tipo_electrico and contador_tipo_tierra < contador_tipo_psiquico:
                tipo_con_menos_pokemones = "Tierra"
            elif contador_tipo_electrico < contador_tipo_psiquico:
                tipo_con_menos_pokemones = "Eléctrico"
            else:
                tipo_con_menos_pokemones = "Psiquico"
            
            #8
            acumulador_poder_total += self.lista_poder_pokemones[i]
            contador_total += 1
        #8
        if contador_total == 0:
            contador_total = 1
        promedio_poder_total = acumulador_poder_total // contador_total
        
        #9
        if contador_poder_electrico == 0:
            contador_poder_electrico = 1
        promedio_poder_electrico = acumulador_poder_electrico // contador_poder_electrico
        
        
        mensaje = f"0) En la pokedex hay {contador_tipo_fuego} pokemones tipo fuego.\n\
                    1) En la pokedex hay {contador_tipo_electrico} pokemones tipo eléctrico.\n\
                    2) Con un poder de {poder_pokemon_mas_poderoso}, el pokemon más poderoso es {nombre_pokemon_mas_poderoso}, de tipo {tipo_pokemon_mas_poderoso}.\n\
                    3) Con un poder de {poder_pokemon_menos_poderoso}, el pokemon menos poderoso es {nombre_pokemon_menos_poderoso}, de tipo {tipo_pokemon_menos_poderoso}.\n\
                    4) Hay {contador_pokemones_poder_mas_100} pokemones con un poder mayor a 100\n\
                    5) Hay {contador_pokemones_poder_menos_100} pokemones con un poder menor a 100\n\
                    6) La mayoría de pokemones son del tipo {tipo_con_mas_pokemones}.\n\
                    7) La minoría de pokemones son del tipo {tipo_con_menos_pokemones}.\n\
                    8) El promedio de poder de todos los pokemones es de {promedio_poder_total}\n\
                    9) El promedio de poder de los pokemones de tipo electrico es de {promedio_poder_electrico}"
        alert("Modelo Parcial: Pokedex", mensaje)            
            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()