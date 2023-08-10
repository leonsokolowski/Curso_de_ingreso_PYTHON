import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K

Una librería que se especializa en venta de libros importados desea calcular ciertas métricas en base a las ventas de sus productos.
Se ingresa de cada venta:
- Título del libro
- Género: (ciencia ficción , Drama , Terror)
- Material del libro (rústica , tapa dura)
- Importe (No pueden ser números negativos ni mayor a los 30000)

Se pide:   
                       	
a) El más barato de drama con su importe.
b) Del libro más barato, el título.
c) El importe promedio sobre el total
d) La cantidad de libros que sean de ciencia ficcion y cuesten menos de $700.
 
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Libreria", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Datos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_datos_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Acá van las listas:
        self.lista_de_titulos = ["Harry Potter", "Canción de Hielo y Fuego", "IT", "El psicoanalista", "EL resplandor"]
        self.lista_de_generos = ["ciencia ficción", "drama", "terror", "drama", "terror"]
        self.lista_de_materiales = ["rústica", "rústica", "tapa dura", "rústica", "tapa dura"]
        self.lista_de_importes = [25000, 10000, 6000, 8000, 6500]

    def btn_cargar_datos_on_click(self):
        continuar = True
        
        while continuar == True:
            
            titulo = prompt(None, "Título del libro:")
            while titulo == None or titulo == "":
                alert("ERROR", "titulo inválido, ingreselo devuelta")
                titulo = prompt(None, "Título del libro:")
            self.lista_de_titulos.append(titulo)
            
            genero = prompt(None, "Género del libro: ciencia ficción, drama o terror")
            while genero == None or genero == "" or (genero.lower() != "ciencia ficción" and genero.lower() != "drama" and genero.lower() != "terror"):
                alert("ERROR", "Genero inválido, ingreselo devuelta")
                genero = prompt(None, "Género del libro: ciencia ficción, drama o terror")
            self.lista_de_generos.append(genero)
            
            material_libro = prompt(None, "Material del libro: rústica o tapa dura.")
            while material_libro == None or material_libro == "" or (material_libro.lower() != "rústica" and material_libro.lower() != "tapa dura"):
                alert("ERROR", "Material del libro inválido, ingreselo devuelta")
                material_libro = prompt(None, "Material del libro: rústica o tapa dura.")
            self.lista_de_materiales.append(material_libro)
            
            importe = prompt(None, "Ingrese el importe: No puede ser ni negativo ni mayor a 30000")
            while importe == None or importe == "" or int(importe) < 0 or int(importe) > 30000:
                alert("ERROR", "Importe inválido, ingresela devuelta")
                importe = prompt(None, "Ingrese el importe: No puede ser ni negativo ni mayor a 30000")
            importe = int(importe)

            continuar = question(None, "¿Desea continuar?")
                
    def btn_mostrar_datos_on_click(self):
        largo_lista = len(self.lista_de_titulos)
        #a
        menor_importe_drama = None
        titulo_menor_importe_drama = None
        #b
        menor_importe = None
        titulo_libro_menor_importe = None
        #c
        contador_total = 0
        acumulador_importes = 0
        #d
        contador_libros_menor_de_700 = 0
        
        for i in range (largo_lista):
            titulo = self.lista_de_titulos[i]
            genero = self.lista_de_generos[i]
            importe = self.lista_de_importes[i]
        
            match(genero):
                case "drama":
                    #a
                    if menor_importe_drama == None or menor_importe_drama > importe:
                        menor_importe_drama = importe
                        titulo_menor_importe_drama = titulo
                case "ciencia ficción":
                    if importe < 700:
                        contador_libros_menor_de_700 += 1

            #b
            if menor_importe == None or menor_importe > importe:
                titulo_libro_menor_importe = titulo
            
            #c
            contador_total += 1
            acumulador_importes += importe
            
        #c
        if contador_total == 0:
            contador_total = 1
        promedio_importe = acumulador_importes // contador_total
        
            
            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()