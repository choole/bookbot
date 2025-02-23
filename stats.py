def get_num_words(bookText):
    words = bookText.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    return words


def get_num_letters(words):
    letters = []
    for x in words:
        letters.append(list(x.lower()))
    single_list = [item for sublist in letters for item in sublist]
    char_counts = {char: single_list.count(char) for char in set(single_list)}
    return char_counts


def sort_dictionary(dictionary):
    # sorted = []
    char_list = [{char: count} for char, count in dictionary.items()]
    char_list.sort(key=lambda d: list(d.values())[0], reverse=True)
    return char_list
