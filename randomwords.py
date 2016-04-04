from random import sample, shuffle, randint
from time import sleep

def get_words():
    with file('/usr/share/dict/words') as f:
        return [word.strip() for word in f.readlines()]

words = get_words()
while True:
    sleep(0.1 * randint(3, 8));
    line = []
    for word in sample(words, randint(5, 15)):
        for i in range(randint(1, 3)):
            line.append(word)
    shuffle(line)
    print(' '.join(line))
