from stats import get_num_words, get_num_letters, sort_dictionary
from sys import argv, exit


def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        # print(file_contents)
        return get_num_words(file_contents)


def main():
    if (len(argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {argv[1]}...")
        words = get_book_text(argv[1])
        dictionary = get_num_letters(words)
        print("--------- Character Count -------")
        sortedList = sort_dictionary(dictionary)
        for i in sortedList:
            if (next(iter(i)).isalpha()):
                print(f"{next(iter(i))}: {i[next(iter(i))]}")
        print("============= END ===============")


main()
