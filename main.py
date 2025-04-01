import curses
import random
from curses import wrapper

strings = ["Hello my name is Rufus, I like to eat bacon!", "Let's talk on the phone at around two pm.", "Everybody needs a drink sometimes, it helps with your mood."]


def main(stdscr):
    
    # initialise colours for typing input
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # select random string from bank of scentences
    chosen_string = strings[random.randint(0,2)]

    # initialise terminal screen and variables
    stdscr.clear()
    stdscr.addstr(4, 5, "Copy this scentence!")
    stdscr.addstr(5, 5, chosen_string)
    input = []
    input_colors = []
    index = 0
    first_stroke = True

    while True:

        # Start timer
        if first_stroke:
            
        
        # Get keystroke and determine correct / incorrect chars
        key = stdscr.getch()
        if key in (8, 127, curses.KEY_BACKSPACE) and index > 0:
            index -= 1
            input.pop()
            input_colors.pop()
        elif 32 <= key <= 126:
            input.append(chr(key))
            input_colors.append(2 if chr(key) == chosen_string[index] else 1)
            index += 1
        elif key == 27:
            break

        # display text
        stdscr.addstr(4, 5, "Copy this scentence!")
        stdscr.addstr(5, 5, chosen_string)
        stdscr.addstr(6, 5, "Chars / min: ")
        stdscr.addstr(10, 5, "Press 'Esc' to exit.")
        
        # add typed text
        x, y = (5, 5)
        for i, char in enumerate(input):
            stdscr.addstr(x, y + i, char, curses.color_pair(input_colors[i]))

        stdscr.refresh()

wrapper(main)