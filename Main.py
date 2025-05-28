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
    Application.mostrar_menu()
    opcion = input("Elege una opcion: ")

    match opcion:
        case "1":
            matriz_notas = Application.cargar_notas(matriz_notas)
            lista_nombres = Application.cargar_alumnos(lista_nombres)
            lista_generos = Application.cargar_generos(lista_generos)
            lista_legajos = Application.cargar_legajos(lista_legajos)

        case "2":
            Utils.imprimir_todos_los_datos(matriz_notas, lista_nombres, lista_generos, lista_legajos)

        case "3":
            lista_promedios_alumnos = Application.calcular_promedios_por_alumnos(matriz_notas)
            Utils.imprimir_promedios(lista_promedios_alumnos, lista_nombres)
        
        case "4":
            modo_ordenamiento = ""
            while modo_ordenamiento != "asc" and modo_ordenamiento != "desc":
                modo_ordenamiento = input("Elige el orden ASC o DESC: ")
                modo_ordenamiento = Utils.to_lower(modo_ordenamiento)

                Utils.ordenar_promedios(lista_promedios_alumnos, lista_nombres, modo_ordenamiento)
                Utils.imprimir_promedios(lista_promedios_alumnos, lista_nombres)

        case "5":
            lista_promedios_materias = Application.calcular_promedios_por_materia(matriz_notas)
            lista_nombres_materias = Application.generar_lista_nombres_materias(lista_promedios_materias)
            Utils.imprimir_materia_mayor_promedio(lista_promedios_materias, lista_nombres_materias)
        case "6":
            legajo = int(input("Ingrese el legajo q desea buscar: "))
            lista_datos_encontrados = Utils.buscar_estudiante_por_legajo(legajo, lista_legajos, lista_nombres, lista_generos, matriz_notas, lista_promedios_alumnos)
            
            if len(lista_datos_encontrados) > 0:
                cabecera = ["Legajo", "Nombre", "Genero"]
                for i in range(1, cantidad_notas + 1):
                    cabecera += [f"Nota_Materia_{i}"]
                cabecera += ["Promedio"]

                Utils.imprimir_lista(cabecera)
                Utils.imprimir_lista(lista_datos_encontrados)
            else:
                print(f"No se encontro el legajo {legajo}.")

        case "7":
            nro_materia = int(input("Ingrese el numero de materia: "))
            lista_conteos = Utils.buscar_cantidad_de_notas(matriz_notas, 1)
            
            cabecera = []
            for i in range(10):
                cabecera += [f"Notas_con_{i + 1}"]
            
            Utils.imprimir_lista(cabecera)
            Utils.imprimir_lista(lista_conteos)                
        
        case "8":
            print("Hasta luego")
            continuar = False

        case _:
            print("Opcion no valida. Intente de nuevamente.")