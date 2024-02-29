def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def get_book_text(path):
    with open(path) as file:
        return file.read()


def get_num_words(text: str):
    words = text.split()
    return len(words)


def get_num_chars(text: str) -> dict:
    letter_appearance = {}
    for char in text:
        # print(f"char {char}")
        lowered_char = char.lower()
        if not lowered_char in letter_appearance:
            letter_appearance[lowered_char] = 1
        letter_appearance[lowered_char] += 1
    return letter_appearance


def get_letters_to_report(text: str) -> list:
    num_chars = get_num_chars(text)
    # print(f"num of letter {num_letters}")
    letters_to_report = []
    for char, count in num_chars.items():
        if char.isalpha():
            letters_to_report.append({"char": char, "count": count})
    letters_to_report.sort(reverse=True, key=lambda item: item["count"])
    return letters_to_report


def print_report(path: str):
    print(f"--- Begin report of {path} ---")
    text = get_book_text(path)
    print(f"{get_num_words(text)} words found in the document")
    print()
    for item in get_letters_to_report(text):
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")


main()
