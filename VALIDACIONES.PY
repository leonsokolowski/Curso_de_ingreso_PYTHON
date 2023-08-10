import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #Alert: recibe 2 parametros 👉 titulo "title" y el mensaje "message"
        alert(title='alert' , message="Esto no anda, funciona") 
        
#-------------------------------------------------------------------------------------------------------------------------------------------------

#                                                        VALIDACIONES PARA PARCIAL

#   .lower() ---> Cualquier caracter que se ingrese será tomado como una minúscula.
#   .upper() ---> Cualquier caracter que se ingrese será tomado como una mayúscula.

#    Para validar a la negativa los tipos por ejemplo, ponemos "while tipo == None or tipo == "" or (tipo != "valor" and tipo != "valor"):"
#    Para validar a la positiva los tipos por ejemplo, ponemos "while tipo != None and tipo != "" and (tipo == "valor" or tipo == "valor"):"

    nombre = prompt(None, "aca_va_la_pregunta")
    while nombre == None or nombre == "":
        alert("ERROR", "Nombre inválido, ingreselo devuelta")
        nombre = prompt(None, "aca_va_la_pregunta")
    
    edad = prompt(None, "aca_va_la_pregunta")
    while edad == None or edad == "":
        alert("ERROR", "Edad inválida, ingresela devuelta")
        edad = prompt(None, "aca_va_la_pregunta")
    edad = int(edad)
    
    tipo = prompt(None, "aca_va_la_pregunta")
    while tipo == None or tipo == "" or (tipo.lower() != "" and tipo.lower() != ""):
        alert("ERROR", "Tipo inválido, ingreselo devuelta")
        tipo = prompt(None, "aca_va_la_pregunta")
     
#--------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()