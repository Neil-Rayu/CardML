import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}-{self.suit}"


class Deck:
    suits = ["Heart", "Diamond", "Club", "Spade"]
    ranks = ["1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "11", "12", "13"]

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_players):
        if num_players <= 0:
            raise ValueError("Number of players should be greater than zero.")

        num_cards_per_player = len(self.cards) // num_players
        hands = []
        for i in range(num_players):
            hand = []
            for _ in range(num_cards_per_player):
                hand.append(self.cards.pop())
            hands.append(hand)

        return hands

    def __str__(self):
        card_list = [str(card) for card in self.cards]
        return ", ".join(card_list)


class Play:

    def __init__(self, hands):
        self.hands = hands
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
        print(str(card))

    # Usage example
deck = Deck()
deck.shuffle()
num_players = 4
hands = deck.deal(num_players)

play = Play(hands)

# play.addCard(hands[0][0])


def sort_cards_by_rank(cards):
    rank_order = ["3", "4", "5", "6", "7", "8",
                  "9", "10", "11", "12", "13", "1", "2"]
    sorted_cards = sorted(cards, key=lambda card: rank_order.index(card.rank))
    return sorted_cards


hands[0] = sort_cards_by_rank(hands[0])
hands[1] = sort_cards_by_rank(hands[1])
hands[2] = sort_cards_by_rank(hands[2])
hands[3] = sort_cards_by_rank(hands[3])

for i, hand in enumerate(hands):
    print(f"Player {i+1}'s hand: {', '.join(str(card) for card in hand)}")

playPile = []


def playGame(hands):
    start = random.randint(0, num_players)
    print(start)
    starter = hands[start]
    playPile.append(starter[0])
