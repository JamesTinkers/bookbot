def opener(filepath):
    with open(filepath) as book:
        return book.read()
def main():
    bookpath= "books/frankenstein.txt"
    book_contents = opener(bookpath)
    print(book_contents)
    print(count_words(book_contents))
def count_words(content):
    words = content.split()
    return len(words)
main()