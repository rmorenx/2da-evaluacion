frutas = {
    "manzana": 2.50,
    "banana": 1.75,
    "uva": 3.00,
    "naranja": 1.50,
    "pera": 2.00
}

def calcular_precio_final(fruta, cantidad):
    if fruta in frutas:
        precio_unitario = frutas[fruta]
        precio_total = precio_unitario * cantidad
        return precio_total
    else:
        raise KeyError("La fruta especificada no existe en el diccionario.")

# Función principal
def main():
    while True:
        try:
            fruta = input("Ingrese el nombre de la fruta: ").lower()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            
            precio_final = calcular_precio_final(fruta, cantidad)
            print(f"El precio final de {cantidad} {fruta}(s) es: ${precio_final:.2f}")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
        except KeyError as e:
            print(e)
        
        continuar = input("¿Desea realizar otra consulta? (s/n): ").lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    main()
