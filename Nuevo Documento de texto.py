#ejercicio1 
def contar_ocurrencias(frase):
    contador = {}
    for letra in frase:
        if letra.isalpha():
            letra = letra.lower()
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    return contador

def main():
    frase = input("Ingresa una frase: ")
    resultado = contar_ocurrencias(frase)

    print("Número de ocurrencias de cada letra:")
    for letra, ocurrencias in resultado.items():
        print(f"{letra}: {ocurrencias}")

main()

#ejercicio2
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
            print("Error")

    print("Fin del programa")

main()

#ejercicio3
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

