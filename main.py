#Shawn's Bookbot from Boot.dev
#1/5/26

#-- Imports --
from stats import word_counter
from stats import char_counter


def get_book_text(file_path):
    with open(file_path) as f:
        read_book = f.read()
    return read_book


def main():
    
    #print("Is my main function working?")
    book_contents=get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_contents)

    num_char = char_counter(book_contents)
    
    print(f"Found {num_words} total words.")
    print(f"{num_char}")

main()




