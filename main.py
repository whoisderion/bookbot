def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        count_characters(file_contents)

def count_words(string):
    return len(string.split())

def count_characters(string):
    char_count = {}
    for word in string.lower().split():
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    print(char_count)

main()