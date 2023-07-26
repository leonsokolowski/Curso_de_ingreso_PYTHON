import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: León
apellido: Sokolowski
div: K

Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt(None, "Ingrese un número"))
        if numero == 2:
            mensaje = "Su número es primo"
        else:
            for i in range (2, numero, 1):
                resto = numero % i
                if resto != 0:
                    mensaje = "Su número es primo"
                else:
                    mensaje = "Su número no es primo"
                    break
        
        alert(None, mensaje)
            
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()