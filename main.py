#Shawn's Bookbot from Boot.dev
#1/5/26

#-- Imports --
from stats import word_counter
from stats import char_counter
from stats import sort_stats
from stats import sort_on
from stats import convert_list

def get_book_text(file_path):
    with open(file_path) as f:
        read_book = f.read()
    return read_book


def main():
    
    book_contents=get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_contents)
    num_char = char_counter(book_contents)
    list_results = convert_list(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print(f"----------- Character Count ----------")
    print(f"First we nest dictionaries in a list: {list_results}")


main()




