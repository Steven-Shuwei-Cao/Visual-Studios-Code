import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

# Define the deck of cards
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
jokers = ['JJ', 'jj']
deck = [v + '-' + s for s in suits for v in values] + jokers

# Shuffle the deck
random.shuffle(deck)

# Set aside three cards
landlord_cards = deck[:3]
deck = deck[3:]

# Distribute the cards to three players
player1 = deck[:17]
player2 = deck[17:34]
player3 = deck[34:]

# Determine the landlord player
face_up_card = deck[0]
landlord = None
if face_up_card in player1:
    landlord = 'Player 1'
    player1 = player1 + landlord_cards
elif face_up_card in player2:
    landlord = 'Player 2'
    player2 = player2 + landlord_cards
else:
    landlord = 'Player 3'
    player3 = player3 + landlord_cards

# Define the main window
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Create the main layout
        layout = QVBoxLayout()

        # Add labels for each player's cards
        layout.addWidget(QLabel('Player 1:'))
        for card in player1:
            layout.addWidget(QLabel(card))
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('Player 2:'))
        for card in player2:
            layout.addWidget(QLabel(card))
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('Player 3:'))
        for card in player3:
            layout.addWidget(QLabel(card))

        # Set the main layout
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())