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
        print("\033[38;5;245m=========\033[0m")
    elif man == 1:
        print("\033[38;5;130m      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 2:
        print("\033[38;5;130m      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 3:
        print("\033[38;5;130m  ----+  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 4:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("      |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 5:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("      |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 6:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("\033[31m  |\033[38;5;130m   |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 7:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("\033[31m /|\033[38;5;130m   |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 8:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("\033[31m /|\\\033[38;5;130m  |  ")
        print("     /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 9:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("\033[31m /|\\\033[38;5;130m  |  ")
        print("\033[34m /\033[38;5;130m   /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")

    elif man == 10:
        print("\033[38;5;130m  +---+  ")
        print("  |   |  ")
        print("\033[38;5;223m  O\033[38;5;130m   |  ")
        print("\033[31m /|\\\033[38;5;130m  |  ")
        print("\033[34m / \\\033[38;5;130m /|  ")
        print("    / |  ")
        print("\033[38;5;245m=========\033[0m")


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
print("\033[34m-----Hang Man-----\033[0m")
print()
begin = False

while begin == False:
    print("\033[34mSelect mode:")
    print("1 - 1 Player (random word)")
    print("2 - 2 Player (Player 1 chooses a word)\033[0m")
    mode = input("\033[34m> ")
    begin = False
    if mode == "1":
        begin = True
        word = random.choice(randomWords)
        print()
        print("Random word selected! Begin guessing.\033[0m")
        print()
        guessed = ""

    elif mode == "2":
        begin = True
        go = False
        while go == False:
            print()
            print("Player 1: enter your word for player 2 to guess:\033[0m")
            word = str(input("\033[34m> "))
            guessed = ""
            print()
            print("Your word: ", word, ". Confirm?[y,n]\033[0m")
            yn = str(input("\033[34m> "))
            print()
            if yn == "y":
                go = True

    else:
        print("\033[31mInvalid selection. Please enter [1,2].\033[0m")

for j in range(len(word)):
    guessed = guessed + "_"

if mode == 2:

    for counter in range(52):
        print()

while alive and not won:
    render_man()
    print()
    print("\033[34mGuessed so far: ", render_word_with_spaces(guessed))
    print()
    print("Letters tried: ", used, "\033[0m")
    go = False

    while go == False:
        print("\033[34mGuess a letter of the word:\033[0m")
        letter = str(input("\033[34m> "))

        if not len(letter) == 1:
            print()
            print("\033[31mPlease enter exactly ONE letter.\033[0m")
            print()

        elif letter in used:
            print()
            print("\033[31mLetter already used!\033[0m")
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
        print("\033[33mThe letter ", letter, " is not in the word!\033[0m")
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
        print("\033[32mYOU WIN!")
        print()
        print("THE WORD WAS: ", word, "\033[0m")
        print()
    else:
        print()
        print("\033[33mPLAYER 2 WINS!")
        print()
        print("THE WORD WAS: ", word, "\033[0m")

else:
    if mode == "1":
        print()
        print("\033[31mYOU LOSE!")
        print()
        print("THE WORD WAS: ", word)
        print("YOU GOT: ", guessed, "\033[0m")
        print()

    else:
        print()
        print("\033[33mPLAYER 1 WINS!")
        print()
        print("THE WORD WAS: ", word)
        print("PLAYER TWO GOT: ", guessed, "\033[0m")
        print()
