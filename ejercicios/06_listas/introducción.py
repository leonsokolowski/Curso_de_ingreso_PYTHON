import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre (validar que no sea None), la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Pedir Datos", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=6, pady=20, columnspan=2, sticky="nsew")
        
        self.lista_de_nombres = [] #<- solamente van a entrar nombres (strings validos)
        self.lista_de_edades = [] #<- solamente numeros enteros validos (mayor a 25 años)
        self.lista_de_votos_por_candidato = [] #<- solamente numeros enteros validos (mayor o igual a 0)
        
    def btn_validar_on_click(self):
        
        #aca pedimos los datos como siempre y los validamos normalmente
        nombre_ingresado = prompt(None, 'Ingrese su nombre')
        while nombre_ingresado is None or nombre_ingresado.isdigit():
            nombre_ingresado = prompt(None, 'Ingrese su nombre')
        #aca estamos insertando los datos pedidos en la lista que esta declarada en la app
        self.lista_de_nombres.append(nombre_ingresado)
        
        #aca pedimos los datos como siempre y los validamos normalmente
        edad_ingresada = prompt(None, 'Ingresa tu edad')
        while edad_ingresada == None or int(edad_ingresada) < 25:
            edad_ingresada = prompt(None, 'Ingresa tu edad')
        #aca estamos insertando los datos pedidos en la lista que esta declarada en la app          
        edad_ingresada = int(edad_ingresada)
        self.lista_de_edades.append(edad_ingresada)
        
        #aca pedimos los datos como siempre y los validamos normalmente        
        cantidad_votos_candidato = prompt(None, 'Ingrese la cantidad de votos del candidato')
        while cantidad_votos_candidato == None or int(cantidad_votos_candidato) < 0:
            cantidad_votos_candidato = prompt(None, 'Ingrese la cantidad de votos del candidato')
        #aca estamos insertando los datos pedidos en la lista que esta declarada en la app       
        cantidad_votos_candidato = int(cantidad_votos_candidato)
        self.lista_de_votos_por_candidato.append(cantidad_votos_candidato)
        

    def btn_mostrar_on_click(self):
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

