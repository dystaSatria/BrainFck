program = input()  # Input the Brainfuck program

box = [0]
box_index = 0

ip = 0

loop_stack = []
loop_table = {}


for ip, instruction in enumerate(program):
    if instruction == "[":
        loop_stack.append(ip)
    elif instruction == "]":
        loop_start_index = loop_stack.pop()
        loop_table[loop_start_index] = ip
        loop_table[ip] = loop_start_index



while ip < len(program):
    instruction = program[ip]

    if instruction == "+":
        box[box_index] = (box[box_index] + 1) % 256  # Increment current cell value, wrap around if necessary

    elif instruction == "-":
        box[box_index] = (box[box_index] - 1) % 256  # Decrement current cell value, wrap around if necessary

    elif instruction == "<":
        box_index -= 1  

    elif instruction == ">":
        box_index += 1  
        if box_index == len(box):
            box.append(0)  

    elif instruction == ".":
        print(chr(box[box_index]), end="")  

    elif instruction == ",":
        box[box_index] = ord(input())  

    elif instruction == "[":
        if box[box_index] == 0:
            ip = loop_table[ip]  

    elif instruction == "]":
        if box[box_index] != 0:
            ip = loop_table[ip]  

    ip += 1  

