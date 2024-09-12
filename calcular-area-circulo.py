# Paso 1: Solicitar al usuario que ingrese el radio del circulo a carcular

# Paso 2: Calcular el area del circulo utilizando la formula area=pi * radio^2 

# Paso 3: Mostrar al usuario el area calculada

from math import pi


radio = float(input("Por favor ingrese el radio del circulo: "))

area = pi * (radio**2) 

print("El area del circulo con radio", radio, "es:", area)