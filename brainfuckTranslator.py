def translateBrainfuck(input_text):
    brainfuckCode = ""
    for char in input_text:
        ascii_value = ord(char)
        brainfuckCode += "+" * ascii_value + ".>"

    return brainfuckCode

while True:
    userInput = input("Input your text for translates to Brainfuck Language (Input 'Exit' for end the program): ")

    if userInput.lower() == "exit":
        break

    brainfuck_program = translateBrainfuck(userInput)

    print("Result as Brainf#ck Languange :")
    print(brainfuck_program)
