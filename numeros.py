import random

# Función para generar una lista de números aleatorios
def crear_lista_aleatoria(n):
    return [random.randint(1, 100) for _ in range(n)]

# Función para crear un diccionario con claves desde 1 hasta n
def crear_diccionario(n):
    return {i: random.randint(1, 100) for i in range(1, n + 1)}

def main():
    n = int(input("Ingrese la cantidad de números aleatorios y el tamaño del diccionario: "))
    
    lista_aleatoria = crear_lista_aleatoria(n)
    
    diccionario = crear_diccionario(n)
    
    print("Lista de números aleatorios:")
    print(lista_aleatoria)
    
    print("Valores del diccionario:")
    for clave, valor in diccionario.items():
        print(f"Clave: {clave}, Valor: {valor}")

if __name__ == "__main__":
    main()
