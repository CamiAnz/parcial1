def num_entero(num):
    if num < 0:
        print("El número ingresado es negativo.")
    elif num> 0:
        print("El número ingresado es positivo.")
    else:
        print("El número ingresado es igual a cero.")

def main():
    while True:
        entrada = input("Ingresa un número entero ('*' para salir): ")

        if entrada == "*":
            break

        try:
            num = int(entrada)
            num_entero (num)
        except ValueError:
            print("Error: Ingresa solo números enteros.")

    print("Fin del programa")

main()

