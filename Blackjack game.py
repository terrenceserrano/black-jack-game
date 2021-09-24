#create a game called black jack using oop

#this is a game that players will have 2 or up to 3 cards that will be added up if over 21 loses
#and equal to 21 is called blackjack

#we will use the import module

import random
import time

# we declare the variables here by using dictionary and arrays

house = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#input of the player 1

name = input("Input the name of the player here: ")

print("\nWelcome to blackjack " + name + "!")

#this is for the input of the chips of the player

chip = int(input("\nInput your total chips here: ")) #this is used in the OOP for chip

print("\nyour starting capital is: " + str(chip))

playing = True #to make the loop continuous

#creating OOP

#this is for the OOP of the card

class Card:

    def __init__(self, suit, rank): #paramaters for the suit and rank
        #this is for the attributes
        self.suit = suit
        self.rank = rank

    def __str__(self): #defining the string

        return self.rank + " of " + self.suit #this is for the number and card type

#OOP for deck and shuffle function

class Deck:

    def __init__(self):
        #this is for the attributes
        self.deck = [] #start of a list

        for suit in house:

            for rank in ranks:

                self.deck.append(Card(suit, rank)) #this will append the cards and suits

    def __str__(self): #__str__ is the string

        deck_comp = " "

        for card in self.deck:

            deck_comp += "\n" + card.__str__() #adding each card in a string

        return "The deck has " + deck_comp

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop() #we use the pop to remove the top part of the deck

        return single_card

# OOP for the cards in hand

class Hand:

    def __init__(self): #the __init__ is an integer
        #this is for the attributes
        self.cards = [] #start of an empty list in deck class, this is for the list of cards in hands
        self.value = 0 #this is the start of cards in hand
        self.aces = 0  #this is an attribute for the ace

    def add_card(self, card): #we are using def to define a variable
        #this is for the attribute
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":

            self.aces += 1

    def adjust_for_ace(self): #this is for a card that is draw with ace that can be 10 or a 1

        while self.value > 21 and self.aces:

            self.value -= 10
            self.aces -= 1

#creating the chip balance for the player

class Chips:

    def __init__(self):
        #this is the attributes
        self.total = chip
        self.bet = 0 #this is for the start of the bet

    def win_bet(self):
        #this is for the attribute for the winning
        self.total += self.bet #this is increasing per win

    def lost_bet(self):
        #this is for the attribute for the losing
        self.total -= self.bet

#this is for the placing a bet

def take_bet(chip):

    while True:
        try:
            chip.bet = bet = int(input("How much you want to bet?: ")) #this is for how much you want to place a bet

        except ValueError:

            print("Sorry you input a wrong value")

        else:
            if chip.bet > chip.total: #this is the formula if exceeded place

                print("Sorry you cannot exceed at {}" + str(chip.total))

            else:
                break

#this is for the action

def hit(deck,hand): #the deck and the hand is the parameters
    #this is for the attribute of the card and adjustments for ace
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#this is if for the player to add more card or stay put

def hit_or_stay(deck,hand): #the deck and hand is the parameter
    global playing

    while True:
        #some of the inputs is included in the OOP
        decision = input("Would you like to hit or stay?(h/s): ")

        if decision.lower() == "h": #this is for the for the input of player

            hit(deck,hand) #this is defined above

        elif decision.lower() == "s":
            print("The players stays! Dealer is drawing")
            playing = False

        else:

            print("Try again")
            continue

        break

#this will display the cards, dealer card and for the scenarios busts, win and push

def show_one(player,dealer): #the paramaters is for the dealer and the player
    #dealer first
    print("\nDealer's hand")
    print("<card hidden>")
    time.sleep(1)
    #this is after the dealer
    print(" ", dealer.cards[1])
    print("\nplayer hand: ", *player.cards, sep= "\n")
    time.sleep(1)

def show_all(player,dealer):
    #dealer first
    print("\nDealer's hand:", *dealer.cards, sep="\n")
    print("Dealer's hand = ", dealer.value)
    time.sleep(2)
    #this is after the dealer
    print("\n" + name + " hand: ", *player.cards, sep= "\n")
    print(name + " hand = ", player.value)
    time.sleep(2)

#this is for the scenario

#this is if the player lost
def player_lost(player,dealer,chips): #if bust the parameters is player, cards and the chips
    time.sleep(2)
    print(name + " went over 21! " + name + " busts!")
    chips.lost_bet() #this will call the function if the player looses

#this is if the player wins
def player_win(player,dealer,chips): #still the parameters is player dealer and chips
    time.sleep(2)
    print(name + " Wins!")
    chips.win_bet() #this is will the function if the player win

#this if the dealer loses
def dealer_lost(player,dealer,chips): #still the same parameters
    time.sleep(2)
    print("Dealer went over 21! dealer busts!")
    chips.win_bet()

#this if the dealer wins
def dealer_win(player,dealer,chips): #still the parameters
    time.sleep(2)
    print("Dealer wins!")

#this is if the player = dealer
def push(player,dealer):
    time.sleep(2)
    print(name + " and the dealer is tied! it is a push!")

#that is the end of all the functions we will use

#this is for the game

while True:

    #This will shuffle the deck and distribute two cards to each player

    deck = Deck() #the deck() is the OOP of the function
    deck.shuffle() #the shuffle is from the random

    #this is for the player card
    player_hand = Hand()
    player_hand.add_card(deck.deal()) #this is for the first card
    player_hand.add_card(deck.deal()) #this is for the second hand

    #this is for the player hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())  # this is for the first card
    dealer_hand.add_card(deck.deal())  # this is for the second hand


    #This for taking the bets
    player_chips = Chips()

    #this will prompt the palyer for the bet
    take_bet(player_chips)

    #show card of the dealer but the other one is hidden
    show_one(player_hand, dealer_hand)

    while playing: #this is from the hit or stay function

        #this is for the player to hit or stay
        hit_or_stay(deck, player_hand)

        #this will show the one card of the dealer and the other one is hidden
        show_one(player_hand, dealer_hand)

        #this is if the player hand exceed 21, this will run the player bust
        if player_hand.value > 21:
            player_lost(player_hand, dealer_hand, player_chips)

            break

    #if player is not busted, play the dealers hand until 17
    if player_hand.value <= 21: #this is for the player

        while dealer_hand.value < 17: #this is for the dealer

            hit(deck, dealer_hand)

        #this will show all the cards of the dealer

        show_all(player_hand, dealer_hand)

        #this will run different scenarios

        if dealer_hand.value > 21:

            dealer_lost(player_hand, dealer_hand, player_chips)

        #this is for the comparison between dealer and player
        elif dealer_hand.value > player_hand.value:

            dealer_win(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:

            player_win(player_hand, dealer_hand, player_chips)

        else:

            push(player_hand, dealer_hand)

    #this is for the information of the total chips
    print("\n" + name + " winnings is at: ", player_chips.total)

    #this is if you want to play again

    game = input("do you want to play again?(y/n): ")

    if game == "y":

        playing = True

        continue

    else:
        print("Thank you! please come back again!")

        break























