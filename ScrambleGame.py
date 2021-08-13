import random


def load_words(WORDLIST_FILENAME):
    print("Loading word list from file...")
    wordlist = list()
    # 'with' can automate finish 'open' and 'close' file
    with open(WORDLIST_FILENAME) as f:
        # fetch one line each time, include '\n'
        for line in f:
            # strip '\n', then append it to wordlist.txt
            wordlist.append(line.rstrip('\n'))
    print(" ", len(wordlist), "words loaded.")

    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


def split_word(random_word):
    return [char for char in random_word]


wordlist = load_words(r"C:\Users\test\PycharmProjects\WordScramble\wordlist.txt")
random_word = choose_word(wordlist)
letters = split_word(random_word)
random.shuffle(letters)
print(letters)
if input(">") == random_word:
    print("you win!!!!")
else:
    print("you lose!!!!")

