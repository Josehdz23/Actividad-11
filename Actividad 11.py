def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = []
def main():
    while True:
        try:
            n = int(input("\nCuántos nombres desea agregar: "))
            for i in range(n):
                nombre = input(f"Nombre {i+1}: ")
                nombres.append(nombre)
            resultado = quick_sort(nombres)
            print(resultado)
        except Exception as ex:
            print(f" Error reintente: {ex}")
main()