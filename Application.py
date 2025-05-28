import random
import Utils
import Validaciones

def mostrar_menu():
    print("Menú de opciones:")
    print("1 - Cargar notas de estudiantes.")
    print("2 - Mostrar estudiantes.")
    print("3 - Calcular promedio de alumnos.")
    print("4 - Ordenar promedios.")
    print("5 - Calcular promedios de materias.")
    print("6 - Buscar datos de un estudiante por legajo.")
    print("7 - None.")
    print("8 - Salir.")

                
def cargar_notas(matriz_notas: list) -> list:
    for i in range(len(matriz_notas)):
        for j in range(len(matriz_notas[i])):
            calificacion = 0
            while not Validaciones.validar_calificacion(calificacion):
                # calificacion = int(input(f"Ingresar nota del alumno: "))
                calificacion = random.randint(1, 10)
            matriz_notas[i][j] = calificacion
    return matriz_notas


def cargar_alumnos(lista_nombres: list) -> list:
    for i in range(len(lista_nombres)):
        nombre = ""
        while not Validaciones.validar_nombre(nombre):
            # nombre = input(f"Ingresar nombre del alumno: ")
            nombre = f"Alumno_{i+1}"
        lista_nombres[i] = nombre
    return lista_nombres


def cargar_generos(lista_generos: list) -> list:
    for i in range(len(lista_generos)):
        genero = ""
        while not Validaciones.validar_genero(genero):
            # genero = input(f"Ingresar genero (F/M/X): ")
            genero = random.choice(['F', 'M', 'X'])
        lista_generos[i] = genero
    return lista_generos


def cargar_legajos(lista_legajos: list) -> list:
    for i in range(len(lista_legajos)):
        legajo = 0
        while not Validaciones.validar_legajo(legajo):
            # legajo = int(input(f"Ingresar legajo: (debe ser de 5 digitos)"))
            legajo = random.randint(10000, 99999)
        lista_legajos[i] = legajo
    return lista_legajos

def calcular_promedios_por_alumnos(matriz_notas:list, )-> list:
    lista_promedios = [0] * 30
    for i in range(len(matriz_notas)):
        suma = 0
        for j in range(len(matriz_notas[i])):
            suma = suma + matriz_notas[i][j]        

        promedio = suma / len(matriz_notas[i])
        lista_promedios[i] = promedio
        
    return lista_promedios

def calcular_promedios_por_materia(matriz_notas: list)->list:
    cantidad_alumnos = len(matriz_notas)
    cantidad_materias = len(matriz_notas[0])
    lista_promedios_materias = [0] * cantidad_materias 

    for j in range(cantidad_materias):
        suma = 0
        for i in range(cantidad_alumnos):
            suma += matriz_notas[i][j]
        promedio = suma / cantidad_alumnos
        lista_promedios_materias[j] = promedio

    return lista_promedios_materias

def generar_lista_nombres_materias(lista_promedios_materias: list)->list:
    cantidad_materias = len(lista_promedios_materias)
    lista_nombres_materias = [0] * cantidad_materias
    for i in range(cantidad_materias):
        lista_nombres_materias[i] = f"Materia_{i+1}"
    
    return lista_nombres_materias