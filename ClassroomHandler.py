from ClassroomDataCenter import addClassroom,modifyClassroom,removeClassroom,getClassroomById,getClassroomByName,getClassroomLocatiobById,canAddClassroom

classroomEntities=[]
classIncrement=0

def isValidClassName(className):
    "Check the class name is correct"
    isClassName=False
    if "-" not in className:
        print("Invalid class name")
    else:
        classnameList=className.split("-")
        if len(classnameList)==2:
            grade=classnameList[0]
            letter=classnameList[1]
            if grade.isdigit() and 13>=int(grade)>0:
                if len(letter)==1 and letter.isupper():
                    isClassName=True
                else:
                    print("The class letter is invalid")
            else:
                 print("Invalid grade.Please check the grade")
        else:
            print("Invalid class name")
    return isClassName

def isValidCapacity(capacity):
    "Check the classroom capacity is valid"
    isCapacity=False
    maxCapacity=30
    if int(capacity)>maxCapacity:
        print("The classroom capaciy is exceded")
    elif int(capacity)<0:
        print("The student capaciy should be a positive number")
    elif 0<int(capacity)<=maxCapacity:
        isCapacity=True
    else:
        print("Invalid capacity")
    return isCapacity
            
def isValidLocatin(location):
    isClassroomLocation=False
    for char in location:
        if char.isdigit():
            print("Classroom location should not be a number")
        elif char.isalnum():
            isClassroomLocation=True
        else:
            print("Invalid class location")
    return isClassroomLocation

def add_class_room(userInput):
    "Add a classroom to the system"
    locationStr=userInput[3:len(userInput)]
    if len(userInput)<=3:
        print("Invalid syntax press 'help-' to check valid command list")
    else:
        if isValidClassName(userInput[1]) and isValidCapacity(userInput[2]) and isValidLocatin(locationStr):
            canAdd=canAddClassroom(userInput[1],locationStr)
            if (canAdd==True):
                global classIncrement
                classIncrement += 1
                classidStr="CR%03d" % classIncrement
                addClassroom(classidStr,userInput[1],userInput[2],locationStr)
                print("Classroom was successfuly added to the system.Classroom Id is",classidStr)
    return
                 
def modify_class_room (userInput):
    "Modify classroom in the system"
    locationStr=userInput[4:len(userInput)]
    if len(userInput)<=4:
        print("Invalid syntax press 'help-' to check valid command list")
    else:
        if isValidClassName(userInput[2]) and isValidCapacity(userInput[3]) and isValidLocatin(locationStr):
            selectedclassroomDict=getClassroomById(userInput[1])
            if selectedclassroomDict==None:
                print("Invalid Classroom Id")

            canAdd=canAddClassroom(userInput[2],locationStr)
            if (canAdd==True):
                classId=userInput[1]
                modifyClassroom(classId,userInput[2],userInput[3],locationStr)
                print("Classroom is Successfully modified")

    return


def remove_class_room (userInput):
    "Remove classroom in the system"
    if len(userInput)!=2:
        print("Invalid syntax press 'help-' to check valid command list")
    else:
        selectedclassroomDict=getClassroomById(userInput[1])
        if selectedclassroomDict==None:
            print("Classroom with "+str(userInput[1])+" does not exist")
        else:
            removeClassroom(userInput[1])
            print("Classroom is successfuly removed") 
    return


def help_class_room (userInput):
    "Help classroom in the system"
    if len(userInput)!=2:
        print("Invalid syntax press 'help-' to check valid command list") 
    else:
        selectedclassroomDict=getClassroomById(userInput[1])
        if selectedclassroomDict==None :
            print("Classroom with "+userInput[1]+" does not exist")
        else:
            print("classroom details :")
            print("\tName : "+selectedclassroomDict["name"])
            print("\tCapacity : "+selectedclassroomDict["capacity"])
            classLocationList=selectedclassroomDict["location"]
            classLocation=" ".join(classLocationList)
            print("\tLocation: "+classLocation)
    return
