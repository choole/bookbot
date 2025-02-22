from stats import get_num_words


def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        # print(file_contents)
        get_num_words(file_contents)


def main():
    get_book_text("./books/frankenstein.txt")


main()

