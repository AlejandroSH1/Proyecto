"""
Este proyecto consiste en un servicio de streaming, que recomienda peliculas
en base a los gustosde un usuario.
"""
#bibliotecas
import statistics

def suspenso(sus_1, sus_2, sus_3):
    """
    Función que devuelve el promedio de las peliculas que pertenecen al genero
    de suspenso
    """
    suspenso_peli = [sus_1, sus_2, sus_3]
    prom_sus = statistics.mean(suspenso_peli)
    return prom_sus

def western(wes_1, wes_2, wes_3):
    """
    Función que devuelve el promedio de las peliculas que pertenecen al genero
    western
    """
    western_peli = [wes_1, wes_2, wes_3]
    prom_wes = statistics.mean(western_peli)
    return prom_wes

def comedia(com_1, com_2, com_3):
    """
    Función que devuelve el promedio de las peliculas que pertenecen al genero
    de comedia
    """
    comedia_peli = [com_1, com_2, com_3]
    prom_com = statistics.mean(comedia_peli)
    return prom_com

def caricatura(car_1, car_2, car_3):
    """
    Función que devuelve el promedio de las peliculas que pertenecen al genero
    de caricatura
    """
    caricatura_peli = [car_1, car_2, car_3]
    prom_car = statistics.mean(caricatura_peli)
    return prom_car

def ficcion(fic_1, fic_2, fic_3):
    """
    Función que devuelve el promedio de las peliculas que pertenecen al genero
    de ficción
    """
    ficcion_peli = [fic_1, fic_2, fic_3]
    prom_fic = statistics.mean(ficcion_peli)
    return prom_fic

"""
Dependiendo de los resultados de los promedios, se va a calcular el género
que más ve el usuario por medio de if y elif y se va a imprimir el promedio
que se obtuvo y el género al que pertenece
"""

def genero_preferido(genero_1, genero_2, genero_3, genero_4, genero_5):
    """
    Funcion en la cual devuelve el género preferido del usuario y en caso de
    ser más de uno se adjunta todo en una lista, en un segundo paso se
    elimina el promedio de los géneros para permanecer unicamente el nombre
    del género
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

print("Califica las películas sobre 10 y en caso de no haber visto alguna,\
coloca 0 ")

#El usuario califica peliculas para conocer su género preferido
intriga = int(input("intriga "))
los_otros = int(input("los otros "))
sexto_sentido = int(input("sexto sentido "))
django = int(input("django "))
los_ocho_mas_odiados = int(input("los 8 más odiados "))
comancheria = int(input("comanchería "))
barbie = int(input("barbie "))
son_como_niños = int(input("son como niños "))
scary_movie = int(input("scary movie "))
cars = int(input("cars "))
shrek =int(input("shrek "))
up = int(input("up "))
spiderman_2 = int(input("spiderman 2 "))
star_wars = int(input("star wars "))
avatar  = int(input("avatar "))

#Se guardan en variables los promedios
gen1 = suspenso(intriga, los_otros, sexto_sentido)
gen2 = western(django, los_ocho_mas_odiados, comancheria)
gen3 = comedia(barbie, son_como_niños, scary_movie)
gen4 = caricatura(cars, shrek, up)
gen5 = ficcion(avatar, star_wars, spiderman_2)

preferido = genero_preferido(gen1, gen2, gen3, gen4, gen5)
print()
print(preferido)
print()

if len(preferido) > 1:
    preferido = [input("Ingresa el nombre del genero que quieras ver hoy\
\n")]

#Se crean listas con recomendaciones de películas según su género
lista_suspenso = ["el_niño", "halloween", "un_lugar_en_silencio",
                  "fragmentado", "la_purga"]
lista_western = ["rambo", "nope", "logan", "renacido",
                 "vaqueros_contra_aliens"]
lista_comedia = ["que_paso_ayer", "golpe_bajo", "gato_con_botas",
                 "en_donde_estan_las_rubias", "mario_bros"]
lista_caricatura = ["kung_fu_panda", "toy_story", "wall-e",
                    "monsters_university", "atlantis"]
lista_ficcion = ["interestelar", "e.t.", "pantera_negra", "avengers",
                 "the_batman"]

recomendaciones = [lista_suspenso, lista_western, lista_comedia,
                   lista_caricatura, lista_ficcion]

#Se aplican if´s para encontrar el género preferido del usuario
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
