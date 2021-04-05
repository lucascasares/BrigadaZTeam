#ingresamos los 3 numeros y los ponemos en una lista

print ("Vamos a encontrar el mayor de los numeros ingresados")

ListadoNumeros=[]
for x in range (3):
    Numero=int(input("Ingrese un número:"))
    ListadoNumeros.append(Numero)

#imprimimos el mayor del listado

print(f'El numero mayor es {max(ListadoNumeros)}.')