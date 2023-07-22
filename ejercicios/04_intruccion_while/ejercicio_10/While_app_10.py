import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: León
apellido: Sokolowski
div: K

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0
                
        while True:
            numero = prompt("", "Ingrese un número (Positivo, negativo o 0)")
            if numero == None or numero == "":
                break
            else:
                numero = int(numero)
                if numero == 0:
                    contador_ceros += 1
                elif numero > 0:
                    contador_positivos += 1
                    suma_positivos += numero
                else:
                    contador_negativos += 1
                    suma_negativos += numero
        
        if contador_positivos > contador_negativos:
            diferencia_positivos = contador_positivos - contador_negativos
            diferencia_str = f"Ingresó ({diferencia_positivos}) números positivos más que negativos."
        else:
            diferencia_negativos = contador_negativos - contador_positivos
            diferencia_str = f"Ingresó ({diferencia_negativos}) números negativos más que positivos."
            
        mensaje = f"Usted ingreso ({contador_ceros}) veces el número 0. Ingreso ({contador_positivos}) veces números positivos, que sumados dan {suma_positivos}. Ingreso ({contador_negativos}) veces números negativos, que sumados dan{suma_negativos}. {diferencia_str}"
        alert("Ejercicio While 10", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
