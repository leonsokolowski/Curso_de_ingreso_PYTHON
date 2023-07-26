import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
nombre:León
apellido:Sokolowski
div: K

Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera (se limita a 1 perrito por ingreso), se les pide: 
nombre, precio de la consulta (validar entre 500 y 2500$) raza: (validar entre caniche, ovejero, siberiano), edad (validar 0 a 15) y peso (entre 25 y 40 kilos) determinar:

a. el nombre y el peso del perro con más peso
b. el porcentaje de razas
c. la facturación en bruto de la veterinaria
d. si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos
e. si el mismo perro tiene múltiples ingresos se le hacen estos descuentos:
    2 ingresos 15% 
    3 a 5 ingresos 35%
    más de 5 ingresos 50%

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
        
        self.lista_de_nombres = ["Eva", "Lila", "Zoe", "Bobi", "Ichi"]
        self.lista_de_precios = [2500, 2200, 1000, 1500, 950]
        self.lista_de_razas = ["ovejero", "ovejero", "ovejero", "siberiano", "caniche"]
        self.lista_de_edades = [11, 9, 14, 6, 4]
        self.lista_de_pesos = [35, 39, 30, 27, 25]
        
        #"Eva", "Lila", "Zoe", "Bobi", "Ichi"
        #2500, 2200, 1000, 1500, 950
        #"ovejero", "ovejero", "ovejero", "siberiano", "caniche"
        #11, 9, 14, 6, 4
        #35, 39, 30, 27, 25
          
    def btn_validar_on_click(self):
        nombre = prompt(None, "Ingrese el nombre de su perro")
        while nombre == None or nombre == "":
            alert("ERROR", "Nombre inválido")
            nombre = prompt(None, "Ingrese el nombre de su perro")
        self.lista_de_nombres.append(nombre)
        
        precio_consulta = prompt(None, "Ingrese el precio de su consulta")
        while precio_consulta == None or precio_consulta == "" or float(precio_consulta) < 500 or float(precio_consulta) > 2500:
            alert("ERROR", "Precio inválido")
            precio_consulta = prompt(None, "Ingrese el precio de su consulta")
        precio_consulta = float(precio_consulta)
        self.lista_de_precios.append(precio_consulta)
        
        raza = prompt(None, "Ingrese la raza de su perro")
        while raza == None or raza == "" or (raza != "caniche" and raza != "ovejero" and raza != "siberiano"):
            alert("ERROR", "Raza inválida")
            raza = prompt(None, "Ingrese la raza de su perro")
        self.lista_de_razas.append(raza)
        
        edad = prompt(None, "Ingrese la edad de su perro")
        while edad == None or edad == "" or int(edad) < 1 or int(edad) > 16:
            alert("ERROR", "Edad inválida")
            edad = prompt(None, "Ingrese la edad de su perro")
        edad = int(edad)
        self.lista_de_edades.append(edad)
        
        peso = prompt(None, "Ingrese el peso de su perro")
        while peso == None or peso == "" or float(peso) < 25 or float(peso) > 40:
            alert("ERROR", "Peso inválido")
            peso = prompt(None, "Ingrese el perro de su peso")
        peso = float(peso)
        self.lista_de_pesos.append(peso)

    def btn_mostrar_on_click(self):
        
        cantidad_perros = len(self.lista_de_nombres)
        #a
        peso_mas_pesado = None
        nombre_perro_mas_pesado = ""
        #b
        contador_ovejeros = 0
        contador_caniches = 0
        contador_siberianos = 0
        #c
        facturacion_bruta = 0
        #e
        contador_nombres_repetidos = 1
             
        for i in range(cantidad_perros):
            
            #a
            if peso_mas_pesado == None or peso_mas_pesado < self.lista_de_pesos [i]:
                peso_mas_pesado = self.lista_de_pesos [i]
                nombre_perro_mas_pesado = self.lista_de_nombres [i]
            
            #b
            match(self.lista_de_razas[i]):
                case "ovejero":
                    contador_ovejeros += 1
                case "caniche":
                    contador_caniches += 1
                case "siberiano":
                    contador_siberianos += 1
            
            #c
            facturacion_bruta += self.lista_de_precios[i]
            
            #e
            # if [i] in self.lista_de_nombres:
            #     contador_nombres_repetidos += 1
            #     self.lista_de_precios [i] * 2
                
                
                
        
        #b
        porcentaje_ovejeros = contador_ovejeros / cantidad_perros * 100      
        porcentaje_caniches = contador_caniches / cantidad_perros * 100
        porcentaje_siberianos = contador_siberianos / cantidad_perros * 100 
        
        #d
        if facturacion_bruta >= 5000:
            iva = (facturacion_bruta * 21) / 100
            facturacion_final = facturacion_bruta - iva
            mensaje_facturacion_final = f"Tendrá una facturación final de {facturacion_final}"
        else:
            facturacion_final = facturacion_bruta
            mensaje_facturacion_final = f"Tendrá una facturación final de {facturacion_final}"
            
        # #e
        # if contador_nombres_repetidos < 1:
        #     descuento = (self.lista_de_precios [i] *15) / 100
        #     precio_con_descuento = self.lista_de_precios [i] - descuento
        # elif contador_nombres_repetidos > 2 and contador_nombres_repetidos < 6:
        #     descuento = (self.lista_de_precios [i] *35) / 100
        #     precio_con_descuento = self.lista_de_precios [i] - descuento
        # else:
        #     descuento = (self.lista_de_precios [i] *50) / 100
        #     precio_con_descuento = self.lista_de_precios [i] - descuento
        
        mensaje = f"El perro más pesado es {nombre_perro_mas_pesado} con {peso_mas_pesado}.\n\
            Hay un {porcentaje_ovejeros}% de ovejeros, un {porcentaje_caniches}% de caniches y un {porcentaje_siberianos}% de siberianos.\n\
            Tendrá una facturación bruta de {facturacion_bruta} pesos.\n\
            {mensaje_facturacion_final}"
                    
        alert("Veterinaria", mensaje)

 
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()