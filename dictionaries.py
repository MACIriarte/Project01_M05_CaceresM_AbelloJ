"""
Estructuras de datos y variables importantes en el juego:
Utilizaremos las siguientes estructuras de datos en el juego:

car t a s = {
"O01": { " l i t e r a l " : "As de Oros" , "va lue" : 1, "pr io r i t y " : 4, "rea lVa l ue" : 1},
"O02": { " l i t e r a l " : "Dos de Oros" , "va lue" : 2, "pr io r i t y " : 4, "rea lVa l ue" : 2},
"O03": { " l i t e r a l " : "Tres de Oros" , "va lue" : 3, "pr io r i t y " : 4, "rea lVa l ue" : 3},
.....}

Es decir, un diccionario para las cartas, cuyos keys son del tipo:
● O01 --> 1 de oros; B12 --> 12 de bastos, E05 --> 5 de espadas ... etc

Como datos, un nuevo diccionario, donde tenemos el nombre literal de la carta, el valor de
la carta, el valor de la carta en el juego y la prioridad ( oros 4, copas 3, espadas 2, bastos 1).

La prioridad nos da la opción de desempatar cartas que tienen el mismo valor.
Este diccionario nos servirá para todo lo relacionado con las cartas.

playe r s = { "11115555A":
{ "name":"Mario" ,"human":True,"bank" :False," in i t i a l C a r d " :"" ,"pr io r i t y " :0,"type" :40,"bet" :4,"poi
nts" :0,"cards " :[],"roundPoint s " :0},
"22225555A":
{ "name":"Pedro" ,"human":True,"bank" :False," in i t i a l C a r d " :"" ,"pr io r i t y " :0,"type" :40,"bet" :4,"poi
nts" :0,"cards " :[],"roundPoint s " :0},
...}

Es decir, un diccionario donde sus keys son los NIF’s de los jugadores disponibles
almacenados en BBDD y como valor un nuevo diccionario con los elementos:

● nombre
● humano del tipo booleano
● banca del tipo booleano
● carta inicial, que será la que determine la prioridad de los jugadores.
● Prioridad, que vendrá determinada por la carta inicial.
● Tipo que será 50 en el caso atrevido, 40 en el caso normal y 30 en el caso prudente.
● Apuesta
● Puntos, representa los puntos de cada jugador en la partida.
● Cartas, que será una lista donde almacenaremos los id’s de cartas en cada turno.
● Puntos ronda, que serán los puntos conseguidos durante el turno.

En este diccionario tendremos almacenados todos los jugadores que se hayan creado en
algún momento y ya estén en BBDD y nos servirá para gestionar todo los relacionado con los
jugadores.

Crearemos una lista, por ejemplo game=[], donde tendremos los NIF de todos los jugadores
que participen en la partida en cada momento.

Crearemos una lista, por ejemplo mazo=[], donde tendremos todos los id’s de las cartas que
componen el mazo en cada momento.

Crearemos un diccionario, por ejemplo context_game={}, donde tendremos una serie de
variables de contexto a las que podamos acceder desde cualquier sitio.

Por ejemplo context_game[«game»] = lista de jugadores en la partida actual
context_game[«round»] = ronda actual de la partida.

Tal y como indica su nombre, este diccionario nos será de utilidad para tener, de forma
ordenada, variables que pueden ser de tipo global.

Con estas variables, ya podemos gestionar prácticamente todos los aspectos del juego.
Algunas sugerencias:

Para la inserción de datos en BBDD, sería conveniente crearse un diccionario para cada una
de las tablas que tengamos que actualizar durante el juego.
Por ejemplo:

cardgame = {'cardgame_id': id de partida, 'players': Numero de jugadores, 'start_hour':Hora
de inicio de artida ( datetime), 'rounds': Número de rondas, 'end_hour': hora final de partida
( datetime) }

player_game = {id_game:{id_player_1:{initial_card_id:”card id”, starting_points:”puntos al
inicio”, ending_points:”puntos al final de partida},...,id_player_n:{initial_card_id:”card id”,
starting_points:”puntos al inicio”, ending_points:”puntos al final de partida}}”

player_game_round = {round:{id_player_1:{is_bank:”0 ó 1”,bet_points:”apuesta en la
ronda”,starting_round_points:”puntos al inicio de la partida,cards_value:”puntos obtenido en
la actual ronda”,endind_round_points:”puntos al final de la ronda”},...,{id_player_n:
{is_bank:”0 ó 1”,bet_points:”apuesta en la ronda”,starting_round_points:”puntos al inicio de la
partida,cards_value:”puntos obtenido en la actual ronda”,endind_round_points:”puntos al
final de la ronda”}
""

