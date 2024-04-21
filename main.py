def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = len(text.split())
    print(f"The frankenstein book has {num_words} words!")

def get_text(path):
    with open(path) as f:
        return f.read()

main()