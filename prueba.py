import tkinter as tk

def crear_ventana():
    ventana = tk.Toplevel()
    ventana.title("Ventana secundaria")
    etiqueta = tk.Label(ventana, text="¡Esta es una ventana secundaria!")
    etiqueta.pack(padx=20, pady=20)
    
    # Botón para cerrar la ventana secundaria
    boton_cerrar = tk.Button(ventana, text="Cerrar ventana", command=ventana.destroy)
    boton_cerrar.pack(pady=10)

def cerrar_ventana_actual():
    # Cierra la ventana actual (la ventana principal)
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana principal")

etiqueta_principal = tk.Label(root, text="¡Esta es la ventana principal!")
etiqueta_principal.pack(padx=20, pady=20)

# Botón para abrir la ventana secundaria
boton_abrir = tk.Button(root, text="Abrir ventana secundaria", command=crear_ventana)
boton_abrir.pack(pady=10)

# Botón para cerrar la ventana principal
boton_cerrar_principal = tk.Button(root, text="Cerrar ventana principal", command=cerrar_ventana_actual)
boton_cerrar_principal.pack(pady=10)

root.mainloop()
