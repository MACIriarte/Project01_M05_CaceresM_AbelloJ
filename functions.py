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
        menu = "\n\n\n" + "*"*140+"\n\n"+"\tPlayers ID\t\t\t\tPlayers name\t\t\t\tPlayers behaviour\n\n"
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


def setplayers(dictionary="players_dict"):
    flg_1 = True
    flg_2 = False
    while True:
        while flg_1:
            add_player = input("Player ID to add: ")
            try:
                with connection.cursor() as cursor:
                    sql = f"SELECT player_id, player_name, player_risk, is_human FROM player WHERE player_id = '{add_player}'"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    if result:
                        player_id = result["player_id"]
                        player_name = result["player_name"]
                        player_risk = result["player_risk"]
                        is_human = result["is_human"]
                        if player_risk == 1:
                            player_risk = "Cautious"
                        elif player_risk == 2:
                            player_risk = "Moderate"
                        elif player_risk == 3:
                            player_risk = "Bold"
                        elif player_risk == 4:
                            player_risk = "Dev"
                        players_dict[player_id] = {"name": player_name, "behaviour": player_risk, "human": is_human}
                        input("Player successfully added!\nPress any key to continue")
                    else:
                        input("Player with the given ID not found! Please make sure the ID is correct\nPress any key to continue")
            except Exception as e:
                print(f"An error occurred: {e}")
            flg_1 = False
            flg_2 = True
        while flg_2:
            option = input("Add one more player? y/n\nOption: ")
            while not (option.lower() == "y" or option.lower() == "n"):
                option = input("Please choose between y/n\nAdd one more player? y/n\nOption: ")
            if option.lower()=="y":
                flg_2 = False
                flg_1 = True
            elif option.lower()=="n":
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

        while flg03:
            # check if value of the column "players" of table "cardgame" is equals to 2 or greater
            # if not then
            input("You must set players first! Please add players on settings!\nPress any key to continue")
            flg03 = False
            flg00 = True
            # if the value of the column "players" of table "cardgame" is equals to 2 or greater then
            playGame()


def playGame():
