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
