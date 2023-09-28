# Recomendaciones para peliculas   A01711368
### Contexto
Una buena recomendación de peliculas basada en tus gustos se ha vuelto crucial actualmente debido al amplio crecimiento de las plataformas de streaming, se ha vuelto escencial debido a que la gente busca una pelicula lo más rápido posible es por eso que un buen algoritmo que se adapte a ti, hace que una app tenga o no éxito.

Como todos nos imaginamos, una forma en la que se recopilan datos para crear este algoritmo propio es por medio de la interacción que tienes con el contenido, al igual que detectan lo que otros usuarios ven después de haber visto esta pelicula o serie que tu mismo viste, también toman como información todo respecto a la pelicula o serie que viste, por ejemplo; año de lanzamiento, ddirector, actores, trama, etc.

Igualmente se checa la hora del día en que normalmente usas el servicio, el dispositivo que usas y cuánto tiempo le inviertes. fuente: https://help.netflix.com/es/node/100639#:~:text=C%C3%B3mo%20funciona%20el%20sistema%20de%20recomendaciones%20de%20Netflix,4%20C%C3%B3mo%20mejoramos%20nuestro%20sistema%20de%20recomendaciones%20

### Idea
Personalmente para hacer este proyecto, considero que es más sencillo hacer una serie de preguntas al usuario, las cuales permitan definir claramente los gustos e intenciones del usuario en la plataforma, simples preguntas que no tardarán mucho tiempo en terminar para que de esta manera se pueda definir clam¿ramente sus gustos.

### Avances
En este 2do avance, he creado el primer archivo del proyecto y en este mismo, se hace una encuesta al usuario sobre peliculas de distintos géneros, esto con el fin de poder crear un promedio de los resultados de los 5 géneros mostrados, para que se pueda encontrar el género que mejor calificación promedia y en base a ello recomendar peliculas de ese estilo.

En el 3er avance, incorporo una nueva función para poder mostrar cual es el género más a fin al usuario.

En el 4to avance incorpore if y elif a mi proyecto para que de esta forma pueda obtener el género que tiene un mayor promedio por parte de las calificaciones
que el usuario asignó.

En este 5to avance practicamente terminé con la idea central del proyecto, solo que encontré un problema en el código y es en donde se pide un pop(), está unido
a una lista que se llama maximo, la cual muestra el género preferido del usuario, esta funcion pop() menciona W3 que sirve para quitar elementos de una lista 
mostrando un número que corresponde a una posición, pero en el python no hace eso y por lo tanto no entendí su funcionamiento, por lo que el código solo funciona
si solo hay un genero preferido y no varios, por lo que tendré que buscar una alternativa o entender como funciona verdaeramente pop().

En este 6to avance investigué mejor la funcion pop() y entendí que lo que pasaba era error mio y las implementé para que borraran los promedios y se mentiene
unicamente el género.
