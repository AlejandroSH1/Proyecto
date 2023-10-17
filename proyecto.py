"""
Alfredo Alejandro Soto Herrera - A01711368
Proyecto integrador
Recomendador de peliculas
Este proyecto consiste en un servicio de streaming, que recomienda peliculas
en base a los gustosde un usuario.
"""
#bibliotecas
import statistics

def promedio_generos(peliculas):
    """
    recibe: peliculas, es un arreglo de 3 películas de un género específico
    Función que calcula el promedio del arreglo
    devuelve: el promedio de las peliculas que pertenecen al género escogido
    """
    promedio = statistics.mean(peliculas)
    return promedio

def genero_preferido(genero_1, genero_2, genero_3, genero_4, genero_5):
    """
    recibe: genero_1, genero_2, genero_3, genero_4 y genero_5 que corresponden
    a los promedios de los géneros suspenso, western, comedia, caricatura y
    ficcion respectivamente
    Funcion en la cual devuelve el género preferido del usuario y en caso de
    ser más de uno se adjunta todo en una lista, en un segundo paso se
    elimina el promedio de los géneros para permanecer unicamente el nombre
    del género
    devuelve: máximo
    """
    maximo = [genero_1, "Suspenso"]
    if genero_2 > maximo[0]:
        maximo = [genero_2, "Western"]
    elif genero_2 == maximo[0]:
        maximo.append(genero_2)
        maximo.append("Western")
    if genero_3 > maximo[0]:
        maximo = [genero_3, "Comedia"]
    elif genero_3 == maximo[0]:
        maximo.append(genero_3)
        maximo.append("Comedia")
    if genero_4 > maximo[0]:
        maximo = [genero_4, "Caricatura"]
    elif genero_4 == maximo[0]:
        maximo.append(genero_4,)
        maximo.append("Caricatura")
    if genero_5 > maximo[0]:
        maximo = [genero_5, "Ficcion"]
    elif genero_5 == maximo[0]:
        maximo.append(genero_5)
        maximo.append("Ficcion")
        
    if len(maximo) == 2:
        maximo.pop(0)
        return maximo
    elif len(maximo) == 4:
        maximo.pop(0)
        maximo.pop(1)
        return maximo
    elif len(maximo) == 6:
        maximo.pop(0)
        maximo.pop(1)
        maximo.pop(2)
        return maximo
    elif len(maximo) == 8:
        maximo.pop(0)
        maximo.pop(1)
        maximo.pop(2)
        maximo.pop(3)
        return maximo
    elif len(maximo) == 10:
        maximo.pop(0)
        maximo.pop(1)
        maximo.pop(2)
        maximo.pop(3)
        maximo.pop(4)
        return maximo

print("Califica las películas sobre 10 y en caso de no haber visto alguna\
coloca 0, en base a estas calificaciones escogeremos un género sobre el \
cual hacerte recomendaciones \n")

#El usuario califica peliculas para conocer su género preferido
peliculas_a_calificar = ["intriga", "los otros", "sexto sentido", "django",
                         "los ocho mas odiados","comancheria", "barbie",
                         "son como niños", "scary movie", "cars", "shrek",
                         "up", "avatar", "star wars(III)","spiderman 2"]

calificaciones = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

i = 0
for i in range(len(peliculas_a_calificar)):
    print(peliculas_a_calificar[i])
    calificaciones[i] = int(input())

suspenso = calificaciones[0:3]
western = calificaciones[3:6]
comedia = calificaciones[6:9]
caricatura = calificaciones[9:12]
ficcion = calificaciones[12:15]

#Se guardan en variables los promedios
gen1 = promedio_generos(suspenso)
gen2 = promedio_generos(western)
gen3 = promedio_generos(comedia)
gen4 = promedio_generos(caricatura)
gen5 = promedio_generos(ficcion)

preferido = genero_preferido(gen1, gen2, gen3, gen4, gen5)
print()
if len(preferido) == 1:
    print("Tu género preferido fue: ", preferido)
else:
    print("Tus géneros preferidos fueron: ", preferido)
    preferido = [input("Ingresa el nombre del genero que quieras ver hoy \n")]
print()

#Se crean listas con recomendaciones de películas según su género
lista_suspenso = ["el niño", "halloween", "un lugar en silencio",
                  "fragmentado", "la purga"]
lista_western = ["rambo", "nope", "logan", "renacido",
                 "vaqueros contra aliens"]
lista_comedia = ["que paso ayer", "golpe bajo", "gato con botas",
                 "en donde estan las rubias", "mario bros"]
lista_caricatura = ["kung fu panda", "toy story", "wall-e",
                    "monsters university", "atlantis"]
lista_ficcion = ["interestelar", "e.t.", "pantera negra", "avengers",
                 "the batman"]

recomendaciones = [lista_suspenso, lista_western, lista_comedia,
                   lista_caricatura, lista_ficcion]

#Se aplican if´s para encontrar el género preferido del usuario y recomendar
if preferido == ["Suspenso"]:
    peli_sus = 0
    while(peli_sus < len(recomendaciones[0])):
        print("te recomendamos ver: \n", recomendaciones[0][peli_sus])
        if peli_sus < 4:
            pregu1 = input("¿Deseas otra recomendacion? ")
        if pregu1 != "no":
            peli_sus = peli_sus + 1
        else:
            peli_sus = len(recomendaciones[0])
    print("\nNo tenemos más recomendaciones por el momento, gracias")
        
if preferido == ["Western"]:
    peli_wes = 0
    while(peli_wes < len(recomendaciones[1])):
        print("te recomendamos ver: \n", recomendaciones[1][peli_wes])
        if peli_wes < 4:
            pregu2 = input("¿Deseas otra recomendacion? ")
        if pregu2 != "no":
            peli_wes = peli_wes + 1
        else:
            peli_wes = len(recomendaciones[1])
    print("\nNo tenemos más recomendaciones por el momento, gracias")
    
if preferido == ["Comedia"]:
    peli_com = 0
    while(peli_com < len(recomendaciones[2])):
        print("te recomendamos ver: \n", recomendaciones[2][peli_com])
        if peli_com < 4:
            pregu3 = input("¿Deseas otra recomendacion? ")
        if pregu3 != "no":
            peli_com = peli_com + 1
        else:
            peli_com = len(recomendaciones[2])
    print("\nNo tenemos más recomendaciones por el momento, gracias")
        
if preferido == ["Caricatura"]:
    peli_car = 0
    while(peli_car < len(recomendaciones[3])):
        print("te recomendamos ver: \n", recomendaciones[3][peli_car])
        if peli_car < 4:
            pregu4 = input("¿Deseas otra recomendacion? ")
        if pregu4 != "no":
            peli_car = peli_car + 1
        else:
            peli_car = len(recomendaciones[3])
    print("\nNo tenemos más recomendaciones por el momento, gracias")
        
if preferido == ["Ficcion"]:
    peli_fic = 0
    while(peli_fic < len(recomendaciones[4])):
        print("te recomendamos ver: \n", recomendaciones[4][peli_fic])
        if peli_fic < 4:
            pregu5 = input("¿Deseas otra recomendacion? ")
        if pregu5 != "no":
            peli_fic = peli_fic + 1
        else:
            peli_fic = len(recomendaciones[4])
    print("\nNo tenemos más recomendaciones por el momento, gracias")
