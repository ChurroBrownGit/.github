# WELCOME TO JOEL'S CRAPPY CODE!!!

# how to timeline
#1. game menu - DONE
    #1.1 select number of players - DONE
    #1.2 bots on/off - DONE
    #1.3 set names - DONE
#2. setup new game
    #2.1 show instructions - DONE
    #2.2 pick starting player - DONE
    #2.3 deal starting card to each player
#3 play game (player turns) :|
    #3.1 starting player turn
    #3.2 next player
    #3.3 take turn
    #3.4 check if game is won - else go to next player
#4 who wins?
    #4.1 show winner and how many cards other players had

import json
import random

def timeline():
    print("Starting New Game...")
    player_count, cards = showGamemenu()
    botsOn = botSetup(player_count)
    player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name, botsOn, player_count = playernames(player_count, botsOn)
    begin, firstturnplayer, players = instructions(player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    deck = shuffledeck(cards)
    player1cards, player2cards, player3cards, player4cards, player5cards, player6cards, player7cards, player8cards, card, is_game_over = play(firstturnplayer, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name, botsOn, cards, deck, player_count, players)
    position = is_valid_placement(player1cards, player2cards, player3cards, player4cards, player5cards, player6cards, player7cards, player8cards, card)
    winner(is_game_over)

def showGamemenu(): #COMPLETE
    ("Welcome to Timeline!")
    player_count = int(input("How many players are playing? "))    
    cards = []
    with open('cards.json') as f:
        cards = json.load(f)
    return player_count, cards

def botSetup(player_count): #COMPLETE
    botsyaynay = input("Would you like to add bots to fill in for empty player spots? (Y/N) ")
    if botsyaynay.lower() == "y":
        botsOn = True
    if botsyaynay.lower() == "n":
        botsOn = False
    return botsOn

def playernames(player_count, botsOn): #COMPLETE
    if player_count == 1 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = "Bot 1"
        player3name = "Bot 2"
        player4name = "Bot 3"
        player5name = "Bot 4"
        player6name = "Bot 5"
        player7name = "Bot 6"
        player8name = "Bot 7"
    if player_count == 1 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = 0
        player3name = 0
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
    if player_count == 2 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = "Bot 1"
        player4name = "Bot 2"
        player5name = "Bot 3"
        player6name = "Bot 4"
        player7name = "Bot 5"
        player8name = "Bot 6"
    if player_count == 2 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = 0
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
    if player_count == 3 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = "Bot 1"
        player5name = "Bot 2"
        player6name = "Bot 3"
        player7name = "Bot 4"
        player8name = "Bot 5"
    if player_count == 3 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
    if player_count == 4 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = "Bot 1"
        player6name = "Bot 2"
        player7name = "Bot 3"
        player8name = "Bot 4"
    if player_count == 4 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
    if player_count == 5 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = "Bot 1"
        player7name = "Bot 2"
        player8name = "Bot 3"
    if player_count == 5 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = 0
        player7name = 0
        player8name = 0
    if player_count == 6 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = "Bot 1"
        player8name = "Bot 2"
    if player_count == 6 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = 0
        player8name = 0
    if player_count == 7 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = "Bot 1"
    if player_count == 7 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = 0
    if player_count == 8:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = input("What would you like to name player 8? ")
    return player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name, botsOn, player_count

def instructions(player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name): #COMPLETE
    print("Playing")
    instructions1 = input("Before we begin, would you like to read the instructions? (Y/N) ")
    if instructions1.lower() == "y":
        print("This is Timeline, a game where you must organize your cards in the correct order. Each player will start with one 'card'. The card will have information about a subject and a year on it. ")
        print("A card will be randomly picked from a deck of the remaining cards. A random player will be picked to play first. You will see a card with no year, and must decide if that card's year is before ")
        print("or after the year you have on your card. If you guess correctly, you keep the card. If you don't correctly guess, the card will go to the next person until someone guesses right. ")
        print("As time goes on, you must choose where a card is with multiple of your own cards, and it could be inbetween, before, or after any of the cards. The main goal is to get 10 cards.")
        print("First player to have 10 correctly ordered cards wins.")
        begin = input("Ready to start? (Y/N) ")
        if begin.lower() == "y":
            seats = [player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name]
            players = []
            for item in seats:
                if item != 0:
                    players.append(item)
            print(players)
            firstturnplayer = random.choice(players)
            print(firstturnplayer)
            print(str(firstturnplayer) + " will have the first turn.")
        elif begin.lower() == "n":
            instructions(player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if instructions1.lower() == "n":
        begin = input("Ready to start? (Y/N) ")
        if begin.lower() == "y":
            seats = [player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name]
            players = []
            for item in seats:
                if item != 0:
                    players.append(item)
            firstturnplayer = random.choice(players)
            print(str(firstturnplayer) + " will have the first turn.")
        elif begin.lower() == "n":
            instructions(player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    return begin, firstturnplayer, players

def shuffledeck(cards): #COMPLETE
    random.shuffle(cards)
    return cards

def play(firstturnplayer, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name, botsOn, cards, deck, player_count, players):
    print("Playing Game")
    player1cards = []
    player2cards = []
    player3cards = []
    player4cards = []
    player5cards = []
    player6cards = []
    player7cards = []
    player8cards = []
    for item in range(1):
        card = deck.pop()
        player1cards.append(card)
        #PRINTS ALL THE CARDS OR WHATEVER IDK
        show_player1_cards = print(player1cards["title"])
        show_player2_cards = print(player2cards["title"])
        show_player3_cards = print(player3cards["title"])
        show_player4_cards = print(player4cards["title"])
        show_player5_cards = print(player5cards["title"])
        show_player6_cards = print(player6cards["title"])
        show_player7_cards = print(player7cards["title"])
        show_player8_cards = print(player8cards["title"])
    #PLAYER 1 CARD CHECK (The others can suck it)
    if len(player1cards) == 20:
        print("Ending game.")
        is_game_over = True
        return player1cards, player2cards, player3cards, player4cards, player5cards, player6cards, player7cards, player8cards 
    else:
        print(player1name + " has " + len(player1cards) + ". Keep Playing!")
        is_game_over = False
    if is_game_over == True:
        return is_game_over
    else:
        return is_game_over

def is_valid_placement(player1cards, player2cards, player3cards, player4cards, player5cards, player6cards, player7cards, player8cards, card, position):
    print(card["title"])
    print(player1cards)
    cardinputs = input("Left or Right of this card?")
    if cardinputs == "left".lower():
        if card(["year"]) < player1cards[1]["year"]:
            return False
        else:
            return True
    if cardinputs == "right".lower():
        if card(["year"]) > player1cards[1]["year"]:
            return False
    else:
        return True


def winner(is_game_over):
    print("The winner is: ")


timeline()