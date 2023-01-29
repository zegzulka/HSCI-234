
from datetime import datetime as dt

from utils import add_class, remove_class


wordsInput = Element("input")

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

def showResult(function):
    print(function)

def getEncryptedMessage():
    words = wordsInput.element.value
    wordsLetters = list(words.lower())
    encryptedWordLetters = []
    def encryptLetter(letter):
            if letter in encryptedLetters:
                encryptedWordLetters.append(encryptedLetters[letter])

    for i in wordsLetters:
            if i.isspace():
                encryptedWordLetters.append(encryptedLetters["space"])
            else:
                encryptLetter(i)
        
    encryptedWord =''.join(encryptedWordLetters)

    def encryptedResult():
         if len(encryptedWord) == 0:
            return "You have to enter words."
         else:
            return encryptedWord
         
    showResult(encryptedResult())


def getDecryptedMessage():   
    codeInput = wordsInput.element.value
    codeEmojis = list(codeInput)
    decryptedLetters = []
    for enteredEmoji in codeEmojis:
        for letter, emojiCode in encryptedLetters.items():
            if emojiCode == enteredEmoji:
                if letter == "space":
                    decryptedLetters.append(" ")
                else:
                    decryptedLetters.append(letter)

    decryptedWord=''.join(decryptedLetters)

    def decryptedResult():
        if len(decryptedLetters) == 0:
            return "You have to enter emojis."
        else:
            return decryptedWord

    showResult(decryptedResult())