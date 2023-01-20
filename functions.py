import random
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    db='db_game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

from dictionaries import *


def addplayerdb():
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

        if answer == "y":
            while True:
                new_player_id = input("New player NIF: ")
                if not new_player_id[:8].isdigit() or not new_player_id[8:9].isalpha():
                    print(
                        "Invalid input. The first eight characters need to be only numbers and the last one a letter.")
                with connection.cursor() as cursor:
                    sql = "SELECT player_id FROM player WHERE player_id = %s"
                    cursor.execute(sql, (new_player_id,))
                    result = cursor.fetchone()
                    if result:
                        print("This ID already exists!")
                        continue

            answer1 = input("Do you want to add this player? Y/n\nOption: ").lower()
            while answer1 not in ["y", "n"]:
                answer1 = input("Invalid input. Do you want to add this player? Y/n\nOption: ").lower()

            if answer1 == "y":
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO player (player_name, player_risk, player_id, human) VALUES (%s, %s, %s, %s)",
                            (new_player_name, new_player_behaviour, new_player_id, 1))
                        connection.commit()
                        print("Player added successfully!")
                except Exception as e:
                    print(f"An error occurred: {e}")

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
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO player (player_name, player_risk, player_id, human) VALUES (%s, %s, %s, %s)",
                            (new_player_name, new_player_behaviour, new_player_id, 0))
                        connection.commit()
                        print("Player added successfully!")
                except Exception as e:
                    print(f"An error occurred: {e}")

            if answer2 == "n":
                print("Player not added.")

        return


def delete_player(player_id):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM player WHERE player_id = {player_id}"
            cursor.execute(sql)
            connection.commit()
            print(f"Player with ID {player_id} has been deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")


def showplayersdb():
    offset = 0
    limit = 10
    while True:
        menu = "\n\n\n" + "*" * 140 + "\n\n" + "\tPlayers ID\t\t\t\tPlayers name\t\t\t\tPlayers behaviour\n\n"
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT player_id, player_name, player_risk FROM player LIMIT {limit} OFFSET {offset}"
                cursor.execute(sql)
                result = cursor.fetchall()
                for player in result:
                    player_id = player["player_id"]
                    player_name = player["player_name"]
                    player_risk = player["player_risk"]
                    if player_risk == 1:
                        player_risk = "Cautious"
                    elif player_risk == 2:
                        player_risk = "Moderate"
                    elif player_risk == 3:
                        player_risk = "Bold"
                    elif player_risk == 4:
                        player_risk = "Dev"
                    menu += f"\t{player_id}\t\t\t\t{player_name}\t\t\t\t{player_risk}\n"
        except Exception as e:
            print(f"An error occurred: {e}")

        print(menu)
        option = input("\t\t+ to display more players, - to display less players, exit to go back\n\t\tOption: ")
        if option == "+":
            offset += limit
            print("+ option selected")
        elif option == "-":
            if offset >= limit:
                offset -= limit
            print("- option selected")
        elif option[:2].lower() == "del" and (len(option) == 13 and option[3:11].isdigit() and option[11:12].isalpha()):
            player_id = int(option[3:11])
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT player_id, player_name FROM player WHERE player_id = {player_id}")
                result = cursor.fetchone()
                if result:
                    player_name = result["player_name"]
                    delete_player = input(
                        f"Are you sure you want to delete this player? y/n\n{player_id}\n{player_name}\nOption: ")
                    if delete_player.lower() == "y":
                        delete_player(player_id)
                        input("Player successfully deleted!\nPress any key to continue")
                        continue
                    if delete_player.lower() == "n":
                        input("Player not deleted!\nPress any key to continue")

        elif option.lower() == "exit":
            input("\nPress any key to continue".rjust(55))
            return


def setplayers():
    flg_1 = True
    flg_2 = False
    while True:
        while flg_1:
            add_player = input("Player ID to add: ")
            try:
                with connection.cursor() as cursor:
                    sql = f"SELECT player_id, player_name, player_risk, human FROM player WHERE player_id = '{add_player}'"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    if result:
                        player_id = result["player_id"]
                        player_name = result["player_name"]
                        player_risk = result["player_risk"]
                        human = result["human"]
                        if player_risk == 1:
                            player_risk = "Cautious"
                        elif player_risk == 2:
                            player_risk = "Moderate"
                        elif player_risk == 3:
                            player_risk = "Bold"
                        elif player_risk == 4:
                            player_risk = "Dev"
                        players_dict[player_id] = {"name": player_name, "behaviour": player_risk, "bet": 0,
                                                   "human": human,
                                                   "points": 40, "bank": False}
                        input("Player successfully added!\nPress any key to continue")
                        with connection.cursor() as cursor:
                            cursor.execute("UPDATE cardgame SET players = players + 1")
                            connection.commit()
                    else:
                        input(
                            "Player with the given ID not found! Please make sure the ID is correct\nPress any key to continue")
            except Exception as e:
                print(f"An error occurred: {e}")
            flg_1 = False
            flg_2 = True
        while flg_2:
            option = input("Add one more player? y/n\nOption: ")
            while not (option.lower() == "y" or option.lower() == "n"):
                option = input("Please choose between y/n\nAdd one more player? y/n\nOption: ")
            if option.lower() == "y":
                flg_2 = False
                flg_1 = True
            elif option.lower() == "n":
                # exit
                return players_dict


def mainprogram():
    option = ""
    menu00 = "\n\n\n" + "*" * 140 + "\n" + \
             "\n_____".rjust(37) + "___".rjust(25) + "__".rjust(14) + "__".rjust(3) + "__".rjust(2) + "______".rjust(
        6) + \
             "\n/ ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/".rjust(36) + \
             "\n\__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /_".rjust(36) + \
             "\n___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/".rjust(35) + \
             "\n/____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/".rjust(34) + \
             "\n ______     _                   _______                      _             _   _ _ _       ".rjust(25) + \
             "\n|  ____|   | |                 |__   __|                    | |           (_) (_) | |      ".rjust(25) + \
             "\n| |__   ___| |_ _____   _____     | | ___ _ __ _ __ __ _  __| | __ _ ___   _   _| | | __ _ ".rjust(25) + \
             "\n|  __| / __| __/ _ \ \ / / _ \    | |/ _ \ '__| '__/ _` |/ _` |/ _` / __| | | | | | |/ _` |".rjust(25) + \
             "\n| |____\__ \ ||  __/\ V /  __/    | |  __/ |  | | | (_| | (_| | (_| \__ \ | | | | | | (_| |".rjust(25) + \
             "\n|______|___/\__\___| \_/ \___|    |_|\___|_|  |_|  \__,_|\__,_|\__,_|___/ |_| |_|_|_|\__,_|".rjust(25) + \
             "\n\n" + \
             "*" * 140 + \
             "\n" + "1)Add/Remove/Show Players".rjust(55) + \
             "\n" + "2)Settings".rjust(55) + \
             "\n" + "3)Play Game".rjust(55) + \
             "\n" + "4)Ranking".rjust(55) + \
             "\n" + "5)Reports".rjust(55) + \
             "\n" + "6)Exit".rjust(55)

    menu01 = "\n\n\n" + "*" * 140 + "\n" + \
             "\n____".rjust(34) + "____".rjust(3) + "____".rjust(3) + "____".rjust(3) + "____".rjust(5) + "__".rjust(
        3) + \
             "\n/ __ ) / __ ) / __ \ / __ \   / __ \ / /____ _ __  __ ___   _____ _____".rjust(33) + \
             "\n/ __  |/ __  |/ / / // / / /  / /_/ // // __ `// / / // _ \ / ___// ___/".rjust(32) + \
             "\n/ /_/ // /_/ // /_/ // /_/ /  / ____// // /_/ // /_/ //  __// /   (__  )".rjust(31) + \
             "\n/_____//_____//_____//_____/  /_/    /_/ \__,_/ \__, / \___//_/   /____/".rjust(30) + \
             "\n/____/".rjust(77) + "\n" + "\n" + \
             "*" * 140 + "\n\n" + "1)New Human Player".rjust(55) + \
             "\n2)New Boot".rjust(55) + \
             "\n3)Show/Remove Players".rjust(55) + \
             "\n4)Go back".rjust(55)

    menu11 = "\n\n\n" + "*" * 140 + "\n" + \
             "\n_   __                  __  __                                   ____   __".rjust(22) + \
             "\n/ | / /___  _      __   / / / /__  __ ____ ___   ____ _ ____     / __ \ / /____ _ __  __ ___   _____".rjust(
                 21) + \
             "\n/  |/ // _ \| | /| / /  / /_/ // / / // __ `__ \ / __ `// __ \   / /_/ // // __ `// / / // _ \ / ___/".rjust(
                 20) + \
             "\n/ /|  //  __/| |/ |/ /  / __  // /_/ // / / / / // /_/ // / / /  / ____// // /_/ // /_/ //  __// /".rjust(
                 19) + \
             "\n/_/ |_/ \___/ |__/|__/  /_/ /_/ \__,_//_/ /_/ /_/ \__,_//_/ /_/  /_/    /_/ \__,_/ \__, / \___//_/".rjust(
                 18) + \
             "\n/____/".rjust(100) + \
             "\n\n\n" + "*" * 140 + "\n\n"

    flg00 = True
    flg01 = False
    flg02 = False
    flg03 = False
    flg04 = False
    flg05 = False

    while option.upper() == "EXIT":
        while flg00:
            option = input(menu00 + "\nOption: ")
            while option not in [1, 2, 3, 4, 5, 6]:
                input("The option given must be between 1 and 6!".rjust(55) + "\nPress any key to continue".rjust(55))
                option = input(menu01 + "\nOption: ".rjust(55))
            else:
                option = int(option)
                if option == 1:
                    # 1)Add/Remove/Show Players
                    flg00 = False
                    flg01 = True
                elif option == 2:
                    # 2)Settings
                    flg00 = False
                    flg02 = True
                elif option == 3:
                    # 3)Play Game
                    flg00 = False
                    flg03 = True
                elif option == 4:
                    # 4)Ranking
                    flg00 = False
                    flg04 = True
                elif option == 5:
                    # 5)Reports
                    flg00 = False
                    flg05 = True
                elif option == 6:
                    # exit
                    return
        while flg01:
            # bbdd players menu
            option = input(menu01 + "Option: ".rjust(57))
            while option not in [1, 2, 3]:
                option = input(menu01 + "Option: ".rjust(57))
            else:
                option = int(option)
                if option == 1:
                    addplayerdb()
                elif option == 2:
                    # show/remove players
                    showplayersdb()
                elif option == 3:
                    # go back
                    flg01 = False
                    flg00 = True

        while flg02:
            # settings menu
            menu02 = "1)Set game players\n2)Set cards deck\n3)Set max rounds\n4)Go back"
            option = input(menu02 + "\nOption: ")
            while option not in [1, 2, 3, 4]:
                input("The option given must be between 1 and 4!".rjust(55) + "\nPress any key to continue".rjust(55))
                option = input(menu01 + "\nOption: ".rjust(55))
            else:
                option = int(option)
                if option == 1:
                    # set gamers function
                    setplayers()
                elif option == 2:
                    # set cards deck function
                    setDeck()
                elif option == 3:
                    # set max rounds function
                    setMaxRounds()
                elif option == 4:
                    # go back
                    flg02 = False
                    flg00 = True

        while flg03:
            with connection.cursor() as cursor:
                cursor.execute("SELECT players FROM cardgame WHERE players >= 2")
                result = cursor.fetchone()
                if result is None:
                    input("You must set players first! Please add players on settings!\nPress any key to continue")
                    flg03 = False
                    flg00 = True
                else:
                    playGame()


def setDeck():
    option = input("Which deck you want to use in the game?\nspn = Spanish deck or eng = English deck?\nOption: ")
    while not option.lower() == "spn" or option.lower() == "eng":
        input("Please choose between spn/eng\nPress any key to continue")
        option = input("Which deck you want to use in the game?\nspn = Spanish deck or eng = English deck?\nOption: ")
    if option.lower() == "spn":
        # game_settings = {"roundlimit":{"active":True,"rounds":5},"deck":{"spn_cards":True,"eng_cards":False}
        # }
        game_settings["deck"]["spn_cards"] = True
        game_settings["deck"]["eng_cards"] = False

    elif option.lower() == "eng":
        # game_settings = {"roundlimit":{"active":True,"rounds":5},"deck":{"spn_cards":False,"eng_cards":True}
        # }
        game_settings["deck"]["eng_cards"] = True
        game_settings["deck"]["spn_cards"] = False
    return


def setMaxRounds():
    while True:
        option = input("How many rounds do you want as maximum in the game?\nWrite none if you dont want a maximum"
                       "\nOption: ")
        if option.lower() == "none":
            game_settings["roundlimit"]["active"] = False
            continue
        while not option.isdigit() and int(option) > 0 or option.lower() == "none":
            input(
                "Please enter a valid number of rounds or write none to not set a maximum!\nPress any key to continue")
            option = input("How many rounds do you want as maximum in the game?\nOption: ")
        else:
            option = int(option)
            game_settings["roundlimit"]["rounds"] = option
            return


def playGame():
    while True:
        # setDeckGame() to prepare the deck for the game
        setDeckGame()
        # listAllPlayers to list all players into a custom display
        listAllPlayers()
        input("This is the first round where the order of cards given to each player will be decided"
              "\nPress any key to continue")
        # firstRound() to decide the order in which the cards will be given to the players
        firstRound()


def firstRound():
    with connection.cursor() as cursor:
        for player_id, player_data in players_dict.items():
            sql = "INSERT INTO player_game_round (round_num, player_id, is_bank, bet_points, starting_points) VALUES (%s, %s, %s, %s, %s)"
            is_bank = 1 if player_data["bank"] else 0
            cursor.execute(sql, (1, player_id, is_bank, player_data["bet"], player_data["points"]))
        connection.commit()

    players_cards = {player_id: [] for player_id in players_dict.items()}

    for player in players_dict.items():
        card = random.choice([card_id for card_id in deck_game.keys() if card_id not in players_cards[player]])
        players_cards[player].append(card)

    playersOrder = []
    for player, cards in players_cards.items():
        realvalue = deck_game[cards[0]]["realvalue"]
        priority = deck_game[cards[0]]["priority"]
        playersOrder.append((player, realvalue, priority))

    playersOrder.sort(key=lambda x: (-x[1], -x[2]))
    global players_cards, playersOrder
    return players_cards, playersOrder

def setDeckGame():
    # game_settings = {"roundlimit":{"active":True,"rounds":5},"deck":{"spn_cards":True,"eng_cards":False}}
    if game_settings["deck"]["spn_cards"] == True and game_settings["deck"]["eng_cards"] == False:
        with connection.cursor() as cursor:
            # Select all rows from the 'card' table where 'deck_id' equals 'spn'
            sql = "SELECT card_id, card_name, card_value, card_priority, card_real_value FROM card WHERE deck_id = 'spn'"
            cursor.execute(sql)
            result = cursor.fetchall()
            deck_game = {}
            # Iterate through the selected rows and add them to the dictionary
            for row in result:
                card_id = row['card_id']
                card_name = row['card_name']
                card_value = row['card_value']
                card_priority = row['card_priority']
                card_real_value = row['card_real_value']
                deck_game[card_id] = {"cardname": card_name, "value": card_value, "priority": card_priority,
                                      "realvalue": card_real_value}
            global deck_game
    return deck_game


def listAllPlayers():
    display_players = "\n\n\n" + "*" * 140 + "\n\n\tName\t\t\tPoints\t\tBehaviour\t\tBet\t\tBank\n\n"
    for player_id, player_info in players_dict.items():
        display_players += "\n\n\t{}\t\t\t{}\t\t{}\t\t{}\t\t{}\n\n".format(
            player_info["name"], player_info["points"], player_info["behaviour"], player_info["bet"],
            player_info["bank"])
        display_players += "*" * 140 + "\n\n"
    print(display_players)
    return display_players

def cardsBetRepartition():
    for player_id in players_dict:
        if players_dict[player_id]["human"] == True or players_dict[player_id]["human"] == 1:
            # the player is human, so ask them to make a bet
            make_bet = input("How much do you want to bet this round? You have available {} points!\nBet: "
                             .format(str(players_dict[player_id]["points"])))
            players_dict[player_id]["bet"] = int(make_bet)
        else:
            # the player is a bot, so determine the likelihood of making a higher bet based on the "behaviour" value
            if players_dict[player_id]["behaviour"] == 1:
                likelihood = 0.3
            elif players_dict[player_id]["behaviour"] == 2:
                likelihood = 0.5
            else:
                likelihood = 0.7
            if random.random() < likelihood:
                # make a high bet
                make_bet = players_dict[player_id]["points"]/2 + random.randint(0, players_dict[player_id]["points"]/4)
            else:
                # make a low bet
                make_bet = random.randint(0, players_dict[player_id]["points"]/2)
            players_dict[player_id]["bet"] = int(make_bet)

    for player in playersOrder:
        players_cards[player] = []
        if players_dict[player]["human"] == False or players_dict[player]["human"] == 0:
            # the player is a bot
            if players_dict[player]["behaviour"] == 1:
                likelihood = 0.3
            elif players_dict[player]["behaviour"] == 2:
                likelihood = 0.5
        else:
            likelihood = 0.7
        card_count = 0
        while (random.random() < likelihood) and (card_count <= 7.5):
            # pick a random card from the deck
            card_id = random.choice([card_id for card_id in deck_game if card_id not in players_cards[player]])
            players_cards[player].append(card_id)
            card_count += deck_game[card_id]["realvalue"]
        players_dict[player]["points"] -= players_dict[player]["bet"]
        else:
            # the player is human
            card_count = 0
        while True:
            option = input("Do you want to pick another card? y/n \nOption: ")
            if option.lower() == "y":
                # pick a random card from the deck
                card_id = random.choice([card_id for card_id in deck_game if card_id not in players_cards[player]])
                players_cards[player].append(card_id)
                card_count += deck_game[card_id]["realvalue"]
                # check if player's cards total value is less than 7.5
                if card_count > 7.5:
                    print("You cannot pick another card, your cards total value is greater than 7.5")
                    break
            else:
                break
        players_dict[player]["points"] -= players_dict[player]["bet"]
