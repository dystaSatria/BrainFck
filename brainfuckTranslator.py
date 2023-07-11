def translateBrainfuck(input_text):
    brainfuck_code = ""
    for char in input_text:
        ascii_value = ord(char)
        brainfuck_code += "+" * ascii_value + ".>"

    return brainfuck_code

while True:
    userInput = input("Input your text for translates to Brainfuck Language (Input 'Exit' for end the program): ")

    if userInput.lower() == "exit":
        break

    brainfuck_program = translateBrainfuck(userInput)

    print("Result as Brainf#ck Languange :")
    print(brainfuck_program)
