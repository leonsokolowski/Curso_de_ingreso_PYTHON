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
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador = 0
        #1) como empieza
        #2) como se desarrolla
        #3) como finaliza
        
        while contador < 10:
            contador += 1
            alert("Ejercicio While 01", contador)
        
        # for i in range(11):
        #     alert("Ejercicio While 01", i)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()