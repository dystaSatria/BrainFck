program = input()

box = [0]
box_index= 0

ip = 0

loop_stack =[]
loop_table = {}

for ip, instruction in enumerate(program):
    if instruction == "[":
        loop_stack.append(ip)
    

    elif instruction == "]":
        loop_startIndex = loop_stack.pop()
        loop_table[loop_startIndex] = ip
        loop_table[ip] = loop_startIndex


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

    elif instruction == ",":
        if input_user == []:
            input_user = list(input()+"\n")    
        box[box_index] = ord(input_user.pop(0))

    elif instruction == "[":
        if not box[box_index]:
            ip = loop_table[ip]
    
    elif instruction == "]":
        if box[box_index]:
            ip = loop_table[ip]

    
ip += 1




