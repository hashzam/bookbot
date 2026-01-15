import sys
print("Usage: python3 main.py <path_to_book>")
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
from stats import get_num_words, get_characters, sort_ch
def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    chars = get_characters(book_text)
    sorted_dict = sort_ch(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")

main()