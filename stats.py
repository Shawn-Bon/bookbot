#stats.py will hold all functions pertaining to analyzing books.
#1/5/2026

def word_counter(current_book):
    count = 0
    words = current_book.split()
    count = len(words)
    return count

def char_counter(current_book):
    book_lowercase = current_book.lower()
    dict_char = {}

    for char in book_lowercase:
        if char == "\ufeff":
            continue
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    return dict_char
            


