#importamos los datos de fecha

from datetime import datetime, date

#solicitamos ingresar los datos con formato dd mm aaaa

print("Ingresa tu fecha de nacimiento con formato (dd mm aaaa) para calcular tu edad:")
fecha_de_nacimiento = datetime.strptime(input("--->"), "%d %m %Y")

#realizamos la resta de año actal-año de nacimiento y en caso de que aun no cumplio los años hago
#una comparacion mes/fecha de hoy MENOR a mes fecha de cumpleaños. Si es menor (no cumplio) es true (1) y le 
#resta 1. Si es false (0) significa que ya cumplio, entonces le resta 0.

def calcular_edad(nacimiento):
    today = date.today()
    return today.year - nacimiento.year - ((today.month, today.day) < (nacimiento.month, nacimiento.day))

#traemos la edad

edad = calcular_edad(fecha_de_nacimiento)

#imprimimos

print(f'Tu edad es {edad} años.')
