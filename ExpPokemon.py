# Pokémon Experience growing type
# https://bulbapedia.bulbagarden.net/wiki/Experience

def input_check(level):
    valid = False
    while not valid:
        level = input('Pokemon level: ')
        try:
            level = int(level)
            valid = True
        except ValueError:
            print('This is not a level')
        else:
            if level in range(2, 101):
                return str(level)  # Level is valid
            elif level == 0:
                print("FINISHED")
                return "0"  # Level is valid, but exit the program
            else:
                print('Level out of range')
                return None  # Level is not valid


def erratic(level):
    if 0 < level <= 50:
        e = (level ** 3 * (100 - level)) / 50
    elif 51 <= level <= 68:
        e = (level ** 3 * (150 - level)) / 100
    elif 69 <= level <= 98:
        e = (level ** 3 * ((1911 - 10 * level) / 3)) / 50
    else:
        e = (level ** 3 * (160 - level)) / 100
    print("erratic     ", int(e))


def fast(level):
    e = 0.8 * level ** 3
    print("fast        ", int(e))


def medium_fast(level):
    e = level ** 3
    print("medium fast ", int(e))


def medium_slow(level):
    e = 1.2 * level ** 3 - 15 * level ** 2 + 100 * level - 140
    print("medium slow ", int(e))


def slow(level):
    e = 1.25 * level ** 3
    print("slow        ", int(e))


def fluctuating(level):
    if 0 < level <= 50:
        e = (level ** 3 * (24 + (level + 1) / 3)) / 50
    elif 51 <= level <= 68:
        e = (level ** 3 * (14 + level)) / 50
    else:
        e = (level ** 3 * (32 + (level / 2)) / 50)
    print("fluctuanting", int(e))


def main(level=None):
    print("Press 0 to exit")
    while True:
        level = input_check(level)
        if level is None:
            continue  # Skip calculations and ask for a new level
        if level == "0":
            break  # Exit the loop if level is "0"
        level = int(level)  # Convert the level string to an integer
        erratic(level)
        fast(level)
        medium_fast(level)
        medium_slow(level)
        slow(level)
        fluctuating(level)


if __name__ == "__main__":
    main()
