from collections import defaultdict
import pathlib

def main():
    path = get_local_path()
    book_path = path + "books/frankenstein.txt"
    book_name = book_path.split("/").pop()
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_chars(book_text)
    counted_chars_list = sort_chars_dict(chars_dict)
    
    nl(1)
    print(f"-- Book report of {book_name} ---\n",
          f"{num_words} words in the document")
    print_chars(counted_chars_list)
    
    return 0

# Function that returns path to current directory
def get_local_path():
    return str(pathlib.Path(__file__).parent.resolve()) + "/"

# Function to print each character and its frequency
def print_chars(char_dict_list):
    for char_info in char_dict_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")

# Function to count the number of words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to return the "num" value from a dictionary, used for sorting
def sort_on(dict_list):
    return dict_list["num"]

# Function to sort the character dictionary by frequency in descending order
def sort_chars_dict(num_chars_dict):
    char_dict_list = []  # List to hold dictionaries of character counts
    
    # Convert the character count dictionary to a list of dictionaries
    for key in num_chars_dict:
        char_dict_list.append({"char" : key, "num" : num_chars_dict[key]})
    
    # Sort the list of dictionaries by frequency in descending order
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

# Function to count each alphabetic character in a text
def get_chars(text):
    text = text.lower()  # Convert text to lowercase
    char_dicts = defaultdict(int)
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # List of valid characters
    
    # Loop through each character in the text
    for i in range(0, len(text)):
        if text[i] in alphabet: # Check if the character is a valid letter
            char_dicts[text[i]] += 1  # Increment the count for the character
    
    return dict(char_dicts)  # Convert defaultdict to a regular dictionary

# Function to read the content of a file given its path
def get_book_text(path):
    with open(path) as f:  # Open the file in read mode
        return f.read()  # Read and return the entire file content

# Function for printing n new lines
def nl(n=1):
    for i in range(n):
        print("\n")

main()