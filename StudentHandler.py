from StudentDataCenter import addStudent,modifyStudent,removeStudent,getStudentById,getStudentByName

studentEntities=[]
studentIncrement = 0

def isValidName(studentName):
    "Check the name and return student name if it is in correct way "
    isStudentName = False
    if studentName.isalpha():
        isStudentName = True   
    elif studentName.isalnum():
        print("Student name should not have numbers included")
    else:
        print("Invalid syntax press 'help-' to check valid command list")
    return isStudentName ;

def checkDOBFormat(DOB):
    "Check whether the is in DD/MM/YYYY format."
    if (len(DOB)==10):
        if (DOB[2]=="/" and DOB[5]=="/"):
            charList=[DOB[0],DOB[1],DOB[3],DOB[4],DOB[6],DOB[7],DOB[8],DOB[9]]
            for char in charList:
                if not(char.isdigit()):
                    print("DOB should match with DD/MM/YYYY format")
                    return False
            return True
        else:
            print("DOB should match with DD/MM/YYYY format")
    else:
        print("DOB should match with DD/MM/YYYY format")
            
def isLeapYear(year):
    "Check whether the a year is a leap year or not."
    if (year%400==0 or (year%100!=0 and year%4==0)):
        return True
    else:
        return False

def isValidDOB(DOB):
    "Check a DOB is a valid DOB"
    
    if(checkDOBFormat(DOB)==True):
       
        dayStr=DOB[0]+DOB[1]
        dayInt=int(dayStr)
        monthStr=DOB[3]+DOB[4]
        monthInt=int(monthStr)
        yearStr=DOB[6]+DOB[7]+DOB[8]+DOB[9]
        yearInt=int(yearStr)
        
        def isValidDaysifNotFeb(DOB):
            "Check the number of days in each month except February are correct."
            if (monthInt==1 or monthInt==3 or monthInt==5 or monthInt==7 or monthInt==8 or monthInt==10 or monthInt==12):
                if(dayInt>31):
                    print("This month can have maximum 31 days")
                    return False
                elif(dayInt==0):
                    print("A month cannot have a 0th day")
                    return False
                else:
                    return True
                
            elif(monthInt==4 or monthInt==6 or monthInt==9 or monthInt==11):
                if(dayInt>30):
                    print("This month can have maximum 30 days")
                    return False
                elif(dayInt==0):
                    print("A month cannot have a 0th day")
                    return False
                else:
                    return True

        if (isLeapYear(yearInt)==True):
            if(monthInt>12 or monthInt<=0):
                print("There are only 12 months for a year")
            elif(monthInt==2):
                if(dayInt>29):
                    print("This month can have maximum 29 days")
                elif(dayInt==0):
                    print("A month cannot have a 0th day")
                else:
                    return True
            elif(isValidDaysifNotFeb(DOB)==False):
                return False
            else:
                return True
            
        else:
            if(monthInt>12 or monthInt<=0):
                print("There are only 12 months for a year")
            elif(monthInt==2):
                if(dayInt>28):
                    print("This month can have maximum 28 days")
                elif(dayInt==0):
                    print("A month cannot have a 0th day")
                else:
                    return True
            elif(isValidDaysifNotFeb(DOB)==False):
                return False
            else:
                return True

    else:
        return False


def add_student (userInput):
    "Add student to the system"

    if(len(userInput)>3)and(userInput[1].isalnum() and userInput[-2].isalnum()):
        print("Student name should have no white space")

    elif len(userInput)!=3:
        print("Invalid syntax press 'help-' to check valid command")
    
    else:
        if isValidName(userInput[1])and isValidDOB(userInput[2]):
            global studentIncrement
            studentIncrement += 1
            studIdStr="ST%03d" % studentIncrement  
            addStudent(studIdStr,userInput[1],userInput[2])
            print("Student was successfuly added to the system.Student Id is",studIdStr)

    return

        

def modify_student (userInput):
    "Modify student in the system"

    if(len(userInput)>4)and(userInput[2].isalpha() and userInput[-2].isalpha()):
        print("Student name should have no white space")

    elif len(userInput)!=4:
        print("Invalid syntax press 'help-' to check valid command list")
        
    else:
        if(isValidName(userInput[2])and isValidDOB(userInput[3])):
            selectedstudentDict=getStudentById(userInput[1])
            if selectedstudentDict==None:
                print("Invalid student Id")
            else:
                modifyStudent(userInput[1],userInput[2],userInput[3])
                print("Successfully modified")
 
    return


def remove_student (userInput):
    "Remove student in the system"
    if len(userInput)!=2:
        print("Invalid syntax press 'help-' to check valid command list") 
    else:
        selectedstudentDict=getStudentById(userInput[1])
        if selectedstudentDict==None:
            print("Student with "+userInput[1]+" does not exist")
        else:
            from MarkHandler import studentSubjectRelations
            canRemove=True
            for dictStud in studentSubjectRelations:
                if (dictStud["studentId"])==(userInput[1]):
                    print("Can not be deleted. Student has scores stored in the system")
                    canRemove=False
                    break
            if (canRemove):
                removeStudent(userInput[1])
                print("Student was successfuly removed")

    return


def help_student (userInput):
    "Help student in the system"
    if len(userInput)!=2:
        print("Invalid syntax press 'help-' to check valid command list") 
    else:
        studList=getStudentById(userInput[1])
        if(studList)== None:
            print("Student with "+userInput[1]+" does not exist")
        else:
            print("Student details :")
            print("\tName : "+studList["name"])
            print("\tDOB  : "+studList["dob"])
    return
