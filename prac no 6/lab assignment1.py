string = input("Enter a string: ")

vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for character in string:

    if (character == 'a' or character == 'e' or character == 'i' or
        character == 'o' or character == 'u' or
        character == 'A' or character == 'E' or character == 'I' or
        character == 'O' or character == 'U'):
        vowel_count = vowel_count + 1

    elif character.isalpha():
        consonant_count = consonant_count + 1

    if character == ' ':
        space_count = space_count + 1

    if character.islower():
        lowercase_count = lowercase_count + 1

print("Number of Vowels =", vowel_count)
print("Number of Consonants =", consonant_count)
print("Number of Spaces =", space_count)
print("Number of Lowercase Letters =", lowercase_count)