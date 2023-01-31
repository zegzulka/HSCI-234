from datetime import datetime as date

from utils import add_class, remove_class

wordsInput = Element("input")
logTemplate = Element("log-template").select(".log", from_content=True)
logList = Element("log-list")

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

logs = []

def showResult(function):
    currentTime = date.now()
    hourMinute = currentTime.strftime("%H:%M:%S")
    global wordsInput

    if not function:
        return None
    
    logID = f"task-{len(logs)}"
    outcome = {
        "id": logID,
        "content": function,
        "time": hourMinute,
        "input": wordsInput
    }

    logs.append(outcome)    

    logHTML = logTemplate.clone(logID)
    logOutcomeHTML = logHTML.select(".outcome")
    logTimeHTML = logHTML.select(".time")
    logInputHTML = logHTML.select(".input")
    logOutcomeHTML.element.innerText = outcome["content"]
    logTimeHTML.element.innerText = outcome["time"]
    logList.element.insertBefore(logHTML.element, logList.element.firstChild)

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