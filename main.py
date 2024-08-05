def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        count_obj = count_characters(file_contents)
        sorted_arr = organize(count_obj)
        report(sorted_arr, word_count)

def count_words(string):
    return len(string.split())

def count_characters(string):
    char_count = {}
    for word in string.lower().split():
        for char in word:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return(char_count)

def sort_on(dict):
    return dict["count"]

def organize(char_count):
    characters = []
    for char in char_count:
        characters.append({"char": char, "count": char_count[char]})
    characters.sort(reverse=True, key=sort_on)
    return characters

def report(arr, count):
    print(f"--- Begin report of books/frankenstein.txt ---\n${count} words found in the document\n")
    for char_obj in arr:
        print(f"The '{char_obj['char']}' character was found {char_obj['count']} times\n")
    print("--- End report ---")


main()