def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = get_words(text)
    letter_count = get_letters(text)
    sorted_letter_count = sort_dict(letter_count)
    print_report(sorted_letter_count, num_words)

def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_words(text):
    return len(text.split())

def get_letters(text):
    letter_count = {}
    for char in text.lower():
        letter_count[char] = letter_count.get(char, 0) + 1 
    return letter_count

def sort_dict(letter_dict):
    return sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)
    

def print_report(sorted_dict, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for letter, count in sorted_dict:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()