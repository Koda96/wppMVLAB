import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title = "Seleccionar informe PDF",
        filetypes = [("Archivos PDF", "*.pdf"), ("Todos los archivos", "*.*")]
    )
    
    if file_path:
        print("Archivo seleccionado: {}".format(file_path))
        return file_path
    else:
        print("No se selecciono ningun archivo")
        return None
    
ruta_archivo = seleccionar_archivo()