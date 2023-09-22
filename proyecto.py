"""
Este proyecto consiste en un servicio de streaming, que recomienda peliculas en base a los gustos
de un usuario.
"""
#Se saca el promedio de cada género de pelicula para ordenar cuál es el género más alto
def suspenso(sus_1, sus_2, sus_3):
    prom_sus = (sus_1 + sus_2 + sus_3) / 3
    return prom_sus

def western(wes_1, wes_2, wes_3):
    prom_wes = (wes_1 + wes_2 + wes_3) / 3
    return prom_wes

def comedia(com_1, com_2, com_3):
    prom_com = (com_1 + com_2 + com_3) / 3
    return prom_com

def caricatura(car_1, car_2, car_3):
    prom_car = (car_1 + car_2 + car_3) / 3
    return prom_car

def ficcion(fic_1, fic_2, fic_3):
    prom_fic = (fic_1 + fic_2 + fic_3) / 3
    return prom_fic
"""
Dependiendo de los resultados de los promedios, se va a calcular el género que más ve el usuario
por medio de if y elif y se va a imprimir el promedio que se obtuvo y el género al que pertenece
"""
def genero_preferido(genero_1, genero_2, genero_3, genero_4, genero_5):
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
        maximo.append(genero_4)
        maximo.append("Caricatura")
    if genero_5 > maximo[0]:
        maximo = [genero_5, "Ficcion"]
    elif genero_5 == maximo[0]:
        maximo.append(genero_5)
        maximo.append("Ficcion")
"""
maximo.pop(), según lo que leí en W3, sirve para quitar elementos de una lista en base a un número
que representa el orden de la lista, pero no me está sirviendo como debería, ya que si colocara 0
me debería de quitar el primer elemento y me está quitando el 2do, de igual forma si hay más de un
genero preferido en vez de eliminarme un elemento, se queda con un solo elemento, voy a estudiarlo
y probarlo para entender por qué cambia sufuncionamiento a como dice en la página W3.
"""
    return maximo.pop(-1)


# Esta instrucción permite al usuario entender que hará con las películas que se le mostrarán
print("Califica las películas sobre 10 y en caso de no haber visto alguna, coloca 0 ")

#Aquí los usuarios calificarán las peliculas que brindamos, solo son 3 por género para conocer si le gusta o no el género 
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

#En este punto se llama la función del genero preferido, para mostrarle al usuario su género más visto
gen1 = suspenso(intriga, los_otros, sexto_sentido)
gen2 = western(django, los_ocho_mas_odiados, comancheria)
gen3 = comedia(barbie, son_como_niños, scary_movie)
gen4 = caricatura(cars, shrek, up)
gen5 = ficcion(avatar, star_wars, spiderman_2)

preferido = genero_preferido(gen1, gen2, gen3, gen4, gen5)
print(preferido)

#Se crean listas con recomendaciones de películas según su género al que pertenece
lista_suspenso = ["el_niño", "halloween", "un_lugar_en_silencio", "fragmentado", "la_purga"]
lista_western = ["rambo", "nope", "logan", "renacido", "vaqueros_contra_aliens"]
lista_comedia = ["que_paso_ayer", "golpe_bajo", "gato_con_botas", "en_donde_estan_las_rubias", "mario_bros"]
lista_caricatura = ["kung_fu_panda", "toy_story", "wall-e", "monsters_university", "atlantis"]
lista_ficcion = ["interestelar", "e.t.", "pantera_negra", "avengers", "the_batman"]

#Se aplican if´s para encontrar el género preferido y mostrarle las recomendaciones al usuario
#El usuario puede elegir si quedarse con la primera recomendación o cualquiera posterior
if preferido =="Suspenso":
    peli_sus = 0
    while(peli_sus < len(lista_suspenso)):
        print("te recomendamos ver: ", lista_suspenso[peli_sus])
        pregu1 = input("¿Deseas otra recomendacion? ")
        if pregu1 != "no":
            peli_sus = peli_sus + 1
        else:
            peli_sus = len(lista_suspenso)
        
if preferido =="Western":
    peli_wes = 0
    while(peli_wes < len(lista_western)):
        print("te recomendamos ver: ", lista_western[peli_wes])
        pregu2 = input("¿Deseas otra recomendacion? ")
        if pregu2 != "no":
            peli_wes = peli_wes + 1
        else:
            peli_wes = len(lista_western)
    
if preferido =="Comedia":
    peli_com = 0
    while(peli_com < len(lista_comedia)):
        print("te recomendamos ver: ", lista_comedia[peli_com])
        pregu3 = input("¿Deseas otra recomendacion? ")
        if pregu3 != "no":
            peli_com = peli_com + 1
        else:
            peli_com = len(lista_comedia)
        
if preferido =="Caricatura":
    peli_car = 0
    while(peli_car < len(lista_caricatura)):
        print("te recomendamos ver: ", lista_caricatura[peli_car])
        pregu4 = input("¿Deseas otra recomendacion? ")
        if pregu4 != "no":
            peli_car = peli_car + 1
        else:
            peli_car = len(lista_caricatura)
        
if preferido =="Ficcion":
    peli_fic = 0
    while(peli_fic < len(lista_ficcion)):
        print("te recomendamos ver: ", lista_ficcion[peli_fic])
        pregu5 = input("¿Deseas otra recomendacion? ")
        if pregu5 != "no":
            peli_fic = peli_fic + 1
        else:
            peli_fic = len(lista_ficcion)
