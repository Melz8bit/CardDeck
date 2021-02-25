import random

DECK_SIZE = 52

deck = [(1, 'd', 0), (2, 'd', 0), (3, 'd', 0), (4, 'd', 0), (5, 'd', 0), (6, 'd', 0), (7, 'd', 0), (8, 'd', 0), (9, 'd', 0), (10, 'd', 0), (11, 'd', 0), (12, 'd', 0), (13, 'd', 0), 
                (1, 'h', 0), (2, 'h', 0), (3, 'h', 0), (4, 'h', 0), (5, 'h', 0), (6, 'h', 0), (7, 'h', 0), (8, 'h', 0), (9, 'h', 0), (10, 'h', 0), (11, 'h', 0), (12, 'h', 0), (13, 'h', 0),
                (1, 'c', 0), (2, 'c', 0), (3, 'c', 0), (4, 'c', 0), (5, 'c', 0), (6, 'c', 0), (7, 'c', 0), (8, 'c', 0), (9, 'c', 0), (10, 'c', 0), (11, 'c', 0), (12, 'c', 0), (13, 'c', 0),
                (1, 's', 0), (2, 's', 0), (3, 's', 0), (4, 's', 0), (5, 's', 0), (6, 's', 0), (7, 's', 0), (8, 's', 0), (9, 's', 0), (10, 's', 0), (11, 's', 0), (12, 's', 0), (13, 's', 0)]
shuffledDeck = []

def shuffleDeck():
        random.seed(None,2)

        while len(shuffledDeck) < DECK_SIZE:
                randCardIndex = random.randint(0, DECK_SIZE - 1)

                card = deck[randCardIndex]

                if card[2] == 0:
                        shuffledDeck.append(card)
                        dealtCard = list(card)
                        dealtCard[2] = 1
                        dealtCard = tuple(dealtCard)        
                        deck[randCardIndex] = dealtCard      

        print(shuffledDeck)

def main():
        shuffleDeck()

if __name__ == "__main__":
        main()