#from isValidCenter import printPattern,getHelp
from ClassroomHandler import add_class_room,modify_class_room,remove_class_room,help_class_room


isTrue=True
while (isTrue):
    
    userData=input()
    userInput=userData.split(" ")
    print(userInput)

    if (len(userInput)==0):
        print("Invalid syntax press ‘help –‘ to check valid command list")

    elif userInput[0]== "add_class_room":
        add_class_room(userInput)
    elif userInput[0]== "modify_class_room":
        modify_class_room(userInput)
    elif userInput[0]== "remove_class_room":
        remove_class_room(userInput)
    elif userInput[0]== "help_class_room":
        help_class_room(userInput)
