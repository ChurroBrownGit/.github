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

import random

def timeline():
    print("Starting New Game...")
    showGamemenu()

def showGamemenu():
    ("Welcome to Timeline!")
    player_count = int(input("How many players are playing? "))
    if int(player_count) < 8:
        botSetup(player_count)
    else:
        playernames(player_count, 1)
    if int(player_count) > 8:
        print("Only 8 players are allowed.")
        showGamemenu()

def botSetup(player_count):
    botsyaynay = input("Would you like to add bots to fill in for empty player spots? (Y/N) ")
    if botsyaynay.lower() == "y":
        botsOn = True
        playernames(player_count, botsOn)
    if botsyaynay.lower() == "n":
        botsOn = False
        playernames(player_count, botsOn)

def playernames(player_count, botsOn):
    if player_count == 1 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = "Bot 1"
        player3name = "Bot 2"
        player4name = "Bot 3"
        player5name = "Bot 4"
        player6name = "Bot 5"
        player7name = "Bot 6"
        player8name = "Bot 7"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 1 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = 0
        player3name = 0
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 2 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = "Bot 1"
        player4name = "Bot 2"
        player5name = "Bot 3"
        player6name = "Bot 4"
        player7name = "Bot 5"
        player8name = "Bot 6"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 2 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = 0
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 3 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = "Bot 1"
        player5name = "Bot 2"
        player6name = "Bot 3"
        player7name = "Bot 4"
        player8name = "Bot 5"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 3 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = 0
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 4 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = "Bot 1"
        player6name = "Bot 2"
        player7name = "Bot 3"
        player8name = "Bot 4"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 4 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = 0
        player6name = 0
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 5 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = "Bot 1"
        player7name = "Bot 2"
        player8name = "Bot 3"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 5 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = 0
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 6 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = "Bot 1"
        player8name = "Bot 2"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 6 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = 0
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 7 and botsOn == True:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = "Bot 1"
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 7 and botsOn == False:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = 0
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)
    if player_count == 8:
        player1name = input("What would you like to name player 1? ")
        player2name = input("What would you like to name player 2? ")
        player3name = input("What would you like to name player 3? ")
        player4name = input("What would you like to name player 4? ")
        player5name = input("What would you like to name player 5? ")
        player6name = input("What would you like to name player 6? ")
        player7name = input("What would you like to name player 7? ")
        player8name = input("What would you like to name player 8? ")
        play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name)

def play(player_count, player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name):
    instructions = input("Before we begin, would you like to read the instructions? (Y/N) ")
    if instructions.lower() == "y":
        print("This is Timeline, a game where you must organize your cards in the correct order. Each player will start with one 'card'. The card will have information about a subject and a year on it. ")
        print("A card will be randomly picked from a deck of the remaining cards. A random player will be picked to play first. You will see a card with no year, and must decide if that card's year is before ")
        print("or after the year you have on your card. If you guess correctly, you keep the card. If you don't correctly guess, the card will go to the next person until someone guesses right. ")
        print("As time goes on, you must choose where a card is with multiple of your own cards, and it could be inbetween, before, or after any of the cards. The main goal is to get 10 cards.")
        print("First player to have 10 correctly ordered cards wins.")
        begin = input("Ready to start? (Y/N) ")
        if begin.lower() == "y":
            players = [player1name, player2name, player3name, player4name, player5name, player6name, player7name, player8name]
            firstturnplayer = random.choice(players)
            print(firstturnplayer + " will have the first turn.")
            gameStarted = True
        if begin.lower() == "n":
            play()
    else:
        gameStarted = True


timeline()