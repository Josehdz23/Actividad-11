estudiantes = {}
def menu():
    print("\n===== MENÚ PRINCIPAL =====\n1. Registrar estudiantes\n2. Mostrar todos los estudiantes y cursos\n3. Buscar estudiante por carnet\n4. Salir")

def registrar_Estudiantes():
    while True:
        try:
            print("\n===== REGISTRAR ESTUDIANTES =====")
            cantidad = int(input("\n¿Cuántos estudiantes quiere registrar?: "))
            if cantidad > 0:
                for i in range(cantidad):
                    try:
                        while True:
                            try:
                                carnet = int(input(f"\nIngrese el carnet del estudiante {i + 1}: "))
                                if carnet > 0:
                                    if carnet in estudiantes:
                                        print("\nEl estudiante ya existe, ingrese un nuevo carnet")
                                    else:
                                        break
                                else:
                                    print("\nEl carnet no es valido, reintente")
                            except Exception as e:
                                print(f"\nEL carnet no es valido, reintente {e}")
                        while True:
                            nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
                            if nombre or nombre.isspace():
                                break
                            else:
                                print("\nEl nombre del estudiante no es valido, reintente")
                        while True:
                            try:
                                edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
                                if edad > 18 and edad < 60:
                                    break
                                else:
                                    print("\nLa edad no es valida, reintente")
                            except Exception as e:
                                print(f"\nLa edad no es valida, reintente {e}")
                        while True:
                            carrera = input(f"Ingrese la carrera del estudiante {i + 1}: ")
                            if carrera or carrera.isspace():
                                break
                            else:
                                print("\nEl nombre de la carrera no es valida, reintente")
                        estudiantes[carnet] = {
                            "Nombre": nombre,
                            "Edad": edad,
                            "Carrera": carrera,
                            "Cursos": {}
                        }
                        while True:
                            try:
                                cursos = int(input(f"Ingrese cuantos cursos se le agregaran al estudiante {i + 1}: "))
                                if cursos > 0:
                                    for j in range(cursos):
                                        while True:
                                            try:
                                                nombreCurso = input(f"\nIngrese el nombre del curso {j + 1}: ")
                                                if nombreCurso or nombreCurso.isspace():
                                                    break
                                                else:
                                                    print("\nEl nombre del curso no es valido, reintente")
                                            except Exception as e:
                                                print(f"\nEl nombre del curso no es valido, reintente {e}")
                                        while True:
                                            try:
                                                notaTareas = float(
                                                    input(f"Ingrese la nota de las tareas del curso {j + 1}: "))
                                                if notaTareas >= 0 and notaTareas <= 30:
                                                    break
                                                else:
                                                    print("\nLa nota de las tareas no es valida, reintente")
                                            except Exception as e:
                                                print(f"\nLa nota de las tareas no es valida, reintente {e}")
                                        while True:
                                            try:
                                                notaParcial = float(
                                                    input(f"Ingrese la nota del parcial del curso {j + 1}: "))
                                                if notaParcial >= 0 and notaParcial <= 30:
                                                    break
                                                else:
                                                    print("\nLa nota del parcial no es valida, reintente")
                                            except Exception as e:
                                                print(f"\nEl nota del parcial no es valida, reintente {e}")
                                        while True:
                                            try:
                                                notaProyecto = float(
                                                    input(f"Ingrese la nota del proyecto del curso {j + 1}: "))
                                                if notaProyecto >= 0 and notaProyecto <= 40:
                                                    break
                                                else:
                                                    print("\nLa nota del proyecto no es valida, reintente")
                                            except Exception as e:
                                                print(f"\nLa nota del proyecto no es valida, reintente {e}")
                                        estudiantes[carnet]["Cursos"][nombreCurso] = {
                                            "Notas Tareas": notaTareas,
                                            "Notas Parcial": notaParcial,
                                            "Notas Proyecto": notaProyecto
                                        }
                                    break
                                else:
                                    print("\nEl numero de cursos no es valido, reintente")
                            except Exception as ex3:
                                print(f"\nOcurrió un error: {ex3}, reintente")
                    except Exception as ex2:
                        print(f"\nOcurrió un error: {ex2}, reintente")
                print("\nSe ha agregado el estudiante")
                break
            else:
                print("\nDato invalido, reintente")
        except Exception as ex:
            print(f"\nOcurrió un error: {ex}, reintente")

def mostrar_estudiantes():
    if estudiantes:
        for clave, datos in estudiantes.items():
            sumaTotal = 0
            noCursos = len(estudiantes[clave]["Cursos"])
            print(f"\nCarnet: {clave}, Nombre: {datos['Nombre']}, Edad: {datos['Edad']}, Carrera: {datos['Carrera']}\nCursos: ")
            for clave2, datos2 in datos["Cursos"].items():
                print(f"Nombre del curso: {clave2}, Nota Tareas: {datos2["Notas Tareas"]}, Nota Parcial: {datos2["Notas Parcial"]}, Nota Proyecto: {datos2["Notas Proyecto"]}")
                suma = datos2["Notas Tareas"] + datos2["Notas Parcial"] + datos2["Notas Proyecto"]
                sumaTotal = sumaTotal + suma
                print(f"Nota total del curso: {suma}")
            print(f"El promedio de todos los cursos del estudiante con CARNET: {clave} es: {sumaTotal/noCursos}")
    else:
        print("\nNo hay estudiantes registrados! ")

def buscar_Estudiantes():
    if estudiantes:
        while True:
            try:
                buscar = int(input("Ingrese el carnet del estudiante a buscar: "))
                if buscar in estudiantes.keys():
                    for clave, datos in estudiantes.items():
                        if buscar == clave:
                            sumaTotal = 0
                            noCursos = len(estudiantes[clave]["Cursos"])
                            print(
                                f"\nCarnet: {clave}, Nombre: {datos['Nombre']}, Edad: {datos['Edad']}, Carrera: {datos['Carrera']}\nCursos: ")
                            for clave2, datos2 in datos["Cursos"].items():
                                print(
                                    f"Nombre del curso: {clave2}, Nota Tareas: {datos2["Notas Tareas"]}, Nota Parcial: {datos2["Notas Parcial"]}, Nota Proyecto: {datos2["Notas Proyecto"]}")
                                suma = datos2["Notas Tareas"] + datos2["Notas Parcial"] + datos2["Notas Proyecto"]
                                sumaTotal = sumaTotal + suma
                                print(f"Nota total del curso: {suma}")
                            print(f"El promedio de todos los cursos del estudiante con CARNET: {clave} es: {sumaTotal / noCursos}")
                    break
                else:
                    print("\nNo se encontró el estudiante! ")
                    break
            except Exception as e:
                print(f"\nEl carnet del estudiante no es valido, reintente {e}")
    else:
        print("\nNo hay estudiantes registrados! ")

def main():
    while True:
        menu()
        try:
            op = int(input("Escoga una opción: "))
            match op:
                case 1:
                    registrar_Estudiantes()
                case 2:
                    mostrar_estudiantes()
                case 3:
                    buscar_Estudiantes()
                case 4:
                    print("\nSaliendo...")
                    break
                case _:
                    print("\nEsa opción no existe")

        except Exception as ex:
            print(f"\nOcurrió un error: {ex}, reintente")

main()