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
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra = prompt("Ingrese letra", "Ingrese la letra U, T o N (en mayusculas)")
        
        while letra is not ("U" or "T" or "N"):
            alert("Error", "Tiene que ser la letra U, T o N en mayúsculas")
            letra = prompt("Ingrese letra", "Ingrese la letra U, T o N (en mayusculas)")        
        
        mensaje = f"Usted eligió la letra {letra}"
        alert("Ejercicio While 05", mensaje)
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()