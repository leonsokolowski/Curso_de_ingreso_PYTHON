'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        
        for i in range (11):
            
            nombre = prompt(None, "Ingrese su nombre")
            
            edad = int(prompt(None, "Ingrese su edad, debe ser mayor."))
            while not(edad >= 18):
                alert("ERROR", "Edad inválida, vuelva a ingresarla")
                edad = int(prompt(None, "Ingrese su edad"))
                
            genero = prompt(None, "Ingrese su género: M, F o NB.")
            while genero != "M" and genero != "F" and genero != "NB":
                alert("ERROR", "Género inválido, vuelva a ingresarlo")
                genero = prompt(None, "Ingrese su género")
                
            tecnologia = prompt(None, "Ingrese la tecnología que maneja: python, js o asp.net.")
            while tecnologia != "python" and tecnologia != "js" and tecnologia != "asp.net":
                alert("ERROR", "Tecnología inválida, vuelva a ingresarla")
                tecnologia = prompt(None, "Ingrese la tecnología que maneja")
            
            puesto = prompt(None, "Ingrese el puesto al que aspira: jr, ssr o sr.")
            while puesto != "jr" and puesto != "ssr" and puesto != "sr":
                alert("ERROR", "Puesto inválido, vuelva a ingresarlo")
                puesto = prompt(None, "Ingrese el puesto al que aspira: jr, ssr o sr.")
            
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()