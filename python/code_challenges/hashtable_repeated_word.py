import re


def first_repeated_word(words:str) -> any:
    dictionary = {}
    words = re.sub(r'[^a-zA-Z\s]', '', words.lower())
    split_words = words.split()

    for word in split_words:
        if word in dictionary:
            return word
        else:
            dictionary[word] = 1

    return None

def count_words(words:str) -> dict:
    dictionary = {}
    words = re.sub(r'[^a-zA-Z\s]', '', words.lower())
    split_words = words.split()

    for word in split_words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

def most_frequent_words(words:str) -> str:
    dictionary = {}
    words = re.sub(r'[^a-zA-Z\s]', '', words.lower())
    split_words = words.split()

    for word in split_words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
    return sorted_dictionary[0][0]

if __name__ == '__main__':
    print(first_repeated_word('The quick brown fox jumps over the lazy dog dog dog dog dog'))
    print(count_words('The quick brown fox jumps over the lazy dog dog dog dog dog dog'))
    print(most_frequent_words('The quick brown fox jumps over the lazy dog dog dog dog'))

