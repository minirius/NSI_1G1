import re

print("Welcome to OWL Compilator")
##filename = "code.owl"

##file = open(filename, "r")
CONTINUE_PROG = True

def getCommand(com):
    return com.split()

VARS = {}

while(CONTINUE_PROG):

    userInput = input(">> ")
    commandList = getCommand(userInput)

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

    elif commandList[0] == "IF":
        operator = commandList[2].strip()
        if(operator == "=="):
            print(commandList[1] == commandList[3])
        if(operator == ">"):
            print(commandList[1] == commandList[3])
        if(operator == "<"):
            print(commandList[1] == commandList[3])
        if(operator == "!="):
            print(commandList[1] == commandList[3])
        
    else:
        print("Bad Type Error")
