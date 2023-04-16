"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left,facing east.
    post-condition: Karel is on the right.
    """
    up()
    cross()
    down()


def up():
    """
    pre:Karel is on the left,facing east.
    post:Karel is on the upper left, facing north.
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def down():
    while front_is_clear():
        move()
    turn_left()


def cross():
    """
    pre:Karel is at the upper left, facing north.
    post:Karel is at the upper right, facing south.
    """
    turn_right()
    move()
    turn_right()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
