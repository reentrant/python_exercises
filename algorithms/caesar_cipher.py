alphabet = "abcdefghijklmnopqrstuvwxyz"

word = "iuur"
shift = 6

new_word = ""

if __name__ == '__main__':
    index = alphabet.index(word[0])
    new_word = alphabet[index - shift]
    index = alphabet.index(word[1])
    new_word = new_word + alphabet[index - shift]
    index = alphabet.index(word[2])
    new_word = new_word + alphabet[index - shift]
    index = alphabet.index(word[3])
    new_word = new_word + alphabet[index - shift]
    print("The decoded word is: ")
    print(new_word)
