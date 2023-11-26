##filename = input("Nom du Fichier : ")
filename="code.txt"

file = open(filename, "r")

LIST = []
REGISTER = {"PC":0, "R1":0, "R2":0, "R3":0, "R4":0, "R5":0, "R6":0, "R7":0, "R8":0, "R9":0, "R10":0, "R11":0, "R12":0, "R13":0, "R14":0, "R15":0}
RAM = {}

for line in file:
    line = line.replace(",", "")
    print(line)
    line_split = line.split(" ")
    temp_list = []
    for item in line_split:
        temp_list.append(item.strip())
    LIST.append(temp_list)

print(LIST)

for command in LIST:
    if command[0] == "MOV":
        if(command[2][0] == "#"):
            REGISTER[command[1]] = command[2].replace("#", "")
            print(REGISTER)
        else:
            if(RAM[command[2]] != ""):
    if command[0] == "ADD":
        None
    if command[0] == "STR":
        None
    if command[0] == "LDR":
        None