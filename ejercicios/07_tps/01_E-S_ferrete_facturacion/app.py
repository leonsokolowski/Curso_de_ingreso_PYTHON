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
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        importe_1 = int(self.txt_importe_1.get())
        importe_2 = int(self.txt_importe_2.get())
        importe_3 = int(self.txt_importe_3.get())
        total = importe_1 + importe_2 + importe_3
        mensaje = f"La suma del precio de sus 3 productos es de {total} pesos"
        alert(title= "E/S TP1", message= mensaje)
    def btn_promedio_on_click(self):
        importe_1 = int(self.txt_importe_1.get())
        importe_2 = int(self.txt_importe_2.get())
        importe_3 = int(self.txt_importe_3.get())
        promedio = (importe_1 + importe_2 + importe_3) / 3
        mensaje = f"El promedio del precio de sus 3 productos es de {promedio} pesos"
        alert(title= "E/S TP1", message= mensaje)
    def btn_total_iva_on_click(self):
        importe_1 = int(self.txt_importe_1.get())
        importe_2 = int(self.txt_importe_2.get())
        importe_3 = int(self.txt_importe_3.get())
        precio_total = importe_1 + importe_2 + importe_3
        iva = (precio_total * 21) / 100
        precio_total_mas_iva = precio_total + iva
        mensaje = f"El promedio del precio de sus 3 productos es de {precio_total_mas_iva} pesos"
        alert(title= "E/S TP1", message= mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()