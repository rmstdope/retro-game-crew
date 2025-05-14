import os
import sys
import yaml
from retro_game_crew.crew import GameBuilderCrew


def run():
    inputs = {
        # 'gamename' : 'pong',
        # 'important_things' : 'that vertical blank sync is enabled and that it is possible to play against a smart computer player',
        'gamename' : 'tetris',
        'important_things' : 'that vertical blank sync is enabled and that the game can be won by clearing all lines',
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