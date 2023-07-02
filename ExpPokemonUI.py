# Pokémon Experience growing type
# https://bulbapedia.bulbagarden.net/wiki/Experience

import tkinter as tk


def input_check():
    level = nivel_entry.get()
    try:
        level = int(level)
        if 2 <= level <= 100:
            return level
        else:
            raise ValueError
    except ValueError:
        error_label.config(text="Level out of range")
        return None


def calculate():
    level = input_check()
    if level is not None:
        erratic(level)
        fast(level)
        medium_fast(level)
        medium_slow(level)
        slow(level)
        fluctuating(level)


def erratic(level):
    if 0 < level <= 50:
        e = (level ** 3 * (100 - level)) / 50
    elif 51 <= level <= 68:
        e = (level ** 3 * (150 - level)) / 100
    elif 69 <= level <= 98:
        e = (level ** 3 * ((1911 - 10 * level) / 3)) / 50
    else:
        e = (level ** 3 * (160 - level)) / 100
    erratic_label.config(text="erratic: " + str(int(e)))


def fast(level):
    e = 0.8 * level ** 3
    fast_label.config(text="fast: " + str(int(e)))


def medium_fast(level):
    e = level ** 3
    medium_fast_label.config(text="medium fast: " + str(int(e)))


def medium_slow(level):
    e = 1.2 * level ** 3 - 15 * level ** 2 + 100 * level - 140
    medium_slow_label.config(text="medium slow: " + str(int(e)))


def slow(level):
    e = 1.25 * level ** 3
    slow_label.config(text="slow: " + str(int(e)))


def fluctuating(level):
    if 0 < level <= 50:
        e = (level ** 3 * (24 + (level + 1) / 3)) / 50
    elif 51 <= level <= 68:
        e = (level ** 3 * (14 + level)) / 50
    else:
        e = (level ** 3 * (32 + (level / 2)) / 50)
    fluctuanting_label.config(text="fluctuating: " + str(int(e)))


def main():
    global nivel_entry, error_label, erratic_label, fast_label, medium_fast_label, medium_slow_label, slow_label, \
        fluctuanting_label

    # Create the main window
    window = tk.Tk()
    window.title("Pokémon Experience growing type calculator")
    window.minsize(550, 300)

    # Create and place the input elements
    nivel_label = tk.Label(window, text="Pokémon level:")
    nivel_label.pack()
    nivel_entry = tk.Entry(window)
    nivel_entry.pack()

    # Create and place the error label
    error_label = tk.Label(window, text="")
    error_label.pack()

    # Create and place the calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate)
    calculate_button.pack()

    # Create and place the result labels
    erratic_label = tk.Label(window, text="")
    erratic_label.pack()

    fast_label = tk.Label(window, text="")
    fast_label.pack()

    medium_fast_label = tk.Label(window, text="")
    medium_fast_label.pack()

    medium_slow_label = tk.Label(window, text="")
    medium_slow_label.pack()

    slow_label = tk.Label(window, text="")
    slow_label.pack()

    fluctuanting_label = tk.Label(window, text="")
    fluctuanting_label.pack()

    # Run the main loop
    window.mainloop()


if __name__ == "__main__":
    main()
