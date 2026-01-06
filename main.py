#Shawn's Bookbot from Boot.dev
#1/5/26

def get_book_text(file_path):
    with open(file_path) as f:
        read_book = f.read()
        print(read_book)

def main():
    #print("Is my main function working?")
    book_contents=get_book_text("books/frankenstein.txt")
    #print(f"{book_contents}")

main()




