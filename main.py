import random


def load_words(WORDLIST_FILENAME):
    wordlist = list()
    # 'with' can automate finish 'open' and 'close' file
    with open(WORDLIST_FILENAME) as f:
        # fetch one line each time, include '\n'
        for line in f:
            # strip '\n', then append it to wordlist.txt
            wordlist.append(line.rstrip('\n'))

        return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


def split_word(random_word):
    return [char for char in random_word]


print("Welcome to Scramble")
print("Type start to begin the game")
print("Type change to change difficulty")
print("Type quit to end the program")
command = ""
difficulty = input("choose easy, medium, or hard >>>")
if difficulty == "easy":
    difficulty = "dictionaryEasy.txt"
elif difficulty == "medium":
    difficulty = "dictionaryMedium.txt"
elif difficulty == "hard":
    difficulty = "dictionaryHard.txt"
else:
    print("unknown command")
while command != "quit":

    command = input(">>>")

    if command == "start":

        wordlist = load_words(difficulty)
        random_word = choose_word(wordlist)
        letters = split_word(random_word)
        random.shuffle(letters)
        print(letters)

        guess_count = 0
        guess_limit = 3
        while guess_count < guess_limit:
            guessed_word = input(">>>")
            guess_count += 1
            if guessed_word == random_word:
                print("you win!!!!")
                print("Type start to play again!!!")
                print("Type change to change difficulty")
                print("Type quit to end the program")
                break
            else:

                print("try again")
        else:
            print(random_word)
            print("you lose!!!")
            print("type start to play again")
    elif command == "quit":
        print("thank you for playing!!!")
        break
    elif command == "change":
        difficulty = input("Choose easy, medium, or hard: ")
        if difficulty == "easy":
            difficulty = "dictionaryEasy.txt"
        elif difficulty == "medium":
            difficulty = "dictionaryMedium.txt"
        elif difficulty == "hard":
            difficulty = "dictionaryHard.txt"
        else:
            print("unknown command")
    else:
        print("I do not understand")
