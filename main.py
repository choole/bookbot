from stats import get_num_words, get_num_letters, sort_dictionary


def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        # print(file_contents)
        return get_num_words(file_contents)


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    words = get_book_text("./books/frankenstein.txt")
    dictionary = get_num_letters(words)
    print("--------- Character Count -------")
    sortedList = sort_dictionary(dictionary)
    for i in sortedList:
        if (next(iter(i)).isalpha()):
            print(f"{next(iter(i))}: {i[next(iter(i))]}")
    print("============= END ===============")


main()
