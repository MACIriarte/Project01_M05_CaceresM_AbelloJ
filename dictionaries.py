# Estructuras de datos y variables importantes en el juego:
# Utilizaremos las siguientes estructuras de datos en el juego:
spn_cards = {
    "O01": {"cardname": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    "O02": {"cardname": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
    "O03": {"cardname": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    "O04": {"cardname": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    "O05": {"cardname": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    "O06": {"cardname": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    "O07": {"cardname": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    "O10": {"cardname": "Sota de Oros", "value": 10, "priority": 4, "realValue": 0.5},
    "O11": {"cardname": "Caballero de Oros", "value": 11, "priority": 4, "realValue": 0.5},
    "O12": {"cardname": "Rey de Oros", "value": 12, "priority": 4, "realValue": 0.5},
    "C01": {"cardname": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"cardname": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    "C03": {"cardname": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
    "C04": {"cardname": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    "C05": {"cardname": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    "C06": {"cardname": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    "C07": {"cardname": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    "C10": {"cardname": "Sota de Copas", "value": 10, "priority": 3, "realValue": 0.5},
    "C11": {"cardname": "Caballero de Copas", "value": 11, "priority": 3, "realValue": 0.5},
    "C12": {"cardname": "Rey de Copas", "value": 12, "priority": 3, "realValue": 0.5},
    "E01": {"cardname": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "E02": {"cardname": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "E03": {"cardname": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "E04": {"cardname": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "E05": {"cardname": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "E06": {"cardname": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "E07": {"cardname": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "E10": {"cardname": "Sota de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
    "E11": {"cardname": "Caballero de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
    "E12": {"cardname": "Rey de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
    "B01": {"cardname": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"cardname": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    "B03": {"cardname": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    "B04": {"cardname": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    "B05": {"cardname": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    "B06": {"cardname": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    "B07": {"cardname": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    "B10": {"cardname": "Sota de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
    "B11": {"cardname": "Caballero de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
    "B12": {"cardname": "Rey de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
}

# english deck, priority diamonds 4, hearts 3, picas 2, trebol 1
eng_cards = {
    "D01": {"cardname": "As de diamantes", "value": 1, "priority": 1, "realvalue": 1},
}

stored_players = {
    "humans": {"12345678A": {"name": "Mario", "behaviour": "cautious", "earnings": 0, "games": 0, "minutes": 0},
               "12345678F": {"name": "Pedro", "behaviour": "moderated", "earnings": 0, "games": 0, "minutes": 0},
               "12345678Z": {"name": "Alejandro", "behaviour": "bold", "earnings": 0, "games": 0, "minutes": 0}
               },
    "boots": {"boot1_id": {"name": "boot1", "behaviour": "cautious", "earnings": 0, "games": 0, "minutes": 0},
              "boot2_id": {"name": "boot2", "behaviour": "moderated", "earnings": 0, "games": 0, "minutes": 0},
              "boot3_id": {"name": "boot3", "behaviour": "bold", "earnings": 0, "games": 0, "minutes": 0}
              }
}

players = {"11115555A":
               {"name": "Mario", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                "points": 0, "cards": [], "roundPoints": 0},
           "22225555A":
               {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                "points": 0, "cards": [], "roundPoints": 0},
           }

game_settings = {
    "default": {"roundlimit":{"active":True,"rounds":5},"deck":{"spanish":True,"english":False}},

    "custom": {"roundlimit":{"active":False,"rounds":0},"deck":{"spanish":True,"english":False}}
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

# Para la inserción de datos en BBDD, sería conveniente crearse un diccionario para cada una
# de las tablas que tengamos que actualizar durante el juego.
# Por ejemplo:
cardgame = {"cardgame_id": "id_de_partida", "players": "Numero_de_jugadores",
            "start_hour": "Hora_de_inicio_de_artida(datetime)",
            "rounds": "Número_de_rondas", "end_hour": "hora_final_de_partida(datetime)"}

player_game = {"id_game": {"id_player_1": {"initial_card_id": "card_id", "starting_points": "puntos al inicio",
                                           "ending_points": "puntos al final de partida"},
                           "id_player_n": {"initial_card_id": "card id",
                                           "starting_points": "puntos al inicio",
                                           "ending_points": "puntos al final de partida"}}}

# player_game_round = {"round":{"id_player_1":{"is_bank":"0 ó 1","bet_points":"apuesta en la ronda",
# "starting_round_points":"puntos al inicio de la partida","cards_value":"puntos obtenido en la actual ronda",
# "endind_round_points":"puntos al final de la ronda"},...,{"id_player_n":{"is_bank":"0 ó 1","bet_points":"apuesta en
# la ronda", "starting_round_points":"puntos al inicio de la partida","cards_value":"puntos obtenido en la actual
# ronda", "endind_round_points":"puntos al final de la ronda"}
