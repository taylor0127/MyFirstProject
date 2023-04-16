"""
File: DoubleBeepers.py
Name:Taylor
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_beepers_back()
    karel_goes_home()


def double_beepers():
    while on_beeper():
        # old beepers, facing East
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beepers, facing East
        turn_around()
        move()
        # new beepers, facing West
        turn_around()


def turn_around():
    turn_left()
    turn_left()


def put_beepers_back():
    move()
    while on_beeper():
        # old beepers, facing East
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def karel_goes_home():
    turn_around()
    move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
