""" La velocidad de escape de un planeta 
(la velocidad mínima necesaria para poder salir de un planeta)
está dada por la siguiente ecuación."""

# velocidad = raiz de 2gr
#g es la gravedad
#R es el radio del planeta

import sys

gravedad = float(sys.argv[1])
radio_km = int(sys.argv[2])
radio_metro = radio_km*1000
import math
x= (2*gravedad*radio_metro)
velocidad_escape= math.sqrt(x)

print("La velocidad de escape del planeta es de: " + str(round(velocidad_escape,3)))


