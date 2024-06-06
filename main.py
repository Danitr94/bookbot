def main():
    book_path = "books/frankenstein.txt"
    text = read_content(book_path)
    report(text,book_path)


def read_content(path):
    with open(path) as f:
         file_contents = f.read()
         return file_contents
def count_words(g):
    splitted = g.split()
    return len(splitted)
def count_chars(c):
    lower = c.lower()
    dict = {}
    for c in lower:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict
def re_dict(dict):
    list = []
    for entry in dict:
        dict1 = {}
        dict1["char"] = entry
        dict1["amount"] = dict[entry]
        list.append(dict1)
    return list
def sort_on(dict):
    return dict["amount"]
def report(text,book_path):
    word_dict = re_dict(count_chars(text))
    word_dict.sort(reverse=True, key=sort_on)
    counted_words = count_words(text)
    counted_chars = count_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{counted_words} words found in the document")
    for entry in word_dict:
        char = entry["char"]
        amount = entry["amount"]
        if char.isalpha() == True:
            print(f"The '{char}' character was found '{amount}' times")
    print("---- End report ----")

main()