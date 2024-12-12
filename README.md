# War_CardGame
A Python implementation of the War Card Game

Project Requirements:

    -Create a 2 player version of War
    -Creates a Deck of 52 cards, 4x each of Ace to King (Ace is Highest Value)
        -Cards should be implemented with OOP, with parameters of Value (0-12), ID (2-10,J,Q,K,A), and will need to be comparable
        based off their Value.
    -Splits Deck into 2 shuffled decks for each player (User and CPU)
    -Prompt User for Turn
    -During a Turn:
        -First card from deck is played from both players
        -Highest Card wins both cards to their deck
        -If card values are equal, WAR:
            -Pause, inform player it's WAR and promp to continue
            -Next 3 cards from each deck are added to the table
            -The next card is played
            -Winner takes all cards on table
            -Repeat if another tie, until no tie
    -At end of turn inform user who won that hand and how many cards they have.
    -Game ends when one player runs out of cards
    -If a player's deck does not have enough cards for WAR (4 remaining), just use whatever their last card is and the rest
    go to the table.

Optional Requirements (If there's extra time):

    -Define Suits (D - Diamond, C - Club, S - Spade, H - Heart) for cards
    -Instead of just adding won cards to a player's deck instead they go into a "played" pile (for each player). When a player uses all of his cards they then shuffle the played pile and that's their new deck.
    -To speed up game, as the game can tend to go on forever, after a certain turn (30?) instead of taking the other player's cards the losing card is instead discarded completely.