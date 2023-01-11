from dictionaries import *


def addplayer():
    while True:
        answer = input("The new player is human? Y/y or N/n\nOption: ")
        while not answer or (answer.lower() != "y" or answer.lower() != "n"):
            answer = input("The new player is human? Y/y or N/n\nOption: ")

        new_player_name = input("New player name: ")
        new_player_name.split()

        while not new_player_name:
            new_player_name = input("New player name: ")
            new_player_name.split()

        new_player_behaviour = input("Choose new player behaviour:\n1)Cautious\n2)Moderated\n3)Bold\nOption: ")
        while new_player_behaviour not in [1, 2, 3]:
            print("Choose an option between 1, 2 or 3!")
            input("Press any key to continue")
            new_player_behaviour = input("Choose new player behaviour:\n1)Cautious\n2)Moderated\n3)Bold\nOption: ")

        if new_player_behaviour == 1:
            new_player_behaviour = "cautious"

        elif new_player_behaviour == 2:
            new_player_behaviour = "moderated"

        elif new_player_behaviour == 3:
            new_player_behaviour = "bold"

        if answer.lower() == "y":
            new_player_id = input("New player NIF: ")

            correct_id = False
            while not correct_id:
                while not new_player_id[:8].isdigit() and new_player_id[8:9].isalpha():
                    input("The first eight characters needs to be only numbers and the last a letter!"
                          "\nPress any key to continue")
                    new_player_id = input("New player NIF: ")

                if new_player_id in stored_players["humans"]:
                    input("This NIF already exists!\nPress any key to continue")
                    new_player_id = input("New player NIF: ")
                correct_id = True

            answer1 = input("Do you want to add this player? Y/y or N/n")
            while not answer1 or (answer1.lower() != "y" or answer1.lower() != "n"):
                answer1 = input("Do you want to add this player? Y/y or N/n")

            if answer1.lower() == "y":
                stored_players["humans"][new_player_id] = {"name": new_player_name, "behaviour": new_player_behaviour,
                                                           "earnings": 0, "games": 0, "minutes": 0}
                input("Player added successfully!\nPress any key to continue")

            elif answer1.lower() == "n":
                input("Player successfully not added!\nPress any key to continue")

        elif answer.lower() == "n":
            new_player_id = input("New bot ID: ")
            while new_player_id in stored_players["boots"]:
                input("This ID already exists!\nPress any key to continue")
                new_player_id = input("New bot ID: ")
            answer2 = input("Do you want to add this player? Y/y or N/n")
            while not answer2 or (answer2.lower() == "y" or answer2.lower() == "n"):
                answer2 = input("Do you want to add this player? Y/y or N/n")
            if answer2.lower() == "y":
                stored_players["boots"][new_player_id] = {"name": new_player_name, "behaviour": new_player_behaviour,
                                                          "earnings": 0, "games": 0, "minutes": 0}
            elif answer2.lower() == "n":
                input("Boot successfully not added!\nPress any key to continue")
        return


def addplayer2():
    while True:
        answer = input("The new player is human? Y/n\nOption: ").lower()
        while answer not in ["y", "n"]:
            answer = input("Invalid input. The new player is human? Y/n\nOption: ").lower()

        new_player_name = input("New player name: ").strip()
        while not new_player_name:
            new_player_name = input("Invalid input. New player name: ").strip()

        new_player_behaviour = input("Choose new player behaviour:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")
        while new_player_behaviour not in ["1", "2", "3"]:
            print("Invalid input. Choose an option between 1, 2, or 3.")
            new_player_behaviour = input("Choose new player behaviour:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")

        new_player_behaviour = ["cautious", "moderated", "bold"][int(new_player_behaviour) - 1]

        if answer == "y":
            while True:
                new_player_id = input("New player NIF: ")
                if not new_player_id[:8].isdigit() or not new_player_id[8:9].isalpha():
                    print(
                        "Invalid input. The first eight characters need to be only numbers and the last one a letter.")
                elif new_player_id in stored_players["humans"]:
                    print("This NIF already exists!")
                else:
                    break

            answer1 = input("Do you want to add this player? Y/n\nOption: ").lower()
            while answer1 not in ["y", "n"]:
                answer1 = input("Invalid input. Do you want to add this player? Y/n\nOption: ").lower()

            if answer1 == "y":
                stored_players["humans"][new_player_id] = {"name": new_player_name, "behaviour": new_player_behaviour,
                                                           "earnings": 0, "games": 0, "minutes": 0}
                print("Player added successfully!")
            else:
                print("Player not added.")

        elif answer == "n":
            while True:
                new_player_id = input("New bot ID: ")
                if new_player_id in stored_players["boots"]:
                    print("This ID already exists!")
                else:
                    break

            answer2 = input("Do you want to add this player? Y/n\nOption: ").lower()
            while answer2 not in ["y", "n"]:
                answer2 = input("Invalid input. Do you want to add this player? Y/n\nOption: ").lower()

            if answer2 == "y":
                stored_players["boots"][new_player_id] = {"name": new_player_name, "behaviour": new_player_behaviour,
                                                          "earnings": 0, "games": 0, "minutes": 0}
        return


def delplayer():
    while True:
        answer = input("The player you want to delete is human? y/n\nOption: ")
        while not answer.lower() == "y" or answer.lower() == "n":
            input("Pleas choose an option between y or n!\nPress any key to continue")
            answer = input("The player you want to delete is human? y/n\nOption: ")
        if answer.lower() == "y":
            option = input("1)Find by NIF\n2)Find by name\n3)Exit\nOption: ")
            while option not in [1, 2, 3]:
                input("Choose an option between 1, 2 or 3!\nPress any key to continue")
                option = input("1)Find by NIF\n2)Find by name\n3)Exit\nOption: ")
            if option == 1:
                while True:
                    search_nif = input("NIF to search: ")
                    while search_nif[:8].isdigit() and search_nif[8:9].isalpha():
                        input("The first eight characters needs to be only numbers and the last a letter!"
                              "\nPress any key to continue")
                        search_nif = input("NIF to search: ")
                    while search_nif not in stored_players["humans"]:
                        input("This NIF does not exist, please make sure is the right one!\nPress any key to continue")
                        search_nif = input("NIF to search: ")

                    answer = input("Are you sure you want to delete this player? y/n")
                    while not answer == "y" and answer == "n":
                        input("Choose an option between y/n!\nPress any key to continue")
                        answer = input("Are you sure you want to delete this player? y/n")
                    if answer.lower() == "y":
                        # look with search_nif in stored_players["humans"][search_nif] and delete all content
                        print()
                    elif answer.lower() == "n":
                        input("Player successfully not deleted!\nPress any key to continue")
                    break
            if option == 2:
                while True:
                    search_name = input("Name to search: ")
                    search_name = search_name.split()
                    while not search_name:
                        input("The name given must not be empty!\nPress any key to continue")
                        search_name = input("Name to search: ")
                    while search_name not in stored_players:
                        input("This name does not exist, please make sure is the right one!\nPress any key to continue")
                        search_name = input("Name to search: ")
                    answer = input("Are you sure you want to delete this boot? y/n")
                    while not answer == "y" and answer == "n":
                        input("Choose an option between y/n!\nPress any key to continue")
                        answer = input("Are you sure you want to delete this player? y/n")
                    if answer.lower() == "y":
                        # look with search_id in stored_players["humans"][key][search_name] and delete all content
                        print()
                    elif answer.lower() == "n":
                        input("Player successfully not deleted!\nPress any key to continue")
                    break

        if answer.lower() == "n":
            option = input("1)Find by NIF\n2)Find by name\n3)Exit\nOption: ")
            while option not in [1, 2, 3]:
                input("Choose an option between 1, 2 or 3!\nPress any key to continue")
                option = input("1)Find by ID\n2)Find by name\n3)Exit\nOption: ")

            if option == 1:
                search_id = input("ID to search: ")
                while search_id not in stored_players["boots"]:
                    input("This ID does not exist, please make sure is the right one!\nPress any key to continue")
                    search_id = input("ID to search: ")
                answer = input("Are you sure you want to delete this boot? y/n")
                while not answer == "y" and answer == "n":
                    input("Choose an option between y/n!\nPress any key to continue")
                    answer = input("Are you sure you want to delete this player? y/n")
                if answer.lower() == "y":
                    # look with search_id in stored_players["boots"][search_id] and delete all content
                    print()
                elif answer.lower() == "n":
                    input("Player successfully not deleted!\nPress any key to continue")
                break

            if option == 2:
                while True:
                    search_name = input("Name to search: ")
                    search_name = search_name.split()
                    while not search_name:
                        input("The name given must not be empty!\nPress any key to continue")
                        search_name = input("Name to search: ")
                    while search_name not in stored_players:
                        input("This name does not exist, please make sure is the right one!\nPress any key to continue")
                        search_name = input("Name to search: ")
                    answer = input("Are you sure you want to delete this boot? y/n")
                    while not answer == "y" and answer == "n":
                        input("Choose an option between y/n!\nPress any key to continue")
                        answer = input("Are you sure you want to delete this boot? y/n")
                    if answer.lower() == "y":
                        # look with search_id in stored_players["boots"][key][search_name] and delete all content
                        print()
                    elif answer.lower() == "n":
                        input("Boot successfully not deleted!\nPress any key to continue")
                    break


# def playGame():
"""Esta es la función principal del proyecto. Una vez establecido el número de rondas, la baraja
con la que se va a jugar, y los jugadores que participan en la partida, ésta será la función
que gestione toda la partida. Para ello, hará uso de otras funciones auxiliares como:"""

# def setGamePriority(mazo):
"""Esta función establece las prioridades de los jugadores.
Se recibe una lista con los id’s de la baraja (mazo), se mezclan, se reparte una carta a
cada jugador, se ordenan la lista de jugadores de la partida (contextGame[“game”])
según la carta que han recibido, y se establecen las prioridades."""

# def resetPoints():
"""Función que establece los 20 puntos iniciales en todos los jugadores."""

# def fill_player_game(player_game,gameID,*fields):
"""Función para insertar datos en el diccionario player_game"""

# def fill_player_game_round(player_game_round,round,*fields):
"""Función para insertar datos en el diccionario player_game_round"""

# def checkMinimun2PlayerWithPoints():
"""Función que verifica que al menos haya dos jugadores con puntos."""

# def orderAllPlayers():
"""Función que ordena los jugadores de la partida (contextGame[“game”]) de forma que
pone la banca al principio y el resto de jugadores después, ordenados según prioridad"""

# def setBets():
"""Función que establece las apuestas de cada jugador en función del tipo de jugador."""

# def standarRound(id, mazo):
"""Función que realiza la tirada de cartas de un jugador en función del tipo de jugador
que es y teniendo en cuenta si el jugador es banca o no."""

# def humanRound(id, mazo):
"""Función que gestiona la tirada de un jugador humano. Nos muestra el menú de
opciones:
1)View Stats
2)View Game Stats
3)Set Bet
4)Order Card
5)Automatic Play
6)Stand
Option:
Y ejecuta la acción que elijamos"""

# def distributionPointAndNewBankCandidates():
"""Función que realiza el reparto de puntos una vez finalizada una ronda y devuelve una
lista con los candidatos a la banca ( los que tienen 7,5)"""

# def printStats(idPlayer="", titulo=""):
"""Esta función nos imprime los stats de todos los jugadores de la partida:
***********************************************************************************************************************************************************

                                                            Seven and Half

******************************************************** Round 0 , Turn of Mario **************************************************************************

Name                  Boot2                                Boot1                                    Mario
Human                 False                                False                                    True
Priority              1                                    2                                        3
Type                  30                                   40                                       40
Bank                  False                                False                                    True
Bet                   6                                    8                                        8
Points                20                                   20                                       20
Cards                 O01;O10;B02                          E07                                      C07
Roundpoints           3.5                                  7.0                                      7.0
"""

# def orderPlayersByPriority(listaJugadores):
"""Ordenamos la lista de jugadores de la partida (contextGame[“game”]) según prioridad."""

# def printWinner():
"""Función que muestra el ganador de la partida:
***********************************************************************************************************************************************************

                                                                Game Over
  
***********************************************************************************************************************************************************
                                          The winner is 11115555A - Mario, in 2 rounds, with 44 points
                                          Enter to continue
"""

# def insertBBDDCardgame(cardgame):
"""Función que guarda un nuevo registro en la tabla cardgame.
Esta función debería llamarse justo después de acabar una partida."""

# def insertBBDD_player_game(player_game,cardgame_id):
"""Función que guarda en la tabla player_game de la BBDD el diccionario player_game.
Esta función debería llamarse justo después de acabar una partida"""

# def insertBBDD_player_game_round(player_game_round,cardgame_id):
"""Función que guarda en la tabla player_game_round de la BBDD el diccionario
player_game_round.
Esta función debería llamarse justo después de acabar una partida.
Una posible estrategia para esta función sería:

Establecer prioridades de los jugadores
Resetear puntos
Crear diccionarios cardgame,player_game,player_game_round
Crear un id de partida
Mientras hayan dos jugadores o más con puntos, y no nos pasemos del máximo de rondas:
  
ordenar jugadores, banca al final y resto de prioridad menor a mayor.
Crear una lista con los id’s de cartas ( mazo).
Barajar el mazo.
Establecer apuestas
Ejecutar jugadas de cada jugador.
Repartir puntos.
Eliminar los jugadores sin puntos.
Establecer nueva banca si es necesario.
Insertar en BBDD los diccionarios creados para tal propósito.
Mostrar el ganador."""

# def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):
"""Función para la gestión de menús. Le pasamos un texto, que nos mostrará un menú, un
rango de opciones válidas, y una lista de excepciones, y nos devuelve la opción elegida por el
usuario."""

# def orderPlayersByPoints(listaJugadores):
"""Función que ordena los jugadores según sus puntos."""

# def chanceExceedingSevenAndHalf(id, mazo):
"""Función que calcula la probabilidad de pasarse de siete y medio"""

# def printPlayerStats(id):
"""Esta función nos muestra los stats de un jugador humano.
    name Mario
    type 40
    human True
    bank True
    initialCard E11
    priority 3
    bet 8
    points 20
    cards C07
    roundPoints 0
"""

# def logToFile(text):
"""Esta función nos puede servir para enviar mensajes de texto al archivo
“logFileSevenAndHalf”, que puede sernos útil a modo de debug.
      f = open("logfileSevenAndHalf.txt", "a")
      f.write(text)
      f.close()
"""

# def baknOrderNewCard(id, mazo):
"""Función que evalúa si la banca pedirá una nueva carta."""

# def newPlayer(dni, name, profile, human):
"""Función que devuelve una tupla con dos elementos, el primero es el dni del nuevo jugador, el
segundo, un diccionario con las claves: name, human, bank, initialCard, priority, type, bet,
points, ards, roundPoints"""

# def addRemovePlayers():
"""Función que nos muestra el menú despues de escoger la opción 1 del menu principal:
  1)New Human Player
  2)New Boot
  3)Show/Remove Players
  4)Go back
Option:
"""

# def settings():
"""Función que gestiona el menú settings, donde podemos establecer los jugadores que
participarán en una partida, la baraja con la que se va a jugar y el número máximo de
rondas."""

# def setMaxRounds():
"""Función que pide al usuario el número de rondas de la siguiente partida y lo establece en el
diccionario contextGame, contextGame[“maxRounds”]"""

# def newRandomDNI():
"""Función que devuelve un dni válido con números aleatorios"""

# def setNewPlayer(human=True):
"""Función que gestiona la creación de un nuevo jugador que insertaremos en la BBDD"""

# def showPlayersGame():
"""Función que muestra los jugadores seleccionados cuando estamos añadiendo jugadores a la
partida:
********************Actual Players In Game********************
11111111A    Boot1               Boot      Moderated
22222222A    Boot2               Boot      Cautious
11115555A    Mario               Human     Moderated
"""

# def setPlayersGame():
"""Función para establecer los jugadores que conformarán la partida siguiente"""

# def removeBBDDPlayer():
"""Función que nos muestra los jugadores disponibles en BBDD, y elimina el que seleccionemos"""

# def reports():
"""Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente"""

# def getPlayers():
"""Función que extrae los jugadores definidos en la BBDD y los almacena en el diccionario
contextGame[“players”]"""

# def setCardsDeck():
"""Elegimos una baraja, y a partir de esa baraja, establecemos el diccionario de cartas
contextGame["cards_deck"]"""

# def savePlayer(nif,name,risk,human):
"""Función que guarda en BBDD un nuevo jugador."""

# def delBBDDPlayer(nif):
"""Función que elimina un jugador de la BBDD"""

# def getGameId():
"""Función que devuelve un id no existente en la tabla cardgame."""

# def getBBDDRanking():
"""Función que crea la vista player_earnings, y retorna un diccionario con los datos de ésta,
player_id | earnings | games_played | minutes_played."""

# def ranking():
"""Función queMuestra el menú del ranking y el ranking según la opción elegida"""

# def returnListRanking(field="earnings"):
"""Función que retorna una lista con los id de jugadores del diccionario que retorna la función
getBBDDRanking(), ordenados según la opción del ranking elegida"""
