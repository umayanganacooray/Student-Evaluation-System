from StudentHandler import isValidName
from StudentDataCenter import getStudentByName,getStudentById,studentEntities
from SubjectDataCenter import getSubjectBySubjectName,getSubjectById,subjectEntities
from StudentSubjectRelation import studentSubjectRelations,addStudentSubjectRelation,modifyStudentSubjectRelation,deleteStudentSubjectRelation,getRelationshipsBySubjectId,getRelationshipsByStudentId

#print(studentEntities)

def isValidMark(mark):
    if mark.lstrip("-").isdigit():
        if (int(mark)<0):
            print("Student mark should be greater than zero")
        elif (int(mark)>100):
            print("Student mark should be less or equal to 100")
        else:
            return True
    elif (not(mark.isdigit())):
        print("Student mark should be a number")
    else:
        return True;

def isValidId(Id):
    if (len(Id)>=2): 
        letterIdStr=Id[0]+Id[1]
        if (not(letterIdStr=="ST" or letterIdStr=="TC" or letterIdStr=="SB" or letterIdStr=="CR" or letterIdStr=="MK")):
            return False
        elif (not(len(Id)>=5)):
            print("Id should be "+letterIdStr+"001 format")
        else:
            numberIdStr=""
            for i in range((len(Id))-2):
                numberIdStr+=Id[i+2]
            return True
    else:
        return False

def isAddedStudent(studentId):
    for student in studentEntities:
        if(student["id"]==studentId):
            return True
    return False

def isAddedSubject(subjectId):
    for subject in subjectEntities:
        if(subject["id"]==subjectId):
            return True
    return False
        
nameSubjectMarkList=[]
incrementVal3 = {'value': 0}

def handleAddMark(userInput):

    def increment(incrementVal3):
        incrementVal3["value"] += 1
        return "MK%03d" % incrementVal3["value"];
    
    if (not(len(userInput)==4)):
        print("Invalid syntax press 'help-' to check valid command list")
        
    elif ((not(isValidId(userInput[1])) and isValidMark(userInput[3]))):
        print("Invalid syntax press 'help-' to check valid command list")
        
    elif (not(isAddedStudent(userInput[1]))):
        print("Student with "+userInput[1]+" does not exist")
        
    elif (not(isAddedSubject(userInput[2]))):
        print("Subject with "+userInput[2]+" does not exist")
        
    else:
        isValidDict=True    
    
        for studentSubjectRelationsDict in studentSubjectRelations:
            if (studentSubjectRelationsDict["studentId"]==userInput[1] and studentSubjectRelationsDict["subjectId"]==userInput[2]):
                print("This student has marks for this subject already")
                isValidDict=False
                break
                        
        if isValidDict:
            stuSubRelationIncrementer=increment(incrementVal3)
            addStudentSubjectRelation(stuSubRelationIncrementer, userInput[1],userInput[2], userInput[3])
            print("Mark is succesfully added")

def handleModifyMark(userInput):
    if (not(len(userInput)==6)):
        print("Invalid syntax press 'help-' to check valid command list")
        
    elif (isValidMark(userInput[5])):
        if (not(isAddedStudent(userInput[1]))):
            print("Student with "+userInput[1]+" does not exist")
        elif (not(isAddedStudent(userInput[3]))) :
            print("Student with "+userInput[3]+" does not exist")
        elif (not(isAddedSubject(userInput[2]))):
            print("Subject with "+userInput[2]+" does not exist")
        elif (not(isAddedSubject(userInput[4]))):
            print("Subject with "+userInput[4]+" does not exist")
        else:
            isHasMark=False
            for studentSubjectRelationsDict in studentSubjectRelations:
                                
                if ((studentSubjectRelationsDict["studentId"]==userInput[1]) and (studentSubjectRelationsDict["subjectId"]==userInput[2])):
                    isHasMark=True
                    idNo=studentSubjectRelationsDict["id"]
                    modifyStudentSubjectRelation(idNo, userInput[2], userInput[4],userInput[5])
                            
                    print("Mark is succesfully modified")
                            
                    if (not isHasMark):
                         print("This student has no marks for this subject yet")


def handleRemoveMark(userInput):
    
    if (not(len(userInput)==3)):
        print("Invalid syntax press 'help-' to check valid command list")
    elif (isValidId(userInput[1])):
        if (not(isAddedStudent(userInput[1]))):
            print("Student with "+userInput[1]+" does not exist")
        elif (not(isAddedSubject(userInput[2]))):
            print("Subject with "+userInput[2]+" does not exist")
        else:
            isHasMark=False
            for studentSubjectRelationsDict in studentSubjectRelations:
                if((studentSubjectRelationsDict["studentId"]==userInput[1]) and (studentSubjectRelationsDict["subjectId"]==userInput[2])):
                    isHasMark=True
                    idNo=studentSubjectRelationsDict["id"]
                    deleteStudentSubjectRelation(idNo)
                    print("Mark is successfully removed")

            if (not isHasMark):
                print("This student has no marks for this subject yet")


def handleShowMark(userInput):

    if (not(len(userInput)==3)):
        print("Invalid syntax press 'help-' to check valid command list")
    elif (not(isAddedStudent(userInput[1]))):
        print("Student with "+userInput[1]+" does not exist")
    elif (not(isAddedSubject(userInput[2]))):
        print("Subject with "+userInput[2]+" does not exist")
    else:
        isHasMark=False
        for studentSubjectRelationsDict in studentSubjectRelations:
            if ((studentSubjectRelationsDict["studentId"]==userInput[1]) and (studentSubjectRelationsDict["subjectId"]==userInput[2])):
                print("\tName    : ",getStudentById(userInput[1])["name"])
                print("\tSubject : ",getSubjectById(userInput[2])["name"])
                print("\tMark    : ",studentSubjectRelationsDict["score"])
                isHasMark=True
                            
        if (not isHasMark):
            print("This student has no marks for this subject yet")

  

def showAllMarks(userInput):
    if (not(len(userInput)==2)):
        print("Invalid syntax press 'help-' to check valid command list")
    elif (not(isAddedStudent(userInput[1]))):
        print("Student with "+userInput[1]+" does not exist")
    elif (not(len(subjectEntities)!=0)):
        print("No marks to show")
    else:
        finalList=getRelationshipsByStudentId(userInput[1])
        finalSubjectIdList=[]
        finalSubjectList=[]
        for finalDict in finalList:
            finalSubjectIdList.append(finalDict["subjectId"])
        for subId in finalSubjectIdList:
            finalSubjectList.append(getSubjectById(subId))
        finalMarkList=[]
        
        lenSubList=[]
        for subName in finalSubjectList:
            lenSubList.append(len(subName))
        maxLength=max(lenSubList)
        if(maxLength<7):
            maxLength=7

        finalLength=maxLength+11
        print("\nList of Marks for each Subject :")
        print("Student Name : "+getStudentById(userInput[1])["name"]+"\n")
        print("="*finalLength)
        print("|"+"Subject".center(maxLength+2," ")+"|"+"Mark".center(6," ")+"|")
        print("="*finalLength)
                    
        for studentSubjectRelationsDict in studentSubjectRelations:
            if (studentSubjectRelationsDict["studentId"]==userInput[1]):
                subjectName=getSubjectById(studentSubjectRelationsDict["subjectId"])["name"]
                mark=studentSubjectRelationsDict["score"]
                print("|"+subjectName.center(maxLength+2," ")+"|"+mark.center(6," ")+"|")
        print("\n")

    
def showAllStudents(userInput):
    if (not(len(userInput)==2)):
        print("Invalid syntax press 'help-' to check valid command list")
        
    elif (not(isAddedSubject(userInput[1]))):
        print("Subject with "+userInput[1]+" does not exist")
        
    elif (not(len(subjectEntities)!=0)):
        print("No marks to show")
        
    else:
        finalList=getRelationshipsBySubjectId(userInput[1])
        finalStudentIdList=[]
        finalStudentList=[]
        for finalDict in finalList:
            finalStudentIdList.append(finalDict["studentId"])
        for studId in finalStudentIdList:
            finalStudentList.append(getStudentById(studId))
        finalMarkList=[]
        
        lenStudList=[]
        for studName in finalStudentList:
            lenStudList.append(len(studName))
        maxLength=max(lenStudList)
        if(maxLength<7):
            maxLength=7

        finalLength=maxLength+11
        print("\nList of Marks")
        print("Subject Name : "+getSubjectById(userInput[1])["name"]+"\n")
        print("="*finalLength)
        print("|"+"Name".center(maxLength+2," ")+"|"+"Mark".center(6," ")+"|")
        print("="*finalLength)
                    
        for studentSubjectRelationsDict in studentSubjectRelations:
            if (studentSubjectRelationsDict["subjectId"]==userInput[1]):
                studentName=getStudentById(studentSubjectRelationsDict["studentId"])["name"]
                mark=studentSubjectRelationsDict["score"]
                print("|"+studentName.center(maxLength+2," ")+"|"+mark.center(6," ")+"|")
        print("\n")
