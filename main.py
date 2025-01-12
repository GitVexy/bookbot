from collections import defaultdict
import pathlib
path = str(pathlib.Path(__file__).parent.resolve()) + "/"

def main():
    book_path = path + "books/frankenstein.txt"
    book_name = book_path.split("/").pop()
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_chars(book_text)
    counted_chars_list = sort_chars_dict(chars_dict)
    
    print(f"--- Book report of {book_name}")
    print(f"{num_words} words in the document")
    print_chars(counted_chars_list)
    
    return 0

def print_chars(char_dict_list):
    for char_info in char_dict_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict_list):
    return dict_list["num"]

def sort_chars_dict(num_chars_dict):
    char_dict_list = []
    
    for key in num_chars_dict:
        char_dict_list.append({"char" : key, "num" : num_chars_dict[key]})
        
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

def get_chars(text):
    text = text.lower()
    char_dicts = defaultdict(int)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(0, len(text)):
        if text[i] in alphabet:
            char_dicts[text[i]] += 1
    
    char_dicts = dict(char_dicts)
    
    return char_dicts

def get_book_text(path):
    with open(path) as f:
        return f.read()

print("\nRunning main():\n")
main()