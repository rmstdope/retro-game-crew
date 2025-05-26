# Retro Game Crew

A multi-AI-agent project powered by [crewAI](https://crewai.com) that tries to implement simple retro style games in Python.

# Setup

## Setup a virtua environment

Create a virtual environment for the project

`python3.12 -m venv .venv`

Activate it

`source .venv/bin/activate`

(or whatever way that is done for your environment)

## Install dependencies

To install CrewAI and its dependencies, use pip

`pip install .`

# Setup your Gemeni API key

Create an .env file in the root folder and puy your Gemeni API key there:

`GEMINI_API_KEY=<Enter API key here>`

# Select a retro game

Select one of the games defined in main.py or simple add youre own to liness of 'game' and 'important_things'. E.g.

```python
    inputs = {
        # 'gamename' : 'pong',
        # 'important_things' : 'that vertical blank sync is enabled and that it is possible to play against a not too smart computer player',
        'gamename' : 'tetris',
        'important_things' : 'that vertical blank sync is enabled and that the game can be won by clearing all lines',
        # 'gamename' : 'snake',
        # 'important_things' : 'that vertical blank sync is enabled, that the current score is always visible on screen and that when you die, your score is shown and you get the option to play again',
        # 'gamename' : 'text adventure',
        # 'important_things' : 'that there are at least 5 diffferent rooms and there is a way to win the game',
        # 'gamename' : 'tic-tac-toe',
        # 'important_things' : 'that the game is controlled using the arrow keys',
        # 'gamename' : 'super mario bros',
        # 'important_things' : 'that vertical blank sync is enabled',
    }
```

# Build

`crewai install`

# Run

Run the crew using

`crewai run`

This will produce two files in the output directory.

- research.txt - A document with the result of the research done by the Game Researcher Agent
- game.py - A file with the game code.
