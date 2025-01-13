def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase_text = text.lower()
    character_dict  = {}
    for character in lowercase_text:
        character_dict [character] = character_dict .get(character, 0) + 1
    return character_dict 

def dict_isalpha(dictionary):
    new_list = []

    for char, count in dictionary.items():
        if char.isalpha():
            temp_dict = {"char" : char, "count" : count}
            new_list.append(temp_dict)
    return new_list

def sort_on(dictionary):
    return dictionary["count"]

def main():
    book_path = "books/frankenstein.txt"
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