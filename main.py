def opener(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    bookpath= "books/frankenstein.txt"
    book_contents = opener(bookpath)
    print(book_contents)
    print("Here is the word count:", count_words(book_contents))
    # print(count_letters(book_contents))
    sorted = sort_letters(count_letters(book_contents))
    for splitten in sorted:
        occured = splitten["num"]
        named = splitten["name"]
        print(f"The '{named}' character was found {occured} times")

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

def sort_letters(character_dict):
    def sort_num(split_list):
        return split_list["num"]
    list_of_dicts = []
    for pair in character_dict:
        split = {"name": pair[0], "num": character_dict[pair]}
        list_of_dicts.append(split)
    list_of_dicts.sort(reverse=True, key=sort_num)
    return list_of_dicts

main()