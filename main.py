def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = get_words(text)
    letter_count = get_letters(text)
    print_report(text, num_words, letter_count)

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

def print_report(text, num_words, letter_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_letter_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()