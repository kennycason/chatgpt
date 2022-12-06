# write python code for blackjack game
import random

# Possible values for cards
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Possible suits for cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# The deck of cards
deck = [(value, suit) for value in values for suit in suits]

# Function to calculate the total value of a hand of cards
def total(hand):
    # Calculate the total value of the hand
    return sum(value for (value, suit) in hand)

# Function to print a hand of cards
def print_hand(hand):
    for (value, suit) in hand:
        print(f"{value} of {suit}")

# Function to check if the player has busted (gone over 21)
def bust(hand):
    return total(hand) > 21

# Function to check if the player has blackjack (21 with only two cards)
def blackjack(hand):
    return len(hand) == 2 and total(hand) == 21

# Function to check if the player should hit (take another card)
def should_hit(hand):
    return total(hand) < 17

# Function to play a game of blackjack
def play():
    # Shuffle the deck of cards
    random.shuffle(deck)

    # Deal the initial hand to the player
    player_hand = [deck.pop(), deck.pop()]

    # Deal the initial hand to the dealer
    dealer_hand = [deck.pop(), deck.pop()]

    # Print the player's initial hand
    print("Your hand:")
    print_hand(player_hand)

    # Print the dealer's initial hand
    print("Dealer's hand:")
    print_hand([dealer_hand[0]])

    # Check if the player has blackjack
    if blackjack(player_hand):
        print("Blackjack! You win!")
        return

    # While the player should hit and hasn't busted, hit
    while should_hit(player_hand) and not bust(player_hand):
        player_hand.append(deck.pop())

        # Print the player's current hand
        print("Your hand:")
        print_hand(player_hand)

    # If the player has busted, the dealer wins
    if bust(player_hand):
        print("You busted! Dealer wins.")
        return

    # Otherwise, the dealer must hit until they have at least 17 points
    while total(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

        # Print the dealer's current hand
        print("Dealer's hand:")
        print_hand(dealer_hand)

    # If the dealer has busted, the player wins
    if bust(dealer_hand):
        print("Dealer busted! You win!")
        return

    # Compare the player's hand to the dealer's hand
    # and determine the winner
    player_total = total(player_hand)
    dealer_total = total(dealer_hand)
    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total: # output buffer ended here, I finished the rest since it was so close.
        print("You Lose!")
    else:
        print("Tie!")


play()
