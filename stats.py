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