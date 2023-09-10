import os
from typing import Optional
import random

import numpy as np

import gymnasium as gym
from gymnasium import spaces
from gymnasium.error import DependencyNotInstalled


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


deck = Deck()

# play.addCard(hands[0][0])


def sort_cards_by_rank(cards):
    rank_order = ["3", "4", "5", "6", "7", "8",
                  "9", "10", "11", "12", "13", "1", "2"]
    sorted_cards = sorted(cards, key=lambda card: rank_order.index(card.rank))
    return sorted_cards


def cmp(a, b):
    return float(a > b) - float(a < b)


# 1 = Ace, 2-10 = Number cards, Jack/Queen/King = 10
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def draw_card(np_random):
    return int(np_random.choice(deck))


def sum_hand(hand):  # Return current hand total
    return sum(hand)


def score(hand):  # Change scoring system, I guess high values are rewarded but also add favor to more same cards
    return sum_hand(hand)


def no_place(hand):
    for range in len(hand):
        if(hand[i] ==)


class BlackjackEnv(gym.Env):
    """
    President, also known as "Asshole" or "Scum," is a popular card game played with a standard deck of 52 cards. The game is typically played with a group of players, and the objective is to get rid of all your cards and become the President in subsequent rounds.

    Here are the general instructions for playing President:

    Setup: Choose a dealer who shuffles the deck and deals the entire deck of cards to all the players. The number of cards dealt to each player may vary depending on the number of players.
    Ranking of Cards: The cards are ranked from highest to lowest: 2, Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3. The suits do not have any significance in this game.

    Gameplay:
        The player who has the 3 of Clubs starts the first round and becomes the President in subsequent rounds.
        The player holding the 3 of Clubs plays it as the first card in the center of the table.
        The player to the left of the President goes next and can play any card or set of cards with the same rank that is higher than the previous play. For example, if the 3 of Clubs is played, the next player can play a higher rank, such as a 4, or a set of equal-ranked cards, such as two 3s or three 3s.
        The subsequent players must play higher-ranking cards or sets of cards. If a player cannot play a higher rank, they pass and do not play any cards in that round.
        The round continues clockwise until all players pass consecutively. At this point, the player who played the last set of cards becomes the new President for the next round.
        The cards played in each round are discarded.
        The goal is to get rid of all your cards as quickly as possible, as the last player to have cards remaining becomes the "Asshole" or "Scum" in subsequent rounds.

    Hierarchy of Positions:
        President: The winner of the previous round becomes the President for the next round and holds the highest rank.
        Vice President: The player who finishes second in the previous round becomes the Vice President.
        Ordinary Players: The players who finish between the President and Vice President.
        Vice Asshole: The second-to-last player in the previous round.
        Asshole (Scum): The last player to get rid of all their cards in the previous round.

    Subsequent Rounds:
        In subsequent rounds, the President starts the game by playing any card or set of cards of their choice.
        The gameplay continues as before, with players playing higher-ranking cards or sets.
        The goal remains the same: Players aim to get rid of all their cards as quickly as possible to avoid becoming the Asshole in the next round.

    End of the Game:
        The game typically continues for several rounds until players decide to stop or a predetermined number of rounds is completed.
        Players can keep track of their positions throughout the rounds, with the President being the highest-ranking position and the Asshole being the lowest.
        The player with the highest rank (President) at the end of the game is declared the overall winner.

    ## Action Space
        Pass: The player chooses to pass their turn and not play any cards in the current round. This action is taken when the player does not have any higher-ranking cards to play.

    Play Cards: The player selects a set of cards from their hand that are higher in rank than the previously played cards. The selected cards are played in the center of the table to continue the round. The specific combination and number of cards played may vary depending on the rules being followed..

    - 0: Pass your Turn
    - 1: Play a Higher rank of cards

    ## Observation Space
    The players Current Hand
    the value of the dealer's one showing card (3-15 where 15 is 2, 14 is Ace),
    The ammount of hat rank the last player has put down

    The observation is returned as `(array(int()), int(), int())`.

    ## Starting State
    The starting state is initialised in the following range.

    | Observation               | Min  | Max  |
    |---------------------------|------|------|
    | Player current hand       | [0]  | [26] |
    | The card value placed     |  3   |  15  |
    | # of cards last placed    |  1   |  4   |

    ## Rewards
    - win game: +1
    - lose game: -1
    - draw game: 0
    - win game with natural blackjack:
    +1.5 (if <a href="#nat">natural</a> is True)
    +1 (if <a href="#nat">natural</a> is False)

    ## Episode End
    The episode ends if the following happens:

    - Termination:
    1. The player hits and the sum of hand exceeds 21.
    2. The player sticks.

    An ace will always be counted as usable (11) unless it busts the player.

    ## Information

    No additional information is returned.

    ## Arguments

    ```python
    import gymnasium as gym
    gym.make('Blackjack-v1', natural=False, sab=False)
    ```

    <a id="nat"></a>`natural=False`: Whether to give an additional reward for
    starting with a natural blackjack, i.e. starting with an ace and ten (sum is 21).

    <a id="sab"></a>`sab=False`: Whether to follow the exact rules outlined in the book by
    Sutton and Barto. If `sab` is `True`, the keyword argument `natural` will be ignored.
    If the player achieves a natural blackjack and the dealer does not, the player
    will win (i.e. get a reward of +1). The reverse rule does not apply.
    If both the player and the dealer get a natural, it will be a draw (i.e. reward 0).

    ## References
    <a id="blackjack_ref"></a>[1] R. Sutton and A. Barto, “Reinforcement Learning:
    An Introduction” 2020. [Online]. Available: [http://www.incompleteideas.net/book/RLbook2020.pdf](http://www.incompleteideas.net/book/RLbook2020.pdf)

    ## Version History
    * v1: Fix the natural handling in Blackjack
    * v0: Initial version release
    """

    metadata = {
        "render_modes": ["human", "rgb_array"],
        "render_fps": 4,
    }

    def __init__(self, num_players=3):
        self.action_space = spaces.Discrete(2)
        array_length = 26
        # Define the array lengths from 0 to 26
        array_lengths = [spaces.Discrete(i) for i in range(array_length + 1)]
        # Create the MultiDiscrete space
        array_space = spaces.MultiDiscrete(array_lengths)

        self.observation_space = spaces.Tuple(
            (array_space, spaces.Discrete(13), spaces.Discrete(4))
        )

        self.num_players = num_players
        hands = deck.deal(num_players)
        hands[0] = sort_cards_by_rank(hands[0])
        self.player = hands[0]

    def step(self, action):
        assert self.action_space.contains(action)
        if action:  # hit: add a card to players hand and return
            if no_place(self.player):
                terminated = True
                reward = -1.0
            else:
                terminated = False
                reward = 0.0
        else:  # stick: play out the dealers hand, and score
            terminated = True
            while sum_hand(self.dealer) < 17:
                self.dealer.append(draw_card(self.np_random))
            reward = cmp(score(self.player), score(self.dealer))
            if self.sab and is_natural(self.player) and not is_natural(self.dealer):
                # Player automatically wins. Rules consistent with S&B
                reward = 1.0
            elif (
                not self.sab
                and self.natural
                and is_natural(self.player)
                and reward == 1.0
            ):
                # Natural gives extra points, but doesn't autowin. Legacy implementation
                reward = 1.5

        if self.render_mode == "human":
            self.render()
        return self._get_obs(), reward, terminated, False, {}

    def _get_obs(self):
        return (self.player, self.dealer[0], usable_ace(self.player))

    def reset(
        self,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ):
        super().reset(seed=seed)
        hands = deck.deal(self.num_players)
        hands[0] = sort_cards_by_rank(hands[0])
        self.player = hands[0]

        _, dealer_card_value, _ = self._get_obs()

        suits = ["C", "D", "H", "S"]
        self.dealer_top_card_suit = self.np_random.choice(suits)

        if dealer_card_value == 1:
            self.dealer_top_card_value_str = "A"
        elif dealer_card_value == 10:
            self.dealer_top_card_value_str = self.np_random.choice([
                                                                   "J", "Q", "K"])
        else:
            self.dealer_top_card_value_str = str(dealer_card_value)

        if self.render_mode == "human":
            self.render()
        return self._get_obs(), {}

    def render(self):  # Changes!
        if self.render_mode is None:
            assert self.spec is not None
            gym.logger.warn(
                "You are calling render method without specifying any render mode. "
                "You can specify the render_mode at initialization, "
                f'e.g. gym.make("{self.spec.id}", render_mode="rgb_array")'
            )
            return

        try:
            import pygame
        except ImportError as e:
            raise DependencyNotInstalled(
                "pygame is not installed, run `pip install gymnasium[toy-text]`"
            ) from e

        player_sum, dealer_card_value, usable_ace = self._get_obs()
        screen_width, screen_height = 600, 500
        card_img_height = screen_height // 3
        card_img_width = int(card_img_height * 142 / 197)
        spacing = screen_height // 20

        bg_color = (7, 99, 36)
        white = (255, 255, 255)

        if not hasattr(self, "screen"):
            pygame.init()
            if self.render_mode == "human":
                pygame.display.init()
                self.screen = pygame.display.set_mode(
                    (screen_width, screen_height))
            else:
                pygame.font.init()
                self.screen = pygame.Surface((screen_width, screen_height))

        if not hasattr(self, "clock"):
            self.clock = pygame.time.Clock()

        self.screen.fill(bg_color)

        def get_image(path):
            cwd = os.path.dirname(__file__)
            image = pygame.image.load(os.path.join(cwd, path))
            return image

        def get_font(path, size):
            cwd = os.path.dirname(__file__)
            font = pygame.font.Font(os.path.join(cwd, path), size)
            return font

        small_font = get_font(
            os.path.join("font", "Minecraft.ttf"), screen_height // 15
        )
        dealer_text = small_font.render(
            "Dealer: " + str(dealer_card_value), True, white
        )
        dealer_text_rect = self.screen.blit(dealer_text, (spacing, spacing))

        def scale_card_img(card_img):
            return pygame.transform.scale(card_img, (card_img_width, card_img_height))

        dealer_card_img = scale_card_img(
            get_image(
                os.path.join(
                    "img",
                    f"{self.dealer_top_card_suit}{self.dealer_top_card_value_str}.png",
                )
            )
        )
        dealer_card_rect = self.screen.blit(
            dealer_card_img,
            (
                screen_width // 2 - card_img_width - spacing // 2,
                dealer_text_rect.bottom + spacing,
            ),
        )

        hidden_card_img = scale_card_img(
            get_image(os.path.join("img", "Card.png")))
        self.screen.blit(
            hidden_card_img,
            (
                screen_width // 2 + spacing // 2,
                dealer_text_rect.bottom + spacing,
            ),
        )

        player_text = small_font.render("Player", True, white)
        player_text_rect = self.screen.blit(
            player_text, (spacing, dealer_card_rect.bottom + 1.5 * spacing)
        )

        large_font = get_font(os.path.join(
            "font", "Minecraft.ttf"), screen_height // 6)
        player_sum_text = large_font.render(str(player_sum), True, white)
        player_sum_text_rect = self.screen.blit(
            player_sum_text,
            (
                screen_width // 2 - player_sum_text.get_width() // 2,
                player_text_rect.bottom + spacing,
            ),
        )

        if usable_ace:
            usable_ace_text = small_font.render("usable ace", True, white)
            self.screen.blit(
                usable_ace_text,
                (
                    screen_width // 2 - usable_ace_text.get_width() // 2,
                    player_sum_text_rect.bottom + spacing // 2,
                ),
            )
        if self.render_mode == "human":
            pygame.event.pump()
            pygame.display.update()
            self.clock.tick(self.metadata["render_fps"])
        else:
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(self.screen)), axes=(1, 0, 2)
            )

    def close(self):
        if hasattr(self, "screen"):
            import pygame

            pygame.display.quit()
            pygame.quit()
