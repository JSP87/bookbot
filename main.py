
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words>(text)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(words):
    words.split()
    return words

main()
