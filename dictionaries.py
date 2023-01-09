"""
Es decir, un diccionario para las cartas, cuyos keys son del tipo:
● O01 --> 1 de oros; B12 --> 12 de bastos, E05 --> 5 de espadas ... etc

Como datos, un nuevo diccionario, donde tenemos el nombre literal de la carta, el valor de
la carta, el valor de la carta en el juego y la prioridad ( oros 4, copas 3, espadas 2, bastos 1).

La prioridad nos da la opción de desempatar cartas que tienen el mismo valor.
Este diccionario nos servirá para todo lo relacionado con las cartas.

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
"""

# Estructuras de datos y variables importantes en el juego:
# Utilizaremos las siguientes estructuras de datos en el juego:

spn_cards = {
"O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
"O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
"O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
"O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
"O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
"O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
"O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
"O08": {"literal": "Ocho de Oros", "value": 8, "priority": 4, "realValue": 0.5},
"O09": {"literal": "Nueve de Oros", "value": 9, "priority": 4, "realValue": 0.5},
"O10": {"literal": "Sota de Oros", "value": 10, "priority": 4, "realValue": 0.5},
"O11": {"literal": "Caballero de Oros", "value": 11, "priority": 4, "realValue": 0.5},
"O12": {"literal": "Rey de Oros", "value": 12, "priority": 4, "realValue": 0.5},
"C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
"C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
"C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
"C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
"C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
"C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
"C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
"C08": {"literal": "Ocho de Copas", "value": 8, "priority": 3, "realValue": 0.5},
"C09": {"literal": "Nueve de Copas", "value": 9, "priority": 3, "realValue": 0.5},
"C10": {"literal": "Sota de Copas", "value": 10, "priority": 3, "realValue": 0.5},
"C11": {"literal": "Caballero de Copas", "value": 11, "priority": 3, "realValue": 0.5},
"C12": {"literal": "Rey de Copas", "value": 12, "priority": 3, "realValue": 0.5},
"E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
"E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
"E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
"E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
"E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
"E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
"E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
"E08": {"literal": "Ocho de Espadas", "value": 8, "priority": 2, "realValue": 0.5},
"E09": {"literal": "As de Espadas", "value": 9, "priority": 2, "realValue": 0.5},
"E10": {"literal": "Sota de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
"E11": {"literal": "Caballero de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
"E12": {"literal": "Rey de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
"B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
"B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
"B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
"B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
"B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
"B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
"B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
"B08": {"literal": "Ocho de Bastos", "value": 8, "priority": 1, "realValue": 0.5},
"B09": {"literal": "Nueve de Bastos", "value": 9, "priority": 1, "realValue": 0.5},
"B10": {"literal": "Sota de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
"B11": {"literal": "Caballero de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
"B12": {"literal": "Rey de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
}

players = {"11115555A":
{"name":"Mario","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0},
"22225555A":
{"name":"Pedro","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0},
}

# Crearemos una lista, por ejemplo game=[], donde tendremos los NIF de todos los jugadores
# que participen en la partida en cada momento.
game = []

# Crearemos una lista, por ejemplo mazo=[], donde tendremos todos los id’s de las cartas que
# componen el mazo en cada momento.
deck = []

# Crearemos un diccionario, por ejemplo context_game={}, donde tendremos una serie de
# variables de contexto a las que podamos acceder desde cualquier sitio.
context_game = []
# Por ejemplo context_game[«game»] = lista de jugadores en la partida actual
# context_game[«round»] = ronda actual de la partida.


