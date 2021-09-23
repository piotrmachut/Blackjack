from ascii import logo
from os import system, name
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card(cards):
    return random.choice(cards)

def calculate_score(score_table):
    total = 0
    for ele in range(0, len(score_table)):
        total = total + score_table[ele]
    return total


def final_score(users_score, computers_score, users_cards, computers_cards):
    print(f"wynik kompa: {computers_score} na kartach {computers_cards}") # TESTING PURPOSES
    print(f"twój wynik: {users_score} na kartach {users_cards}") # TESTING PURPOSES


def game(cards):
    users_cards = []
    computers_cards = []
    for i in range(0, 2):
        users_cards.append(pick_card(cards))
        computers_cards.append(pick_card(cards))
    print(f"    Your cards: {users_cards}")
    print(f"    Conputer's fitst card: {computers_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' yo pass: ").lower()
    if another_card == "y":
        users_cards.append(pick_card(cards))
    users_score = calculate_score(users_cards)
    computers_score = calculate_score(computers_cards)
    if computers_score < 17:
        computers_cards.append(pick_card(cards))
    final_score(users_score, computers_score, users_cards, computers_cards)

app_running = True
while app_running:
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()
    if game_start == "y":
        print(logo)
        game(cards)

    elif game_start == "n":
        app_running = False
        clear()
    else:
        print("Please restart and follow the instructions!")