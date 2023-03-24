program = input()

box = [0]
box_index= 0

ip = 0

while ip < len(program):
    instruction = program[ip] 
    # + mean is increase 1 step
    if instruction == "+":
        box[box_index] += 1
        if box[box_index] == 256 :
            box_index = 0

    # - mean is decrease 1 step
    elif instruction == "-":
        box[box_index] -= 1
        if box[box_index] == -1 :
            box_index = 256

    # s mean is square the step
    elif instruction =="<":
        box_index -= 1

    elif instruction == ">":
        box_index += 1
        if box_index == len(box):
            box.append(0)

    elif instruction == ".":
        print(chr(box[box_index]),end="")# this is print about character variable type



