# calculadora

# esta funcion es para sumar dos numeros
def add(x, y):
    return x + y

# esta funcion es para restar dos numeros
def subtract(x, y):
    return x - y

# esta funcion es para multiplicar dos numeros
def multiply(x, y):
    return x * y

# esta funcion es para dividir 2 numeros
def divide(x, y):
    return x / y


print("Selecciona una operacion.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # ingresa la opcion
    choice = input("Eligi tu opcion(1/2/3/4): ")

    # verifica la opcion
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa tu primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Valor invalido")
