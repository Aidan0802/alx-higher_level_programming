#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_sentence = []
    characters = [".", "?", ":"]
    for char in text:
        current_sentence.append(char)
        if char in characters:
            next_index = text.find(char) + 1
            if next_index < len(text) and text[next_index].isspace():
                print("".join(current_sentence).strip())
                print()
                current_sentence = []
    if current_sentence:
        print("".join(current_sentence).strip())
