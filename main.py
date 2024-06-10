def letter_count(book):
    dic = {}
    low_book = book.lower()
    character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z' , 'x', 'c', 'v', 'b', 'n', 'm']

    for letter in low_book:
        if letter in character_list:
            if letter not in dic:
                dic.update({letter: 1})
            else:
                dic[letter] += 1

    return dic

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        print(len(words))
        print(letter_count(str(words)))

main()
