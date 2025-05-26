import os
import sys
import yaml
from retro_game_crew.crew import GameBuilderCrew


def run():
    inputs = {
        # 'gamename' : 'pong',
        # 'important_things' : 'that vertical blank sync is enabled and that it is possible to play against a not too smart computer player',
        'gamename' : 'tetris',
        'important_things' : 'that vertical blank sync is enabled and that the game can be won by clearing all lines',
        # 'gamename' : 'snake',
        # 'important_things' : 'that vertical blank sync is enabled, that the current score is always visible on screen and that when you die, your score is shown and you get the option to play again',
        # 'gamename' : 'text adventure',
        # 'important_things' : 'that there are at least 5 different rooms and there is a way to win the game',
        # 'gamename' : 'tic-tac-toe',
        # 'important_things' : 'that the game is controlled using the arrow keys',
        # 'gamename' : 'super mario bros',
        # 'important_things' : 'that vertical blank sync is enabled',
    }

    game= GameBuilderCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """

    inputs = {
        'gamename' : 'tetris',
        'important_things' : 'that vertical blank sync is enabled and that the game can be won by clearing all lines',
    }
    try:
        GameBuilderCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")