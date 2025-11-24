import random

alive = True
won = False
man = 0
used = []
guessed = ""
randomWords = [
    "python",
    "hangman",
    "computer",
    "program",
    "random",
    "challenge",
    "science",
    "elephant",
    "galaxy",
    "mystery",
    "keyboard",
    "guessing",
    "puzzle",
    "circuit",
    "mouse",
    "superb",
    "great",
    "book",
    "piano",
    "chips",
    "creeper",
    "minecraft",
    "minecart",
    "code",
    "binary",
    "headphones",
    "dog",
    "alphabet",
    "painting",
    "firefighter",
    "thinking",
    "humble",
    "incompressible",
    "jumping",
    "laughing",
    "nothing",
    "optical",
    "queen",
    "game",
    "something",
    "unhappy",
    "vortex",
    "words",
    "xylophone",
    "yellow",
    "zebra",
    "radiation",
    "electrical",
    "impostor",
    "task",
    "admin",
    "cafeteria",
    "meltdown",
    "metadata",
    "programming",
    "music",
    "house",
    "mario",
    "goomba",
    "bowser",
    "koopa",
    "blocks",
    "pickaxe",
    "tools",
    "crewmate",
    "enderman",
    "mushroom",
    "piranha",
    "pipe",
    "plumber",
    "medbay",
    "ghast",
    "artificial",
    "intelligence",
    "politics",
    "cat",
    "pseudopseudohypoparathyroidism",
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "trophy",
    "mathematics",
    "floccinaucinihilipilification",
    "hippopotomonstrosesquippedaliophobia",
    "antidisestablishmentarianism",
    "supercalifragilisticexpialidocious",
    "Eellogofusciouhipoppokunurious",
    "Hexakosioihexekontahexaphobia",
    "Spectrophotofluorometrically",
    "Honorificabilitudinitatibus",
    "bus",
]


def render_man():
    global man
    if man == 0:
        print()
        print()
        print()
        print()
        print()
        print()
        print("=========")
    elif man == 1:
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("=========")

    elif man == 2:
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 3:
        print("  ----+  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 4:
        print("  +---+  ")
        print("  |   |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 5:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 6:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print("  |   |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 7:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|   |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 8:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\\  |  ")
        print("     /|  ")
        print("    / |  ")
        print("=========")

    elif man == 9:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\\  |  ")
        print(" /   /|  ")
        print("    / |  ")
        print("=========")

    elif man == 10:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\\  |  ")
        print(" / \\ /|  ")
        print("    / |  ")
        print("=========")


def replace_at(string, index, new_char):
    return string[:index] + new_char + string[index + 1 :]


def render_word_with_spaces(word: str) -> str:
    """
    This function takes a word string and returns a new string
    with each character separated by a space.
    For example, "python" becomes "p y t h o n"
    Args:
        word: The word to render
    Returns:
        A string with each character separated by a space
    """
    return " ".join(list(word))


# Main program
print()
print("-----Hang Man-----")
print()
print("Select mode:")
print("1 - 1 Player (random word)")
print("2 - 2 Player (Player 1 chooses a word)")
mode = input("> ")
begin = False

while begin == False:
    if mode == "1":
        begin = True
        word = random.choice(randomWords)
        print()
        print("Random word selected! Begin guessing.")
        print()
        guessed = ""

    elif mode == "2":
        begin = True
        go = False
        while go == False:
            print()
            print("Player 1: enter your word for player 2 to guess:")
            word = str(input("> "))
            guessed = ""
            print()
            print("Your word: ", word, ". Confirm?[y,n]")
            yn = str(input("> "))
            print()
            if yn == "y":
                go = True

    else:
        print("Invalid selection. Please enter [1,2].")

for j in range(len(word)):
    guessed = guessed + "_"

if mode == 2:

    for counter in range(52):
        print()

while alive and not won:
    render_man()
    print()
    print("Guessed so far: ", render_word_with_spaces(guessed))
    print()
    print("Letters tried: ", used)
    go = False

    while go == False:
        print("Guess a letter of the word:")
        letter = str(input("> "))

        if not len(letter) == 1:
            print()
            print("Please enter exactly ONE letter.")
            print()

        elif letter in used:
            print()
            print("Letter already used!")
            print()

        else:
            used.append(letter)
            go = True

    go = False

    if letter in word:

        indexes = [y for y, char in enumerate(word) if char == letter]
        for x in indexes:
            guessed = replace_at(guessed, x, letter)

    else:
        print("The letter ", letter, " is not in the word!")
        man = man + 1

    print()

    if man >= 10:
        alive = False

    if guessed == word:
        won = True

render_man()

if won == True:
    if mode == "1":
        print()
        print("YOU WIN!")
        print()
        print("THE WORD WAS: ", word)
        print()
    else:
        print()
        print("PLAYER 2 WINS!")
        print()
        print("THE WORD WAS: ", word)

else:
    if mode == "1":
        print()
        print("YOU LOSE!")
        print()
        print("THE WORD WAS: ", word)
        print("YOU GOT: ", guessed)
        print()

    else:
        print()
        print("PLAYER 1 WINS!")
        print()
        print("THE WORD WAS: ", word)
        print("PLAYER TWO GOT: ", guessed)
        print()
