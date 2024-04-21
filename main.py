def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        print(f.read())

main()