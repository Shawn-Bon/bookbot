#stats.py will hold all functions pertaining to analyzing books.
#1/5/2026

def sort_on(items):
    return items["num"]

def sort_stats(char_list):
    char_list.sort(reverse=True, key=sort_on)
    print(char_list)
    return


def convert_list(num_char):
    char_list = []
    for letter in num_char:
        temp_dict = {}
        letter_sum = num_char[letter]
        temp_dict["char"] = letter
        temp_dict["num"] = letter_sum
        char_list.append(temp_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

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
            


