
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words,chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(words):
    words.split()
    return len(words)

def get_chars_dict(text):
    chars_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_count:
            chars_count[lowered] += 1
        else:
            chars_count[lowered] = 1

    return chars_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(book_path, num_words, chars_dict):
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"|--- Begin report of {book_path} ---|")
    print(f"{num_words} words was found in the document.")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("|--- End Report ---|")

main()
