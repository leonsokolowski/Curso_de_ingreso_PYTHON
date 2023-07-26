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
        #a
        contador_a = 0
        #b
        nombre_postulante_jr_menos_grande = None
        edad_jr_menos_grande = 0
        #c
        acumulador_edades_masculinas = 0
        acumulador_edades_femeninas = 0
        acumulador_edades_nb = 0
        contador_edades_masculinas = 0
        contador_edades_femeninas = 0
        contador_edades_nb = 0
        #d
        contador_python = 0
        contador_js = 0
        contador_asp_net = 0
        #e
        contador_total_generos = 0
        contador_masculinos = 0
        contador_femeninas = 0
        contador_nb = 0
        
        
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
            contador_total_generos += 1
                
            tecnologia = prompt(None, "Ingrese la tecnología que maneja: python, js o asp.net.")
            while tecnologia != "python" and tecnologia != "js" and tecnologia != "asp.net":
                alert("ERROR", "Tecnología inválida, vuelva a ingresarla")
                tecnologia = prompt(None, "Ingrese la tecnología que maneja")
            
            puesto = prompt(None, "Ingrese el puesto al que aspira: jr, ssr o sr.")
            while puesto != "jr" and puesto != "ssr" and puesto != "sr":
                alert("ERROR", "Puesto inválido, vuelva a ingresarlo")
                puesto = prompt(None, "Ingrese el puesto al que aspira: jr, ssr o sr.")
            
            #a
            if genero == "NB" and (tecnologia == "js" or tecnologia == "asp.net") and edad > 24 and edad < 41 and puesto == "ssr":
                contador_a += 1
            
            #c
            match(genero):
                case "M":
                    acumulador_edades_masculinas += edad
                    contador_edades_masculinas += 1
                    contador_masculinos += 1
                case "F":
                    acumulador_edades_femeninas += edad
                    contador_edades_femeninas += 1
                    contador_femeninas += 1
                case "NB":
                    acumulador_edades_nb += edad
                    contador_edades_nb += 1
                    contador_nb += 1
            
            #d
            match(tecnologia):
                case "python":
                    contador_python += 1
                case "js":
                    contador_js += 1
                case "asp.net":
                    contador_asp_net += 1
        
        #b
        if puesto == "jr" and edad_jr_menos_grande == None or edad_jr_menos_grande > edad:
            edad_jr_menos_grande = edad
            nombre_postulante_jr_menos_grande = nombre
        
        #c
        if contador_edades_masculinas == 0:
            contador_edades_masculinas = 1
        promedio_edades_masculinas = acumulador_edades_masculinas / contador_edades_masculinas
        
        if contador_edades_femeninas == 0:
            contador_edades_femeninas = 1
        promedio_edades_femeninas = acumulador_edades_femeninas / contador_edades_femeninas
        
        if contador_edades_nb == 0:
            contador_edades_nb = 1
        promedio_edades_nb = acumulador_edades_nb / contador_edades_nb
        
        #d
        if contador_python > contador_js and contador_python > contador_asp_net:
            tecnologia_mas_postulantes = f"La tecnología con más postulantes es phyton con {contador_python}"
        elif contador_js > contador_asp_net:
            tecnologia_mas_postulantes = f"La tecnología con más postulantes es js con {contador_js}"
        else:
            tecnologia_mas_postulantes = f"La tecnología con más postulantes es asp.net con {contador_asp_net}"
        
        #e
        porcentaje_postulantes_masculinos = (contador_masculinos / contador_total_generos) * 100
        porcentaje_postulantes_femininas = (contador_femeninas / contador_total_generos) * 100 
        porcentaje_postulantes_nb = (contador_nb / contador_total_generos) * 100
         
        mensaje = f"La cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr es de {contador_a}\n\
        El nombre del postulante Jr con menor edad es {nombre_postulante_jr_menos_grande}\n\
        El promedio de edades masculinas, femeninas y nb es de {promedio_edades_masculinas}, {promedio_edades_femeninas} y {promedio_edades_nb} respectivamente.\n\
        {tecnologia_mas_postulantes}\n\
        El porcentaje de postulantes masculinos, femeninos y nb es de {porcentaje_postulantes_masculinos}%, {porcentaje_postulantes_femininas}% y {porcentaje_postulantes_nb}% respectivamente."
        
        alert("TP 7", mensaje)
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()