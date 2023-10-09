import os
import sys

vars = {}

def add_variable(name, value):
    vars[name] = int(value)

def set_variable(name, value):
    vars[name] = int(value)

def get_variable(name):
    return vars[name]

if(len(sys.argv) < 2):
    print("Usage : python3 pasm.py <file>")

file_path = sys.argv[1]

if not os.path.exists(file_path) or not os.path.isfile(file_path):
    print("file not found : " + file_path)

code_file = open(file_path, 'r')

code_lines = code_file.readlines()

log = 0

if len(sys.argv) > 2:
    log = int(sys.argv[2])

current_line = 0

while True:
    code_line = code_lines[current_line].replace("\n","")
    code_line_split = code_line.split(" ")
    if len(code_line_split) >= 1:
        if len(code_line_split[0]) > 0:
            if code_line_split[0][0] != '#':
                if log > 0:
                    print(code_line_split)
                    print(vars)
                match code_line_split[0]:
                    case "var":
                        if len(code_line_split) == 3:
                            add_variable(code_line_split[1], int(code_line_split[2]))
                        else:
                            print("Syntax error line : " + str(current_line + 1))      
                    case "inc":
                        set_variable(code_line_split[1], get_variable(code_line_split[1]) + 1)
                    case "dec":
                        set_variable(code_line_split[1], get_variable(code_line_split[1]) - 1)
                    case "print":
                        if len(code_line_split) == 2:
                            print(get_variable(code_line_split[1]))
                        else:
                            print("Syntax error line : " + str(current_line + 1))   
                    case "jmp":
                        if len(code_line_split) == 2:
                            jmp_line = int(code_line_split[1]) - 2
                            if (jmp_line + 1) <= len(code_lines):
                                current_line = jmp_line
                            else:
                                print("Syntax error line : " + str(current_line + 1))   
                        else:
                            print("Syntax error line : " + str(current_line + 1))
                    case "tst":
                        if len(code_line_split) == 2:
                            jmp_line = current_line
                            if get_variable(code_line_split[1]) == 0:
                                jmp_line += 1 

                            if jmp_line <= len(code_lines):
                                current_line = jmp_line
                            else:
                                print("Syntax error line : " + str(current_line + 1))   
                        else:
                            print("Syntax error line : " + str(current_line + 1))
                    case "hlt":
                        print("Program exit") 
                        print(vars)
                        break 
    current_line += 1

# convert to Johny ram
johny = open(file_path + ".bij", "w")

current_line = 0

while True:
    code_line = code_lines[current_line].replace("\n","")
    code_line_split = code_line.split(" ")
    if len(code_line_split) >= 1:
        if len(code_line_split[0]) > 0:
            if code_line_split[0][0] != '#':
                match code_line_split[0]:    
                    case "inc":
                        johny.write("\n")
                    case "dec":
                        johny.write("\n")
                    case "jmp":
                        johny.write("\n")
                    case "tst":
                        johny.write("\n")
                    case "hlt":
                        johny.write("\n")
    current_line += 1

johny.close()