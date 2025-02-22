import sys
from stats import get_book_text, get_word_count, char_count, dict_isalpha, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_dict = char_count(text)
    character_list = dict_isalpha(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for char_dict in character_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")

main()