def opener(filepath):
    with open(filepath) as book:
        return book.read()
def main():
    bookpath= "books/frankenstein.txt"
    book_contents = opener(bookpath)
    print(book_contents)
    print("Here is the word count:", count_words(book_contents))
    print(count_letters(book_contents))

def count_words(content):
    words = content.split()
    return len(words)
def count_letters(content):
    lowered_content = content.lower()
    letter_count_dict = {}
    for letter in lowered_content:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1
    return letter_count_dict
main()