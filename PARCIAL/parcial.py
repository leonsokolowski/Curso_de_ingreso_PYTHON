import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K

Un importante laboratorio nos contrató para realizar una pequeña app con el fin
de poder obtener algunos datos estadísticos relacionados al ingreso de sus pacientes.
Al momento de admitir a sus pacientes, el laboratorio exige que estos proporcionen ciertos
datos personales, los cuales la app tiene que validar, los datos son:
1) Nombre completo: Validar que no sea None.
2) Localidad: Validar que no se None.
3) Sexo: Validar "Masculino", "Femenino", "Otro".
4) Edad: Validar que no sea None, tampoco puede ser menor de 0.
5) Estudio a realizarse: Validar Hemograma, Coagulograma, Hepatograma, Urocultivo
Los precios de los estudios son fijos y solamente se ingresa 1 estudio por ingreso ya
que NO ES POSIBLE, de momento, realizar más de 1 determinación por ingreso al sistema,
los precios son los siguientes:
- Hemograma: 950$
- Coagulograma: 1050$
- Hepatograma: 1200$
- Urocultivo: 1800$
Con la información brindada al momento de dar de alta los pacientes, a través de una carga
indefinida de pacientes, la empresa necesita calcular:
A) El porcentaje de pacientes de cada género.
B) La localidad del paciente más joven de género femenino.
C) El nombre y sexo del paciente masculino más viejo.
D) El promedio de recaudación sobre el total facturado
Aclaraciones: El examen debe ser realizado en dos partes, la toma de datos y las
validaciones deben estar en el botón pedir datos y esos datos ser ingresados en sus
correspondientes listas. La lógica y la salida de datos debe estar realizada en el botón
mostrar, la salida de datos puede ser realizada utilizando las funciones print o alert
(la que más cómoda les quede) pero tiene que ser 1 solo mensaje concatenado, NO pueden ser
múltiples mensajes, alerts o prints. Las validaciones mínimas deben ser las mencionadas en el
ejercicio NO ES NECESARIO realizar más validaciones que las mencionadas, pero pueden
agregar más si así desean. 
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="CASCARA", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Datos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_datos_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Acá van las listas:
        self.lista_de_nombres_completos = []
        self.lista_de_localidades = []
        self.lista_de_sexos = []
        self.lista_de_edades = []
        self.lista_de_estudios = []
    def btn_cargar_datos_on_click(self):
        
        continuar = True
        
        while continuar == True:
            
            nombre_completo = prompt(None, "Ingrese su nombre completo")
            while nombre_completo == None or nombre_completo == "":
                alert("ERROR", "Nombre completo inválido, ingreselo devuelta")
                nombre_completo = prompt(None, "Ingrese su nombre completo")
            self.lista_de_nombres_completos.append(nombre_completo)
            
            localidad = prompt(None, "Ingrese su localidad")
            while localidad == None or localidad == "":
                alert("ERROR", "Localidad inválida, ingresela devuelta")
                localidad = prompt(None, "Ingrese su localidad")
            self.lista_de_localidades.append(localidad)
            
            sexo = prompt(None, "Sexo: masculino, femenino u otro")
            while sexo == None or sexo == "" or (sexo.lower() != "masculino" and sexo.lower() != "femenino" and sexo.lower() != "otro"):
                alert("ERROR", "Sexo inválido, ingreselo devuelta")
                sexo = prompt(None, "Sexo: masculino, femenino u otro")
            self.lista_de_sexos.append(sexo)
            
            edad = prompt(None, "Ingrese su edad")
            while edad == None or edad == "" or int(edad) < 0:
                alert("ERROR", "Edad inválida, ingresela devuelta")
                edad = prompt(None, "Ingrese su edad")
            edad = int(edad)
            self.lista_de_edades.append(edad)
            
            estudio = prompt(None, "¿Qué estudio se va a realizar? (Hemograma, Coagulograma, Hepatograma, Urocultivo)")
            while estudio == None or estudio == "" or (estudio.lower() != "hemograma" and estudio.lower() != "coagulograma" and estudio.lower() != "hepatograma" and estudio.lower() != "urocultivo"):
                alert("ERROR", "Estudio inválido, ingreselo devuelta")
                estudio = prompt(None, "¿Qué estudio se va a realizar? (Hemograma, Coagulograma, Hepatograma, Urocultivo)")
            self.lista_de_estudios.append(estudio)
          
            continuar = question(None, "¿Desea continuar?")
            
                
    def btn_mostrar_datos_on_click(self):
        
        largo_de_lista = len(self.lista_de_nombres_completos)
        #a
        contador_sexo_total = 0
        contador_sexo_masculino = 0
        contador_sexo_femenino = 0
        contador_sexo_otro = 0
        #b
        edad_femenino_mas_joven = None
        localidad_femenino_mas_joven = None
        #c
        edad_masculino_mas_viejo = None
        nombre_masculino_mas_viejo = None
        sexo_masculino_mas_viejo = None
        #d
        contador_importes_total = 0
        acumulador_importes_total = 0
        
        
        for i in range (largo_de_lista):
            nombre = self.lista_de_nombres_completos[i]
            localidad = self.lista_de_localidades[i]
            sexo = self.lista_de_sexos[i]
            edad = self.lista_de_edades[i]
            estudio = self.lista_de_estudios[i]
            
            #a
            contador_sexo_total += 1
            match(sexo):
                case "masculino":
                    contador_sexo_masculino += 1
                    #c
                    if edad_masculino_mas_viejo == None or edad_masculino_mas_viejo < edad:
                        nombre_masculino_mas_viejo = nombre
                        sexo_masculino_mas_viejo = sexo
                case "femenino":
                    contador_sexo_femenino += 1
                    #b
                    if edad_femenino_mas_joven == None or edad_femenino_mas_joven > edad:
                        localidad_femenino_mas_joven = localidad
                case "otro":
                    contador_sexo_otro += 1 
            
            #d
            contador_importes_total += 1
            match(estudio):
                case "hemograma":
                    acumulador_importes_total += 950 
                    
                    
                case "coagulograma":
                    acumulador_importes_total += 1050
                case "hepatograma":
                    acumulador_importes_total += 1200
                case "urocultivo":
                    acumulador_importes_total += 1800
    
        
        #a
        porcentaje_sexo_masculino = (contador_sexo_masculino * 100) / contador_sexo_total
        porcentaje_sexo_femenino = (contador_sexo_femenino * 100) / contador_sexo_total
        porcentaje_sexo_otro = (contador_sexo_otro * 100) / contador_sexo_total
        
        #d
        if contador_importes_total == 0:
            contador_importes_total = 1
        promedio_importes = acumulador_importes_total / contador_importes_total
        
        mensaje = f"Hay {porcentaje_sexo_masculino}% de pacientes masculinos, {porcentaje_sexo_femenino}% de pacientes femeninos y {porcentaje_sexo_otro}% de pacientes otro.\n\
                    La localidad de la paciente más joven es {localidad_femenino_mas_joven}\n\
                    El nombre del paciente mas viejo es {nombre_masculino_mas_viejo} y es del sexo {sexo_masculino_mas_viejo}.\n\
                    El promedio de recaudación es de {promedio_importes} pesos."
        alert(None, mensaje)
            
              
    
if __name__ == "__main__":
    app = App()
    app.mainloop()