class Card():
    def __init__(self, face: str, suit: str, strength: int):
        self.face = face
        self.suit = suit
        self.strength = strength


class Deck():
    ...


def main():
    #Create list of 52 cards
    cards = create_cards()
    #Splits cards into user and cpu decks.
    

def create_cards():
    suits = ["♢", "♡", "♠️", "♣️"]
    faces = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_list = []
    for suit in suits:
        for face in faces:
            card = Card(face, suit, faces.index(face))
            card_list.append(card)
    return card_list


if __name__ == "__main__":
    main()