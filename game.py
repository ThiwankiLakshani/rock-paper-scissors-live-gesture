import random
from gesture import CHOICES

class ScoreBoard:
    def __init__(self):
        self.player = 0
        self.ai = 0

    def update(self, result):
        if result == "Win":
            self.player += 1
        elif result == "Lose":
            self.ai += 1

    def reset(self):
        self.player = 0
        self.ai = 0

def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "Tie"
    winning_combinations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    if winning_combinations[player_choice] == ai_choice:
        return "Win"
    return "Lose"

def get_ai_choice():
    return random.choice(CHOICES) 