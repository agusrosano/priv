mi_nombre = 'Agus'
mi_apellido = 'Rosano'
nombreCompleto = mi_nombre +' '+ mi_apellido 

#print(nombreCompleto)

a = 10 
b = 20 
suma = a + b
#print(suma)

mi_lista = [1, 2, 3, 4, 5, 6]
# esto es una lista
mi_lista.append(7)
#print(mi_lista)

def filtrar_lista(lista,elemento):
     if elemento in lista:
        return elemento
     else: return f"{elemento} no existe "


resultado = filtrar_lista(mi_lista, 4)
#print(resultado)

# Puedes probar con otros números también
otro_resultado = filtrar_lista(mi_lista, 8)
#print(otro_resultado)

mi_tupla = (1, 2, 3, 4, 5)
# es parecido a una lista pero es inmutable

mi_conjunto = {1, 2, 3, 4, 5}
#Los conjuntos son colecciones desordenadas de elementos únicos. No permiten elementos duplicados.

mi_diccionario = {'nombre': 'Agus', 'apellido': 'Rosano', 'edad': 30}
#Los diccionarios son colecciones desordenadas de pares clave-valor. Las claves deben ser únicas.

####################################################################################################
#________________________________________________for________________________________________________
####################################################################################################

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'q':8}
dict2 = {'e': 4, 'f': 2, 'g': 5, 'h': 3,'q':8}

valores_comunes = []

for clave1,valor1 in dict1.items(): # recorre todas las claves y valores de dict1.
    #comparar con los valores del segundo, el .item se usa para usar apuntar al valor 
 if valor1 in dict2.values():
        valores_comunes.append(valor1)

#print("Valores comunes:", valores_comunes)

# Diccionario para almacenar las claves y valores comunes

dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict4 = {'e': 4, 'b': 5, 'g': 5, 'c': 6}

claves_valores_comunes = {}

for clave3 in dict3.keys():

    if clave3 in dict4.keys():
        claves_valores_comunes[clave3] = (dict3[clave3], dict4[clave3])

#print("Claves y valores comunes:", claves_valores_comunes)





####################################################################################################
#__________________________________________funciones________________________________________________
####################################################################################################

def sumar(a, b):
    return a + b

# cuando llamas a la funcion le das los parametros
resultado = sumar(10, 20)
#print(f"La suma es: {resultado}")

#___________________________________________________________________________________________________

def encontrar_objetos_con_claves_repetidas(dict1, dict2):
    # Diccionario para almacenar los objetos completos con claves repetidas
    objetos_repetidos = {}

    # Iterar sobre el primer diccionario
    for key1, subdict1 in dict1.items():
        # Iterar sobre el segundo diccionario
        for key2, subdict2 in dict2.items():
            # Encontrar claves repetidas entre los subdiccionarios
            claves_comunes = set(subdict1.keys()) & set(subdict2.keys())
            if claves_comunes:
                # Almacenar los objetos completos en el diccionario de resultados
                objetos_repetidos[key1] = subdict1
                objetos_repetidos[key2] = subdict2

    return objetos_repetidos

# Ejemplo de uso
dict1 = {
    'item1': {'a': 1, 'b': 2, 'c': 3},
    'item2': {'d': 4, 'e': 5, 'f': 6},
    'item3': {'g': 7, 'h': 8, 'i': 9}
}

dict2 = {
    'p4': {'a': 10, 'j': 11, 'k': 12},
    'p5': {'l': 13, 'b': 14, 'm': 15},
    'item6': {'n': 16, 'o': 17, 'c': 18}
}

# Llamar a la función y obtener los resultados
objetos_con_claves_repetidas = encontrar_objetos_con_claves_repetidas(dict1, dict2)

#print("Objetos con claves repetidas:", objetos_con_claves_repetidas)


def find_personas_con_apellido(diccionario, apellido):
    """
    ##Encuentra todas las personas en el diccionario que tienen el apellido dado.

   ## Args:
        diccionario (dict): El diccionario que contiene la información de las personas.
        apellido (str): El apellido que se desea buscar.

    ##Returns:## dict: Un nuevo diccionario que contiene solo las personas que tienen el apellido dado.
    """
    personas_encontradas = {}
    for key, persona in diccionario.items():
        if persona.get('Apellido', '') == apellido:
            personas_encontradas[key] = persona
    return personas_encontradas

# Ejemplo de uso
personas = {
    'p1': {'nombre': 'agus', 'Apellido': 'rosano', 'edad': 33},
    'p2': {'nombre': 'pepito', 'Apellido': 'antoniet', 'edad': 23},
    'p3': {'nombre': 'juan', 'Apellido': 'filipino', 'edad': 13},
    'p4': {'nombre': 'elias', 'Apellido': 'rodriguez', 'edad': 53},
    'p5': {'nombre': 'lucas', 'Apellido': 'rosano', 'edad': 6},
}

personas_rosano = find_personas_con_apellido(personas, 'rosano')
#print("Personas con apellido 'rosano':", personas_rosano)


#___________________________________________________________________________________________________


import requests

# URL del endpoint de la API
url = 'https://pokeapi.co/api/v2/pokemon/'

# Realizar la petición GET
response = requests.get(url)

# Verificar si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Guardar los resultados en una variable
    resultados = response.json()
else:
    print("Error al realizar la petición:", response.status_code)

# Usar la variable 'resultados' según sea necesario
print("Conteo total de Pokémon:", resultados['count'])
print("Próxima página de resultados:", resultados['next'])
print("Pokémon encontrados:")
for pokemon in resultados['results']:
    print(pokemon['name'])