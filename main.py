import sys 
from stats import number_of_words
from stats import counting_letters
from stats import sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    text = get_book_text(sys.argv[1])
    all_words = number_of_words(text)
    all_letters = counting_letters(text)
    
    # Call the sorted_list function with all_letters
    list_sorted = sorted_list(all_letters)
    
    # Print the report according to the desired format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {all_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in list_sorted:
        char = char_dict['char']
        count = char_dict['count']
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
main()