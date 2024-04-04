import itertools
import random

deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'],
                               ['Hearts', 'Diamonds', 'Clubs', 'Spades']))

print("Deck before shuffling:")
for card in deck:
    print(f"{card[0]} of {card[1]}")

random.shuffle(deck)

print("\nDeck after shuffling:")
for card in deck:
    print(f"{card[0]} of {card[1]}")
