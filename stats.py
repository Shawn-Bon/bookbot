#stats.py will hold all functions pertaining to analyzing books.
#1/5/2026

def word_counter(current_book):
    count = 0
    words = current_book.split()
    count = len(words)
    return count
