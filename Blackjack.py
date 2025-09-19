import random

players = [[0], [0], [0], [0]]

cards = [
    "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds", "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds", "Queen Diamonds", "King Diamonds", "Ace Diamonds",
    "2 Spades", "3 Spades", "4 Spades", "5 Spades", "6 Spades", "7 Spades", "8 Spades", "9 Spades", "10 Spades", "Jack Spades", "Queen Spades", "King Spades", "Ace Spades",
    "2 Hearts", "3 Hearts", "4 Hearts", "5 Hearts", "6 Hearts", "7 Hearts", "8 Hearts", "9 Hearts", "10 Hearts", "Jack Hearts", "Queen Hearts", "King Hearts", "Ace Hearts",
    "2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs", "7 Clubs", "8 Clubs", "9 Clubs", "10 Clubs", "Jack Clubs", "Queen Clubs", "King Clubs", "Ace Clubs"
]
# list of all players

def draw_cards(amount, player_num):
    for _ in range(amount):
        card = random.choice(cards)
        cards.remove(card)
        players[player_num].append(card)
        # draws a unique carrd from the game

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
    print(f"\nPlayer {player_num+1} info:")
    print(f"Cards Total: {players[player_num][0]}")
    for i in range(1, len(players[player_num]), 1):
        print(f"{players[player_num][i]}")
    # reads cards from the player

total_players = int(input("Enter total number of players: "))
print("\n")
for i in range(total_players):
    draw_cards(2, i)
    calc_total(i)
# start game logic

Playing = True

while Playing:
    # start game loop
    for i in range(total_players):
        read_cards(i)
        draw_card = input(f"Player {i+1}: Do you want to stick or twist: ")
        if draw_card == "stick":
            read_cards(i)
        elif draw_card == "twist":
            draw_cards(1, i)
            calc_total(i)
            read_cards(i)            
            # makes user choose between stick and twist

        if players[i][0] == 21:
            print(f"Player {i+1} wins!")
            exit()
        elif players[i][0] > 21:
            print(f"Player {i+1} lost!")
            # checks player win/lose condition  