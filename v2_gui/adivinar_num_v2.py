import tkinter as tk
from tkinter import messagebox
import random as r

contador_intentos = 3

def generar_lista():
    global contador_intentos
    try:
        valor_entrada=entrada_cantidad.get()
        x=int(valor_entrada)
        while True:
            if x<3:
                messagebox.showwarning("Atención", "Ingresar un número mayor a 3 ⚠")
                return
            else:
                break
        datos=list()
        while len(datos)<x:
            num=r.randint(1,101)
            if num not in datos:
                datos.append(num)
        datos.sort()
        messagebox.showinfo("Lista generada", "¡A jugar! ✅")
        contador_intentos=3
        etiqueta_vidas.config(text=f"Vidas: {contador_intentos}❤")
        etiqueta_lista.config(text=f"Opciones: {datos}",fg="black")
        entrada_adivina.config(state="normal")
        boton_verificar.config(state="normal")        
        global numero_secreto
        numero_secreto = r.choice(datos)
    except ValueError as e:
        messagebox.showerror("Error", f"Ingresar un valor valido ❌")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error inesperado: {e} ❌")

def comprobar_suerte():
    global contador_intentos
    try:
        respuesta=entrada_adivina.get()
        respuesta=int(respuesta)
        if respuesta < numero_secreto:
            messagebox.showinfo("¡Pista!", "¡Demasiado bajo!⚠")
        elif respuesta > numero_secreto:
            messagebox.showinfo("¡Pista!", "¡Demasiado alto!⚠")
        elif respuesta == numero_secreto:
            messagebox.showinfo("¡Felicidades!", f"¡El número {respuesta} es correcto! Has ganado 🏆")
            etiqueta_lista.config(text="GANASTE ✅🚬", fg="green")
            entrada_adivina.config(state="disabled")
            boton_verificar.config(state="disabled")
        contador_intentos-=1
        etiqueta_vidas.config(text=f"Vidas: {contador_intentos} ❤")
        if contador_intentos == 0:
            messagebox.showwarning("¡Perdiste!", f"Tus vidas se han agotado, el número correcto era: {numero_secreto}💥")
            etiqueta_lista.config(text="JUEGO TERMINADO ❌", fg="red")
            entrada_adivina.config(state="disabled")
            boton_verificar.config(state="disabled")
    except ValueError as e:
        messagebox.showerror("Error", f"Ingresar un valor valido ❌")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error inesperado: {e} ❌")

#Definir ventana
ventana= tk.Tk()
ventana.title("Adivina el Número - Paul Edition")
ventana.geometry("400x400")

#Etiquetas:
instrucciones=tk.Label(ventana, text="Ingresar un número mayor o igual a 3:",font=("Arial", 10)) #scribir una etiqueta label
instrucciones.pack(pady=10) #Espacio arriba y abajo

#Crear text box:
entrada_cantidad=tk.Entry(ventana)
entrada_cantidad.pack(pady=5)

#Crear boton:
boton_iniciar=tk.Button(ventana,text="Generar Lista",bg="blue",fg="white", command=generar_lista)
boton_iniciar.pack(pady=10)

# --- Área de juego ---
etiqueta_lista=tk.Label(ventana, text="---", font=("Arial",10,"bold"))
etiqueta_lista.pack(pady=10)

etiqueta_vidas=tk.Label(ventana, text="Vidas: - ❤",font=("Arial",10, "bold"))
etiqueta_vidas.pack(pady=10)

tk.Label(ventana, text="¿Cual crees que es el número correcto?", font=("Arial",10, "bold")).pack(pady=10)

#Text box ingresar respuesta
entrada_adivina=tk.Entry(ventana)
entrada_adivina.pack(pady=5)

#Boton para verificar
boton_verificar=tk.Button(ventana, text="Verificar✅",bg="green",fg="white", command=comprobar_suerte)
boton_verificar.pack(pady=10)

#Lanzar programa
ventana.mainloop()
