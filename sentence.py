
def sentence_checker():
    text = input("please enter a sentence: ")
    count = 0
    vowels = 0
    consonants = 0
    vowel = ["a", "e", "i", "u", "o"]
    space = 0

    for char in text:
        # checks for vowels
        #if (char == "a") or (char == "e") or (char == "i") or (char == "u") or (char == "o"):
        if char in vowel:
            vowels +=1
        elif char == " ":
            space +=1
        # checks for consonants
        else:
            consonants +=1
        # counts the number of characters
        count += 1
    print(f"The number of characters: {count - space}")
    print(f"The number of vowels: {vowels}")
    print(f"The number of consonants: {consonants}")

# counts the number of each word and the total number of words
    words = text.split()
    word_counts = {}
    total_words = 0
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        total_words += 1

    print(f"Total number of each word: {word_counts}")
    print(f"Total count of words: {total_words}")

sentence_checker()