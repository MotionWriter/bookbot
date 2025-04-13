import sys
from stats import get_num_words
from stats import count_characters
from stats import sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file = sys.argv[1]

def main():
    words = get_book_text(file)
    count = get_num_words(words)
    char_dict = count_characters(words)
    sort = sorted_list(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{file}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sort:
        char = i["char"]
        if char.isalpha():
            count = i["count"]
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()