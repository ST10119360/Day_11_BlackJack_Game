import random

import art

game_over = False
deck_of_cards = {
    'Hearts': {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
               'Queen': 10, 'King': 10},
    'Diamonds': {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
                 'Queen': 10, 'King': 10},
    'Clubs': {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
              'Queen': 10, 'King': 10},
    'Spades': {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
               'Queen': 10, 'King': 10}
}


def dealing():
    """Function that deals cards to users"""
    user_cards = [random_card() for _ in range(2)]  # The underscore means we do not need a variable just for the
    # random_card function to run twice for comp and user
    comp_cards = [random_card() for _ in range(2)]
    return user_cards, comp_cards


def random_card():
    """Generates random cards"""
    random_suit = random.choice(list(deck_of_cards.keys()))
    random_value = random.choice(list(deck_of_cards[random_suit].keys()))
    return random_value, random_suit  # Create a tuple with two elements


def calculate_total(cards):
    """To work out the value of players hand"""
    total = sum(deck_of_cards[suit][value] for value, suit in cards)
    num_aces = sum(1 for value, suit in cards if value == 'Ace')

    # Adjust the total if there are Aces and the total exceeds 21
    while num_aces > 0 and total > 21:
        total -= 10  # Change the value of one Ace from 11 to 1
        num_aces -= 1

    return total


def print_user_cards_and_total(player, cards, total):
    """Prints users hand and total"""
    print(f"\n{player}'s cards:")
    for card in cards:
        print(f"  {card[0]} of {card[1]}")
    print(f"\n{player}'s total: {total}\n")


def print_computer_cards_and_total(comp_cards, comp_total, show_all=False):
    """Prints computers hand and total"""
    print("\nComputer's cards:")
    for i, card in enumerate(comp_cards):
        if i == 0 or show_all:
            print(f"  {card[0]} of {card[1]}")
        else:
            print("  Hidden Card")
    print(f"\nComputer's total: {comp_total}\n")

user, comp = dealing()
user_total = calculate_total(user)
comp_total = calculate_total(comp)
comp_total1 = "Hidden"
compcard1 = "Hidden"
print(art.logo)
print_user_cards_and_total("User", user, user_total)
print_computer_cards_and_total(comp, comp_total1, show_all=False)


while not game_over:
    if comp_total == 21 and user_total != 21:
        print("Computer has a blackjack")
    if user_total == 21 and comp_total != 21:
        print("You have a blackjack")
        game_over = True
    elif user_total < 21:
        print("Would you like to 'hit' or 'stay'")
        reply = input().lower()
        if reply == 'hit':
            result = random_card()
            user.append(result)
            user_total = calculate_total(user)
            print_user_cards_and_total("User", user, user_total)
        elif reply == 'stay':
            while comp_total < 17:
                comp.append(random_card())
                comp_total = calculate_total(comp)
            game_over = True
        else:
            print("Invalid input. Please enter 'hit' or 'stay'")
    else:
        print("User busted! Game over.")
        game_over = True

print_user_cards_and_total("Final User", user, user_total)
print_user_cards_and_total("Final Computer", comp, comp_total)

if comp_total < user_total <= 21:
    print("You win")
elif user_total == comp_total:
    print("It is a draw")
elif comp_total > 21 >= user_total:
    print("Computer busted, You win")
else:
    print("You lose")


