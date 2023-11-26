##filename = input("Nom du Fichier : ")
filename="Chapitre 3/code.owl"

file = open(filename, "r")

LIST = []
def getCommand(com):
    return com.split()

VARS = {}

print(file)

jump = 0
jump_forward = True

for line in file:
    IR = 1
    if(int(jump) > 0):
        if(jump_forward):
            IR += 1
            continue
        else:
            IR -= 1
            continue
    commandList = getCommand(line)

    for i, case in enumerate(commandList):
        if i>0:
            if(commandList[i].startswith("#")):
                tempvar = commandList[i].replace("#", "");
                commandList[i] = VARS[tempvar]
                
            userInput += " "+str(commandList[i])
        else:
            userInput = commandList[i]

    if(commandList[0] == "EXIT"):
        CONTINUE_PROG = False
        continue
    elif commandList[0] == "SHOW":
        stackTemp = ""
        for i, item in enumerate(commandList):
            if(i>0): stackTemp += item+" "
        print(stackTemp)

    elif commandList[0] == "ASK":
        tempList = userInput.split(":")
        stackQuest = tempList[1].strip()
        returned = input(str(stackQuest)+" : ")
        VARS[commandList[1]] = returned
    elif commandList[0] == "SET":
        tempList = userInput.split(":")
        stackQuest = tempList[1].strip()
        VARS[commandList[1]] = stackQuest
    elif commandList[0] == "JUMP":
        line_number = int(userInput.split(" ")[1].strip())
        print("jumping line", line_number)
        jump = line_number
        if(int(jump) < int(IR)): jump_forward = False

    elif commandList[0] == "TEST":
        operator = commandList[3].strip()
        if(operator == "=="):
            VARS[commandList[1]] = commandList[2] == commandList[4]
        if(operator == ">"):
            VARS[commandList[1]] = commandList[2] > commandList[4]
        if(operator == "<"):
            VARS[commandList[1]] = commandList[2] < commandList[4]
        if(operator == "!="):
            VARS[commandList[1]] = commandList[2] != commandList[4]
        
    else:
        print("Bad Type Error")