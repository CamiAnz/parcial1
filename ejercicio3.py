def calcular_suma(lista):
    return sum(lista)

def calcular_promedio(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    else:
        return 0

def main():
    numero = []
    while True:
        entrada = input("Ingresa un número entero ('0' para salir): ")

        try:
            num = int(entrada)
            if num == 0:
                break
            numero.append(num)
        except ValueError:
            print("Error")

    sumatoria = calcular_suma(numero)
    promedio = calcular_promedio(numero)

    print("Los números ingresados fueron:", numero)
    print("La sumatoria de los números es:", sumatoria)
    print("El promedio de los números es:", promedio)

main()
