# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choice

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    prev = opponent_history[-1]

    return guess(prev)

def guess(hand):
    if hand == "P":
        return "S"
    elif hand =="R":
        return "P"
    elif hand =="S":
        return "R"
    return choice(["R", "P", "S"])