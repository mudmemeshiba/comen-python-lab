# PPPPPP-P-
#       P P
# 7,9 should pass but failed

# Shuffle a deck of cards using a Python random module
import random
from random import shuffle

# Define a class to create all type of cards
class Cards:
    global suites, values, SEP
    # 'diamonds (♦)', 'clubs (♣)', 'hearts (♥)', 'spades (♠)'
    suites = ['♥', '♦', '♣', '♠']
    values = ['A', '2', '3', '4', '5', '6', '7', '8']
    values += ['9', '10', 'J', 'Q', 'K']
    SEP = '-'
    def __init__(self):
        pass

# Define a class to categorize each card
class Deck(Cards):
    def __init__(self):
        super().__init__()
        self.mycardset = []
        for n in suites:
            for c in values:
                self.mycardset.append(c+ SEP +n)
  # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            print("Card removed is", cardpopped)

# Define a class gto shuffle the deck of cards
class ShuffleCards(Deck):
  # Constructor
    def __init__(self):
        super().__init__()
    # Method to shuffle cards
    def shuffle(self, seed=0):
        '''use integer seed != 0 to generate the same random number'''
        if seed != 0:
            random.seed(seed)
        shuffle(self.mycardset)
        return self.mycardset
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            return (cardpopped)

# objShuffleCards = ShuffleCards()
# # card set 2 (shuffled..)
# set2Cards = objShuffleCards.shuffle()
# print('\n Set 2 Cards: \n', set2Cards)
# # Remove some cards
# print('\n Removing a card from the deck:', objShuffleCards.popCard())
# print('\n Removing another card from the deck:', objShuffleCards.popCard())

# student code, ie. Game class, below this line
###---------------------------- BEGIN Student work ----------------------------

class Game(ShuffleCards):
    def __init__(self):
        super().__init__()
    
    def play_game(self, intSeed):
        global name, seed, p1, p2, c1, c2
        name = input("Player1 name: ")
        print("Welcome to Simple BackJack.. ©2023 MikeLab.Net")
        seed = self.shuffle(intSeed)
        p1 = self.popCard()
        c1 = self.popCard()
        p2 = self.popCard()
        c2 = self.popCard()
        # call functions 
        self.firstTurn()
        hs = input(f"{name}, would you (H)it or (S)tand..? ")  
        if hs == "S" or hs == "s":
            print("Now, it is my turn..")
            self.firstTurn()
            self.comTurn()
        elif hs == "H" or hs == "h":
            self.playerTurn()
    
    def firstTurn(self):
        global name, p1, p2, c1, c2, pCards, cCards, pVal, cVal
        pCards, cCards, pVal, cVal = [], [], [], []
        pCards.append(p1)
        cCards.append(c1)
        pCards.append(p2)
        cCards.append(c2)
        # get card val in int
        self.convertPVal(p1)
        self.convertCVal(c1)
        self.convertPVal(p2)
        self.convertCVal(c2)
        self.printRes(pCards, pVal, cCards, cVal)
    
    def playerTurn(self):
        newPcard = self.popCard()
        pCards.append(newPcard)
        self.convertPVal(newPcard)
        self.checkA() # -15
        self.printRes(pCards, pVal, cCards, cVal)
        
        while sum(pVal) < sum(cVal) < 21:
            hs = input(f"{name}, would you (H)it or (S)tand..? ")  
            if hs == "H" or hs == "h":
                # self.playerTurn() # test6 failed
                newPcard = self.popCard()
                pCards.append(newPcard)
                self.convertPVal(newPcard)
                self.printRes(pCards, pVal, cCards, cVal)
                print("Now, it is my turn..")
                self.printRes(pCards, pVal, cCards, cVal)
                self.whoWins()
                return # ends the function
            
        if (sum(cVal) < sum(pVal) < 21) or (sum(cVal) == sum(pVal) == 21):
            hs = input(f"{name}, would you (H)it or (S)tand..? ")  
            if hs == "S" or hs == "s":
                print("Now, it is my turn..")
                self.printRes(pCards, pVal, cCards, cVal)
                self.checkA()
                self.comTurn()
            elif hs == "H" or hs == "h":
                self.playerTurn()
                hs = input(f"{name}, would you (H)it or (S)tand..? ")
                if hs == "S" or hs == "s":
                    print("Now, it is my turn..")
                    self.printRes(pCards, pVal, cCards, cVal)
                    self.comTurn()
        elif sum(cVal) < 21 < sum(pVal):
            print("Now, it is my turn..")
            self.printRes(pCards, pVal, cCards, cVal) #can swap with 134
            self.checkA()
            self.whoWins()

    def comTurn(self): # case 4 18<22 conflict with 18<20 (p,c both less than 21)
        while (sum(cVal) < 21) and (sum(cVal) < sum(pVal)):
            if (sum(pVal) < sum(cVal) < 21):
                self.whoWins() 
                return
            newCcard = self.popCard()
            cCards.append(newCcard)
            self.convertCVal(newCcard)
            self.checkA()
            self.printRes(pCards, pVal, cCards, cVal)
        self.whoWins()
    
    def convertPVal(self, card):
        if card[0] == "1" and card[1] == "0":
            val = 10
        elif card[0] == "K" or card[0] == "Q" or card[0] == "J":
            val = 10
        elif card[0] == "A":
            val = 11
        else:
            val = int(card[0])
        pVal.append(val)
        return pVal
    
    def convertCVal(self, card):
        if card[0] == "1" and card[1] == "0":
            val = 10
        elif card[0] == "K" or card[0] == "Q" or card[0] == "J":
            val = 10
        elif card[0] == "A":
            val = 11
        else:
            val = int(card[0])
        cVal.append(val)
        return cVal

    def checkA(self):
        if sum(pVal) > 21 and (11 in pVal) and ("A-♥" or "A-♦" or "A-♣" or "A-♠" in pCards):
            pVal.remove(11)
            pVal.append(1)
            return pVal
        if sum(cVal) > 21 and (11 in cVal) and ("A-♥" or "A-♦" or "A-♣" or "A-♠" in cCards):
            cVal.remove(11)
            cVal.append(1) 
            return cVal

    def whoWins(self):
        print("Who wins?") # no more games after who wins
        self.printRes(pCards, pVal, cCards, cVal)
        if (sum(pVal) == sum(cVal)):
            print("DRAW..")
        elif (sum(pVal) >= 21 and sum(pVal) > sum(cVal)) or (sum(pVal) < sum(cVal) < 21): #<= 21 matters?
            print("[Computer] wins this round")
        elif (sum(cVal) >= 21 and sum(cVal) > sum(pVal)):
            print(f" {name} wins this round")

    def printRes(self, pCards, pVal, cCards, cVal):
        print(f"   {name}: ", end="")
        print(*pCards, sep=', ', end='')
        print(f", ({sum(pVal)})  Computer: ", end='')
        print(*cCards, sep=', ', end='')
        print(f", ({sum(cVal)})")

###---------------------------- END Student work ----------------------------

##### main driver code for the above student work, ie. Game class.
import random
from random import shuffle

while True:
    doc = '''Just press ENTER to let the card deck be shuffled
randomly, or any integer N to run random.seed(N)
with the same shuffle pattern, or (q)uit!'''
    #print('X'*50)
    print(doc, end='')
    intSeed = input(': ')
    #print('X'*50)
    if intSeed.upper()=='Q':
        print('Bye.')
        break
    try:
        if intSeed=='':
            g = Game()
            g.play_game()
        else:
            g = Game()
            g.play_game(int(intSeed)) 
    except ValueError:
        print(f'ERROR: You entered a wrong input: [{intSeed}]!!')