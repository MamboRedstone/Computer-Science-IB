import random
from terminology import in_black, on_red, on_green, on_white

cards = [
    "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds", "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds", "Queen Diamonds", "King Diamonds", "Ace Diamonds",
    "2 Spades", "3 Spades", "4 Spades", "5 Spades", "6 Spades", "7 Spades", "8 Spades", "9 Spades", "10 Spades", "Jack Spades", "Queen Spades", "King Spades", "Ace Spades",
    "2 Hearts", "3 Hearts", "4 Hearts", "5 Hearts", "6 Hearts", "7 Hearts", "8 Hearts", "9 Hearts", "10 Hearts", "Jack Hearts", "Queen Hearts", "King Hearts", "Ace Hearts",
    "2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs", "7 Clubs", "8 Clubs", "9 Clubs", "10 Clubs", "Jack Clubs", "Queen Clubs", "King Clubs", "Ace Clubs"
]
# list of all cards

def draw_cards(amount, player_num):
    for _ in range(amount):
        card = random.choice(cards)
        cards.remove(card)
        players[player_num].append(card)
        # draws a unique card from the game

def calc_total(player_num):
    players[player_num][0] = 0  
    for i in range(1, len(players[player_num])):
        card = players[player_num][i]
        card_val = card.split()[0]
        if card_val.isdigit():
            players[player_num][0] += int(card_val)
            # check if the card is not a face card and then adds there value
        else:
            if card_val in ["Jack", "Queen", "King"]:
                players[player_num][0] += 10
                # add 10 for face cards
            elif card_val == "Ace":
                if players[player_num][0] + 11 > 21:
                    players[player_num][0] += 1
                else:
                    players[player_num][0] += 11
                    # if ace gets over 21 it changes from 11 to 1

def read_cards(player_num):
    print("\n")
    print(on_white(in_black(f"Player {player_num+1} Cards:")))
    # print(f"Cards Total: {players[player_num][0]}")
    for i in range(1, len(players[player_num]), 1):
        print(f"{players[player_num][i]}")
        # reads cards from the player

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

print("\n")

players = [[0] for _ in range(total_players)]
# array that stores all players total and cards.

for i in range(total_players):
    draw_cards(2, i)
    calc_total(i)
# start game logic

Playing = True
end_game_check = 0


while Playing:
    # start game loop
    if end_game_check == total_players:
        print(on_red("All players have lost!"))
        exit()
    end_game_check = 0
    # check for if all players have lost
    
    for i in range(total_players):
        if players[i][0] > 21:
            end_game_check += 1
            continue
            # skips player that have lost
        
        read_cards(i)
        draw_card = input(on_white(in_black(f"Player {i+1}: Do you want to stick or twist? "))).lower()
        if draw_card in ["stick", "s"]:
            continue
        elif draw_card in ["twist", "t"]:
            draw_cards(1, i)
            calc_total(i)
            read_cards(i)
            # makes user choose between stick and twist

        if players[i][0] == 21:
            print(on_green(f"Player {i+1} wins!\n"))
            exit()
        elif players[i][0] > 21:
            print(on_red(f"Player {i+1} lost!\n"))
            # checks player win/lose condition  