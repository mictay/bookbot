
def main():
    book = "books/frankenstein.txt"
    lettersDic: dict = {}

    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()

    print(f"--- Begin report of {book} ---")
    print(f"{len(words)} words found in the document")

    for word in words:
        seen_letters = {} #don't want to count letters twice in the same word
        for character in word.lower():
            if seen_letters.get(character):
                continue
            if not character.isalpha():
                continue
            if not lettersDic.get(character):
                lettersDic[character] = 0

            seen_letters[character] = True
            lettersDic[character] += countCharacterIgnoreCase(word, character)

    sorted_letters = sorted(lettersDic.items(), key=lambda x:x[1], reverse=True)
    # ie: sorted_letters = [('e', 46043), ('t', 30365), ('a', 26743),...

    for key in sorted_letters:
        print(f"The {key[0]} was found {lettersDic[key[0]]} times")

    #print(lettersDic)

    print("--- End report ---")

def countCharacterIgnoreCase(stringElement: str, character: str):
    lowerCase = stringElement.lower()
    return lowerCase.count(character.lower())


main()

