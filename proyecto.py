"""
Este proyecto consiste en un servicio de streaming, que recomienda peliculas en base a los gustos
de un usuario.
"""
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
spiderman2 = int(input("spiderman 2 "))
star_wars = int(input("star wars "))
avatar  = int(input("avatar "))

#Se saca el promedio de cada género de pelicula para ordenar cuál es el género más alto
def suspenso(intriga, los_otros, sexto_sentido):
    prom_sus = (intriga + los_otros + sexto_sentido) / 3
    return prom_sus

def western(django, los_ocho_mas_odiados, comancheria):
    prom_wes = (django + los_ocho_mas_odiados + comancheria) / 3
    return prom_wes

def comedia(barbie, son_como_niños, scary_movie):
    prom_com = (barbie + son_como_niños + scary_movie) / 3
    return prom_com

def caricatura(cars, shrek, up):
    prom_car = (cars + shrek + up) / 3
    return prom_car

def ficcion(spiderman2, star_wars, avatar):
    prom_fic = (spiderman2 + star_wars + avatar) / 3
    return prom_fic

#Dependiendo de los resultados de los promedios, se ordenarán los generos de mayor a menor, para conocer cuál es el género que más ve el usuario
