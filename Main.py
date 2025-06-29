import Application
import Utils

cantidad_alumnos= 30
cantidad_notas = 5

matriz_notas = Utils.inicializar_matriz(cantidad_alumnos, cantidad_notas, 0)
lista_nombres = [0] * cantidad_alumnos 
lista_generos = [0] * cantidad_alumnos
lista_legajos = [0] * cantidad_alumnos
lista_promedios_alumnos = [0] * cantidad_alumnos


continuar = True
while continuar:
    Utils.imprimir_menu()
    opcion = input("Elege una opcion: ")
    print("")

    match opcion:
        case "1":
            matriz_notas = Application.cargar_notas(matriz_notas)
            lista_nombres = Application.cargar_alumnos(lista_nombres)
            lista_generos = Application.cargar_generos(lista_generos)
            lista_legajos = Application.cargar_legajos(lista_legajos)

        case "2":
            Utils.imprimir_todos_los_datos(matriz_notas, lista_nombres, lista_generos, lista_legajos, lista_promedios_alumnos)

        case "3":
            lista_promedios_alumnos = Application.calcular_promedios_por_alumnos(matriz_notas)
        
        case "4":
            Utils.ordenar_promedios(lista_nombres, lista_legajos, lista_generos, matriz_notas, lista_promedios_alumnos)

        case "5":
            Application.promedios_de_materias(matriz_notas)

        case "6":
            Application.buscar_alumno_por_legajo(lista_nombres, lista_legajos, lista_generos, matriz_notas, lista_promedios_alumnos)
        
        case "7":
            Application.cantidad_de_notas_por_materia(matriz_notas)

        case "8":
            print("Hasta luego")
            continuar = False

        case _:
            print("Opcion no valida. Intente de nuevamente.")