import curses
import random
from curses import wrapper

strings = ["Hello my name is Rufus, I like to eat bacon!", "Let's talk on the phone at around two pm.", "Everybody needs a drink sometimes, it helps with your mood."]


def main(stdscr):
    random_str = strings[random.randint(0,2)]
    stdscr.clear()
    stdscr.addstr(4, 5, "Copy this scentence!")
    stdscr.addstr(5, 5, random_str)
    input = ""

    while True:
        
        keyStrokes = 0
        key = stdscr.getch()
        input += chr(key)

        stdscr.addstr(4, 5, "Copy this scentence!")
        stdscr.addstr(5, 5, random_str)
        stdscr.addstr(6, 5, "Chars / min: ")
        stdscr.addstr(10, 5, "Press 'Esc' to exit.")
        stdscr.addstr(5, 5, input)

        if key == 27:
            break

        stdscr.refresh()

wrapper(main)