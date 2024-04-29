def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for k, v in sort_char_nums(count_characters(text)).items():
        print(f"The '{k}' character appears {v} times.")
    print(f"--- End report of {book_path} ---")
        
def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    c = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in c:
                c[lowered] += 1
            else:
                c[lowered] = 1
    return c

def sort_char_nums(chars: dict):
    return {k: v for k, v in sorted(chars.items(), key = lambda item: item[1], reverse=True)}
    
if __name__ == "__main__":
    main()
