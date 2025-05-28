# Validaciones
def validar_dato_longitud(dato, longitud_min:int, longitud_max:int)-> bool:
    """
    Valida que un dato tenga la longitud esperada
    
    Args:
        dato: Es el dato que se va a contar su longitud.
        longitud: Es el valor de longitud que debe tener el dato.

    Returns:
        bool: Retorna True si la longitud del dato es la esperada.
    """

    result = False
    longitud_dato = len(dato)
    if longitud_dato >= longitud_min and longitud_dato <= longitud_max:
        result = True

    return result

def validar_dato_numerico(dato)-> bool:
    """
    Valida que un dato sea un valor numerico
    
    Args:
        dato: Es el dato que se va comprobar q sea numerico.

    Returns:
        bool: Retorna True si el dato es numerico.
    """

    result = True
    for i in str(dato):
        if not (ord(i) >= ord('0') and ord(i) <= ord('9')):
            result = False
    
    return result
    

def validar_dato_string(dato:str)-> bool:
    """
    Valida que un dato sea un valor numerico
    
    Args:
        dato: Es el dato que se va comprobar q sea numerico.

    Returns:
        bool: Retorna True si el dato es numerico.
    """
    
    result = True
    for i in str(dato):
        if not ((ord('A') <= dato <= ord('Z')) or (ord('a') <= dato <= ord('z'))):
            result = False

    return result 



def validar_calificacion(calificacion:int)-> bool:
    """
    #calificaciones: que sean numericas y de entre 1 y 10

    Valida que la calificacion sea un valor entre 1 y 10.
    
    Args:
        calificacion: Es el dato que se va comprobar q sea entre 1 y 10.

    Returns:
        bool: Retorna True si la calificacion es entre 1 y 10.
    """

    result = False    
    es_numerico = validar_dato_numerico(calificacion)
    
    if(es_numerico == True):
        if int(calificacion) >= 1 and int(calificacion) <= 10:
            result = True
    
    return result

def validar_nombre(nombre:str)->bool:
    """
    #calificaciones: que sean numericas y de entre 1 y 10

    Valida que el nombre tenga una longitud > 0
    
    Args:
        calificacion: Es el dato que se va comprobar q sea entre 1 y 10.

    Returns:
        bool: Retorna True si la calificacion es entre 1 y 10.
    """

    result = False

    if len(nombre) > 0:
        result = True

    return result

def validar_genero(genero: str) -> bool:
    """
    # genero: que sea F M o X y la longitud sea de 1.

    Valida que el genero sea un valor F, M o X
    
    Args:
        genero: Es el dato que se va comprobar q sea F, M o X.

    Returns:
        bool: Retorna True si el genero es F, M o X.
    """
    result = False
    generos_validos = ["F", "M", "X"]

    # aca hacer genero to upper casero

    if len(genero) == 1:
        for i in generos_validos:
            if genero == i:
                result = True
    return result

def validar_legajo(legajo:int)->bool:
    """
    # legajo: que sea numerico y que su longitd sea de 5

    Valida que un dato tenga una longitud de 5.
    
    Args:
        dato: Es el dato que se va a validar su longitud.

    Returns:
        bool: Retorna True si el dato es de longitud 5.
    """
    result = False

    if len(str(legajo)) == 5:
        result = True

    return result