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
    return maximo

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

print(genero_preferido(gen1, gen2, gen3, gen4, gen5))
