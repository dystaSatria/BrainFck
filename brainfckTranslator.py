def translateBrainfck(inputText):
    brainfukCode = ""
    for char in inputText:
        asciiValue = ord(char)
        brainfukCode += "+" * asciiValue + ".>"

    return brainfukCode

while True:
    userInput = input("Input your text for translates to Brainfuck Language (Input 'Exit' for end the program): ")

    if userInput.lower() == "exit":
        break

    brainfckProgram = translateBrainfck(userInput)

    print("Result as Brainf#ck Languange :")
    print(brainfckProgram)
