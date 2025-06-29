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
            lista_promedios_materias = Application.calcular_promedios_por_materia(matriz_notas)
            lista_nombres_materias = Application.generar_lista_nombres_materias(lista_promedios_materias)
            
            Utils.ordenar_promedios_materias_desc(lista_promedios_materias, lista_nombres_materias)
            Utils.imprimir_promedios_materias(lista_promedios_materias, lista_nombres_materias)

            Utils.imprimir_materia_mayor_promedio(lista_promedios_materias, lista_nombres_materias)

        case "6":
            legajo = int(input("Ingrese el legajo q desea buscar: "))
            print("")

            lista_datos_del_alumno = Utils.buscar_estudiante_por_legajo(legajo, lista_legajos, lista_nombres, lista_generos, matriz_notas, lista_promedios_alumnos)
            
            if len(lista_datos_del_alumno) > 0:
                Utils.imprimir_datos_alumno(lista_datos_del_alumno)

            else:
                print(f"No se encontro el legajo {legajo}.")

        case "7":
            nro_materia = int(input("Ingrese el numero de materia: "))
            lista_notas_de_materia = Utils.buscar_cantidad_de_notas(matriz_notas, 1)
            Utils.imprimir_datos_materia(lista_notas_de_materia)                
        
        case "8":
            print("Hasta luego")
            continuar = False

        case _:
            print("Opcion no valida. Intente de nuevamente.")