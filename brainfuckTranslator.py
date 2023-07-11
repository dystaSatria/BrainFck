def translate_to_brainfuck(input_text):
    brainfuck_code = ""
    for char in input_text:
        ascii_value = ord(char)
        brainfuck_code += "+" * ascii_value + ".>"

    return brainfuck_code

while True:
    user_input = input("Input your text for translates to Brainfuck Language (Input 'Exit' for end the program): ")

    if user_input.lower() == "exit":
        break

    brainfuck_program = translate_to_brainfuck(user_input)

    print("Result as Brainf#ck Languange :")
    print(brainfuck_program)
