import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)
                
        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        apellido = prompt("TP 5", "Ingrese su apellido")
        while apellido == None or apellido == "" or apellido.isdigit():
            alert("ERROR", "Apellido inválido. Ingreselo devuelta.")
            apellido = prompt("TP 5", "Ingrese su apellido")

        edad = prompt("TP 5", "Ingrese su edad")
        while not (edad != None and edad != "" and (edad.isdigit() and (int(edad) > 17 and int(edad) < 91))):
            alert("ERROR", "Edad inválida. Ingresela devuelta")
            edad = prompt("TP 5", "Ingrese su edad")
        else:
            edad = int(edad)
            
        estado_civil = prompt("TP 5", "Ingrese su estado civil: soltero/a, casado/a, divorciado/a, viudo/a")
        while not(estado_civil != None and estado_civil != "" and estado_civil.isalpha() or estado_civil == "Soltero/a" or estado_civil == "Casado/a" or estado_civil == "Divorciado/a" or estado_civil == "Viudo/a"):
            alert("ERROR", "Estado civil inválido. Ingreselo devuelta")
            estado_civil = prompt("TP 5", "Ingrese su estado civil: soltero/a, casado/a, divorciado/a, viudo/a")
        
        numero_legajo = prompt("TP 5", "Ingrese su número de legajo")
        while not(numero_legajo != None and numero_legajo != "") or len(numero_legajo) > 4:
            alert("ERROR", "Número de legajo inválido. Ingreselo devuelta")
            numero_legajo = prompt("TP 5", "Ingrese su número de legajo")
            
        self.txt_apellido.delete(0, 150)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, 150)
        self.txt_edad.insert(0, edad)
        # self.combobox_tipo.delete(0,150)
        # self.combobox_tipo.insert(0, estado_civil)
        self.txt_legajo.delete(0, 150)
        self.txt_legajo.insert(0, numero_legajo)
            
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()