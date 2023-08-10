# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    0
    
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    9
    
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    7
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        # self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        # self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        # self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 70, 90, 150, 80, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        largo_lista = len(self.lista_nombre_pokemones)
               
        for i in range (largo_lista):
            nombre = self.lista_nombre_pokemones[i]
            print(f"{i:5} {nombre:15}")
                        
    def btn_mostrar_informe_1(self):
        largo_lista = len(self.lista_nombre_pokemones)
        contador_pokemones_tipo_fuego_mas_100 = 0
        
        for i in range (largo_lista):
            if self.lista_tipo_pokemones[i] == "fuego":
                aumento = (self.lista_poder_pokemones[i] * 10) / 100
                poder_mas_aumento = self.lista_poder_pokemones[i] + aumento
                if poder_mas_aumento > 100:
                    contador_pokemones_tipo_fuego_mas_100 += 1
        
        mensaje_informe_1 = f"La cantidad de Pokemones tipo fuego cuyo poder de pelea con un 10% extra supera los 100 puntos es {contador_pokemones_tipo_fuego_mas_100}"
        print(mensaje_informe_1)
                
    def btn_mostrar_informe_2(self):
        largo_lista = len(self.lista_nombre_pokemones)
        acumulador_poder_psiquico = 0
        contador_pokemones_psiquicos = 0
        
        for i in range (largo_lista):
            
          if self.lista_tipo_pokemones[i] == "psíquico":
              acumulador_poder_psiquico += self.lista_poder_pokemones[i]
              contador_pokemones_psiquicos += 1
        
        if contador_pokemones_psiquicos == 0:
            contador_pokemones_psiquicos = 1
        promedio_poder_psiquico = acumulador_poder_psiquico // contador_pokemones_psiquicos
        
        mensaje_informe_2 = f"El promedio de poder de todos los Pokemones tipo psíquico es {promedio_poder_psiquico}."
        print(mensaje_informe_2)
        
    def btn_mostrar_informe_3(self):
        largo_lista = len(self.lista_nombre_pokemones)
        contador_tipo_fuego = 0
        contador_tipo_agua = 0
        contador_tipo_psiquico = 0
        
        for i in range (largo_lista):
            
            match(self.lista_tipo_pokemones[i]):
                case "fuego":
                    contador_tipo_fuego += 1
                case "agua":
                    contador_tipo_agua += 1
                case "psíquico":
                    contador_tipo_psiquico += 1
        
        if contador_tipo_fuego < contador_tipo_agua and contador_tipo_fuego < contador_tipo_psiquico:
            tipo_con_menos_pokemones = "Fuego"
        elif contador_tipo_agua < contador_tipo_psiquico:
            tipo_con_menos_pokemones = "Agua"
        else:
            tipo_con_menos_pokemones = "Psiquico"
        
        #ESTO SE PUEDE HACER UTILIZANDO LISTAS
        
        
        mensaje_informe_3 = f"El tipo de Pokemon con menos Pokemones es el tipo {tipo_con_menos_pokemones}."
        print(mensaje_informe_3)        
                
    def btn_cargar_pokedex_on_click(self):
        
        for i in range (10):
            
            nombre = prompt(None, "Ingrese el nombre de su Pokemon")
            while nombre == None or nombre == "":
                alert("ERROR", "Nombre inválido, ingreselo devuelta")
                nombre = prompt(None, "Ingrese el nombre de su Pokemon")
            self.lista_nombre_pokemones.append(nombre)
            
            tipo = prompt(None, "Ingrese el tipo de su Pokemon: agua, psiquico o fuego")
            tipo = tipo.lower()
            while tipo == None or tipo == "" or (tipo != "agua" and tipo != "psiquico" and tipo != "fuego"):
                alert("ERROR", "Tipo inválido, ingreselo devuelta")
                tipo = prompt(None, "Ingrese el tipo de su Pokemon: agua, psíquico o fuego")
            self.lista_tipo_pokemones.append(tipo)
            
            poder= prompt(None, "Ingrese el poder de su Pokemon: entre 50 y 200")
            while poder == None or poder == "" or int(poder) < 50 or int(poder) > 200:
                alert("ERROR", "Poder inválido, ingreselo devuelta")
                poder= prompt(None, "Ingrese el poder de su Pokemon: entre 50 y 200")
            poder = int(poder) 
            self.lista_poder_pokemones.append(poder)
        
      
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    