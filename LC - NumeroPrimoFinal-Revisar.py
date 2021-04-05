#aca decimos que todo numero EsPrimo. Ingresamos un numero y armamos una lista de 2 al numero ingresado
#si el resto entre ambos es 0, entonces no es primo.

n = int(input("Ingrese su numero para saber si es primo= "))
EsPrimo = True
for l in range(2, n):
   if n % l == 0:
     EsPrimo = False
     break

#imprimimos el resultado de EsPrimo (falso o verdadero)

print(EsPrimo)