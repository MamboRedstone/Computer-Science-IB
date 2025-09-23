import random
from terminology import in_black, on_red, on_green, on_white


cards = [
    "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds", "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds", "Queen Diamonds", "King Diamonds", "Ace Diamonds",
    "2 Spades", "3 Spades", "4 Spades", "5 Spades", "6 Spades", "7 Spades", "8 Spades", "9 Spades", "10 Spades", "Jack Spades", "Queen Spades", "King Spades", "Ace Spades",
    "2 Hearts", "3 Hearts", "4 Hearts", "5 Hearts", "6 Hearts", "7 Hearts", "8 Hearts", "9 Hearts", "10 Hearts", "Jack Hearts", "Queen Hearts", "King Hearts", "Ace Hearts",
    "2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs", "7 Clubs", "8 Clubs", "9 Clubs", "10 Clubs", "Jack Clubs", "Queen Clubs", "King Clubs", "Ace Clubs"
] # list of all possible cards


# function draws a unique card from the game
def draw_cards(amount, player_num):
    for _ in range(amount):
        card = random.choice(cards)
        cards.remove(card)
        players[player_num].append(card)


#function to calculate all cards value 
def calc_total(player_num):
    acePresent = 0
    players[player_num][0] = 0  
    # check if the card type
    for i in range(1, len(players[player_num])):
        card = players[player_num][i]
        card_val = card.split()[0]
        if card_val.isdigit():
            players[player_num][0] += int(card_val) # add value of card
        
        else:
            if card_val in ["Jack", "Queen", "King"]:
                players[player_num][0] += 10 # add 10 for face cards

            # if ace gets over 21 it changes from 11 to 1
            elif card_val == "Ace":
                acePresent += 1

    for _ in range(acePresent):
        if players[player_num][0] + 11 > 21:
            players[player_num][0] += 1 # add 1
        else:
            players[player_num][0] += 11 # add 11
                    

# function to read total value of cards and all cards of a specific player
def read_cards(player_num):
    print("\n")
    print(on_white(in_black(f"Player {player_num+1} Cards ({players[player_num][0]}):")))
    for i in range(1, len(players[player_num]), 1):
        print(f"{players[player_num][i]}")


# player count input
Valid = False
while not Valid:
    try:
        total_players = int(input("Enter total number of players (1-8): "))
        if not 1 <= total_players <= 8:
            print("\nInvalid player count.")
        else:
            Valid = True
    except ValueError:
        print("\nMust be a number.")

players = [[0] for _ in range(total_players)] # array that stores all players total and cards.

# assign 2 cards to each player at start of game
for i in range(total_players):
    draw_cards(2, i)
    calc_total(i)

Playing = True
end_game_check = 0
# main game loop
while Playing:
    # checks for if all players have lost
    if end_game_check == total_players:
        print(on_red("All players have lost!"))
        exit()
    end_game_check = 0
    
    for i in range(total_players):
        # skips player that have lost
        if players[i][0] > 21:
            end_game_check += 1
            continue
        
        read_cards(i)
        # makes user choose between stick and twist
        draw_card = input(on_white(in_black(f"Player {i+1}: Do you want to stick or twist? "))).lower()
        if draw_card in ["stick", "s"]:
            pass
        elif draw_card in ["twist", "t"]:
            draw_cards(1, i)
            calc_total(i)
            read_cards(i)

        # checks player win/lose condition
        if players[i][0] == 21:
            print(on_green(f"Player {i+1} wins!\n"))
            exit()
        elif players[i][0] > 21:
            print(on_red(f"Player {i+1} lost!\n"))       