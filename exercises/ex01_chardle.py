"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730554082"

counter = 0
fiveCharacterWord: str = input("Enter a 5-character word: ")

if len(fiveCharacterWord) != 5:
    print("Error: Word must contain 5 characters")
    exit()

singleCharacter: str = input("Enter a single character: ")

if len(singleCharacter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + singleCharacter + " in " + fiveCharacterWord)

if fiveCharacterWord[0] == singleCharacter:
    print(singleCharacter + " found at index 0")
    counter = counter + 1
if fiveCharacterWord[1] == singleCharacter:
    print(singleCharacter + " found at index 1")
    counter = counter + 1
if fiveCharacterWord[2] == singleCharacter:
    print(singleCharacter + " found at index 2")
    counter = counter + 1
if fiveCharacterWord[3] == singleCharacter:
    print(singleCharacter + " found at index 3")
    counter = counter + 1
if fiveCharacterWord[4] == singleCharacter:
    print(singleCharacter + " found at index 4")
    counter = counter + 1

if counter > 1:
    print(str(counter) + " instances of " + singleCharacter + " found in " + fiveCharacterWord)
if counter == 1:
    print(str(counter) + " instance of " + singleCharacter + " found in " + fiveCharacterWord)
if counter == 0:
    print("No instances of " + singleCharacter + " found in " + fiveCharacterWord)