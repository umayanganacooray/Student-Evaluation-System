from isValidCenter import printPattern,getHelp
from StudentHandler import add_student,modify_student,remove_student,help_student
from SubjectHandler import add_subject,modify_subject,remove_subject,show_subject
from MarkHandler import handleAddMark,handleModifyMark,handleRemoveMark,handleShowMark,showAllMarks,showAllStudents

printPattern("Welcome to Smart student evaluation System")

commandList=("add_student","modify_student","remove_student","help_student",
             "add_subject","modify_subject","remove_subject","show_subject",
             "add_mark","modify_mark","remove_mark","show_mark","show_all_marks","show_all_students",
             "help","exit")

while (True):
    
    userData=input()
    userInput=userData.split(" ")

    if (len(userInput)==0):
        print("Invalid syntax press ‘help –‘ to check valid command list")

    elif userInput[0] in commandList:
        if userInput[0]== "add_student":
            add_student(userInput)
        elif userInput[0]== "modify_student":
            modify_student(userInput)
        elif userInput[0]== "remove_student":
            remove_student(userInput)
        elif userInput[0]== "help_student":
            help_student(userInput)
            

        elif userInput[0]== "add_subject":
            add_subject(userInput)
        elif userInput[0]== "modify_subject":
            modify_subject(userInput)
        elif userInput[0]== "remove_subject":
            remove_subject(userInput)
        elif userInput[0]== "show_subject":
            show_subject(userInput)
        
        elif userInput[0]== "add_mark":
            handleAddMark(userInput)
        elif userInput[0]== "modify_mark":
            handleModifyMark(userInput)
        elif userInput[0]== "remove_mark":
            handleRemoveMark(userInput)
        elif userInput[0]== "show_mark":
            handleShowMark(userInput)
        elif userInput[0]== "show_all_marks":
            showAllMarks(userInput)
        elif userInput[0]== "show_all_students":
            showAllStudents(userInput)

        elif userInput[0]== "help":
            getHelp()
        elif userInput[0]== "exit":
            printPattern("Good Bye!!! Have a nice day")
            break
            
    else:
        print("Invalid syntax press 'help-' to check valid command list")
