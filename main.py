def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as file:
        return file.read()


def get_num_words(text: str):
    words = text.split()
    return len(words)


def get_num_letters(text: str):
    lowered_string = text.lower()
    letter_appearance = {}
    for letter in lowered_string:
        if not letter in letter_appearance:
            letter_appearance[letter] = 1
        letter_appearance[letter] += 1
    return letter_appearance


main()
