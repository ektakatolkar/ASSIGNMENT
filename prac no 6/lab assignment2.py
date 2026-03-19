sentence = input("Enter a sentence: ")

capital_sentence = ""

for character in sentence:
    capital_character = character.upper()
    capital_sentence = capital_sentence + capital_character

print("Sentence in CAPITAL LETTERS:")
print(capital_sentence)