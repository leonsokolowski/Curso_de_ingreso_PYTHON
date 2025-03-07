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
        #Lengh -> len() -> ESTO ES FEO (Pero lo vamos a usar)
        # largo_lista = len(self.lista_de_votos_por_candidato) 
        # for item in range (largo_lista):                     
        
        #For each
        #for cantidad_votos in self.lista_de_votos_por_candidato:  #<--- RECORRE CADA UNO DE LOS ELEMENTOS DE LA LISTA
        
        largo = len(self.lista_de_votos_por_candidato)
        mayor_cantidad_de_votos = None
        nombre_candidato_mayor_cantidad_de_votos = ''
        menor_cantidad_votos = None
        nombre_candidato_menor = ''
        edad_candidato_menor = 0
        acumulador_edades = 0
        acumulador_votos = 0
        
        for i in range(largo):
            #punto A
            if mayor_cantidad_de_votos == None or mayor_cantidad_de_votos < self.lista_de_votos_por_candidato[i]:
                mayor_cantidad_de_votos = self.lista_de_votos_por_candidato[i]
                nombre_candidato_mayor_cantidad_de_votos = self.lista_de_nombres[i]
            #punto A
            
            #punto B
            if menor_cantidad_votos == None or menor_cantidad_votos > self.lista_de_votos_por_candidato[i]:                  
                menor_cantidad_votos = self.lista_de_votos_por_candidato[i]
                edad_candidato_menor = self.lista_de_edades[i]
                nombre_candidato_menor = self.lista_de_nombres[i]
            #punto B
            
            #punto C
            acumulador_edades += self.lista_de_edades[i]
            #punto C
            
            #punto D
            acumulador_votos += self.lista_de_votos_por_candidato[i]
            #punto D
        
        #punto C
        promedio_edades = acumulador_edades / largo
        #punto C

        mensaje_salida = f'El nombre del candidato con mas votos es: {nombre_candidato_mayor_cantidad_de_votos}, con {mayor_cantidad_de_votos}. El nombre del candidato con menos votos es: {nombre_candidato_menor}, tiene {edad_candidato_menor} años de edad y obtuvo una cantidad de {menor_cantidad_votos}. El promedio de edad entre todos los candidatos es de: {promedio_edades}. El total de votos emitidos es de: {acumulador_votos}'
        
        print(mensaje_salida) 
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

        # #PUNTO A.
        # mayor_cantidad_votos = None 
        # nombre_candidato_mas_votos = ""
        
        # largo_lista_votos = len(self.lista_de_votos_por_candidato)
        
        # for i in range (largo_lista_votos):
        #     if mayor_cantidad_votos == None or mayor_cantidad_votos < self.lista_de_votos_por_candidato [i]:
        #         mayor_cantidad_votos = self.lista_de_votos_por_candidato [i]
        #         nombre_candidato_mas_votos = self.lista_de_nombres [i]
        
        # mensaje_a = f"El cantididato con mayor cantidad de votos es {nombre_candidato_mas_votos} con {mayor_cantidad_votos} votos."
        # print(mensaje_a)
        
        # #PUNTO B.
        # menor_cantidad_votos: None
        # nombre_candidato_menos_votos = ""
        # edad_candidato_menos_votos = 0
        
        # for j in range (largo_lista_votos):
        #     if menor_cantidad_votos == None or menor_cantidad_votos > self.lista_de_votos_por_candidato [j]:
        #         menor_cantidad_votos = self.lista_de_votos_por_candidato [j]
        #         edad_candidato_menos_votos = self.lista_de_edades [j]
        #         nombre_candidato_menos_votos = self.lista_de_nombres [j]
        
        # mensaje_b = f"El candidato con menor cantidad de votos es {nombre_candidato_menos_votos}, tiene {edad_candidato_menos_votos} y tuvo {menor_cantidad_votos} votos."
        # print(mensaje_b)
        
        # #PUNTO C.
        # acumulador_edades = 0
        # for k in range (largo_lista_votos):
        #     acumulador_edades += self.lista_de_edades [k]
        
        # promedio_edades = acumulador_edades // len(self.lista_de_edades)
        
        # mensaje_c = f"El promedio de edades es {promedio_edades}"
        # print(mensaje_c)
        
        # #PUNTO D.
        # acumulador_votos = 0
        
        # for l in range (largo_lista_votos):
        #     acumulador_votos += self.lista_de_votos_por_candidato
            
        # mensaje_d = f"La cantidad total de votos es de {acumulador_votos}"
        # print(mensaje_d)
