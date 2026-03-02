import random

def adivina_el_numero():
    contador=0
    datos=list()
    x=0
    while x<3:
        x=input("Ingrese un número mayor o igual a 3: ").strip()
        if not x.isdigit():
            print("Caracter invalido⚠")
            x=0
            continue
        x=int(x)
    while len(datos)<x:
        num = random.randint(1,101)
        if num not in datos:
            datos.append(num)

    while contador<3:
        contador+=1
        print(f"Adivina el número correcto: {sorted(datos)}")
        answer=int(input("Ingrese su respuesta: "))
        if answer==num:
            print("¡Correcto!✅")
            break
        elif answer>num:
            print("¡Demasiado alto!⚠")
        elif answer<num:
            print("¡Demasiado bajo!⚠")
    else:
        print("¡Has agotado tus intentos!❌")
    return f"Juego completado, el número correcto era: {num}💥"

print(adivina_el_numero())