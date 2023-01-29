words = input("Enter your message: ")
wordsLetters = list(words.lower())
encryptedWordLetters = []
encryptedLetters = {
        "a": "😄",
        "b": "😍",
        "c": "😇",
        "d": "🙁",
        "e": "😫",
        "f": "🥺",
        "g": "🤓",
        "h": "😛",
        "i": "😡",
        "j": "😚",
        "k": "😰",
        "l": "🤔",
        "m": "😶",
        "n": "🥳",
        "o": "😎",
        "p": "😦",
        "q": "😈",
        "r": "🤡",
        "s": "😻",
        "t": "😽",
        "u": "😹",
        "v": "🤤",
        "w": "😴",
        "x": "🤑",
        "y": "🤠",
        "z": "🤕",
        "space": "😵"
        }

def encryptLetter(letter):
        if letter in encryptedLetters:
            encryptedWordLetters.append(encryptedLetters[letter])

for i in wordsLetters:
        if i.isspace():
            encryptedWordLetters.append(encryptedLetters["space"])
        else:
            encryptLetter(i)
    
encryptedWord =''.join(encryptedWordLetters)
print(encryptedWord)

code = input("Enter your code: ")
codeEmojis = list(code)
decryptedLetters = []
for enteredEmoji in codeEmojis:
    for letter, emojiCode in encryptedLetters.items():
        if emojiCode == enteredEmoji:
            if letter == "space":
                decryptedLetters.append(" ")
            else:
                decryptedLetters.append(letter)

decryptedWord=''.join(decryptedLetters)

if len(decryptedLetters) == 0:
    print("not correct code entered")
else:
    print(decryptedWord)