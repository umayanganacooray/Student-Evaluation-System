from SubjectDataCenter import getSubjectBySubjectName,getSubjectById,deleteSubject,modifySubject,addSubject

subjectList=[]
incrementVal2={'value': 0}

def isValidStream(stream):
    
    if (stream=="O/L") or (stream=="A/L"):
        return True;
    else:
        print("Stream should be either A/L or O/L")
        return False;
    
def isValidSubjectName(subjectName):
    
    isValid=False

    if subjectName.isalpha():
        isValid=True
    elif subjectName.isalnum():
        print("Subject name should not have numbers included")
    else:
        print("Invalid syntax press ‘help –‘ to check valid command list")
    return isValid;

def add_subject(userInput):

    def increment(incrementVal2):
        incrementVal2["value"] += 1
        return incrementVal2["value"];

    if len(userInput)==3:
        
        if (isValidSubjectName(userInput[1]) and isValidStream(userInput[2])):
            
            if (userInput[1] not in subjectList):
                subjectList.append(userInput[1])  
                subjectIncrementer=increment(incrementVal2)
                isSuccess=addSubject(subjectIncrementer,userInput[1],userInput[2])

                if (isSuccess):
                    print("Subject successfully added")

            else:
                print("Two subjects can not have same name")
                
    elif (len(userInput)>3 and (userInput[1].isalnum() and userInput[2].isalpha())):
            print("Subject name should have no white spaces")
      
    else:
        print("Invalid syntax press ‘help –‘ to check valid command list")
        
    return;

def modify_subject(userInput):

    if len(userInput)==4:
        
        if (isValidSubjectName(userInput[1]) and isValidSubjectName(userInput[2]) and isValidStream(userInput[3])):

            subList=getSubjectBySubjectName(userInput[1])
            
            if len(subList)==0 :
                print("Subject with "+userInput[1]+" does not exist")

            elif (not(userInput[1]==userInput[2])) and (userInput[2] in subjectList):
                    print("Subject with "+userInput[2]+" already exist")
                    print("Two subjects can not have same name")                
            else:
                from MarkHandler import nameSubjectMarkList
                for dictSub in nameSubjectMarkList:
                    if (dictSub["Subject"]==(userInput[1])):
                        dictSub["Subject"]=(userInput[2])
                subID=subList[0]["id"]
                isSuccess=modifySubject(subID, userInput[2], userInput[3])
                    
                subjectList.remove(userInput[1])
                subjectList.append(userInput[2])

                if (isSuccess):
                    print("Subject successfully modified")

    elif (len(userInput)>4 and (userInput[1].isalnum() and userInput[2].isalpha() and userInput[3].isalpha())):
         print("Subject name should have no white spaces")
         
    else:
        print("Invalid syntax press ‘help –‘ to check valid command list")
        
    return;


def remove_subject(userInput):
    
    if len(userInput)==2:
        
        if (isValidSubjectName(userInput[1])):

            subList=getSubjectBySubjectName(userInput[1])
            
            if len(subList)==0 :
                print("Subject with "+userInput[1]+" does not exist")
                
            else:
                from MarkHandler import nameSubjectMarkList
                canRemove=True
                for dictSub in nameSubjectMarkList:
                    if (dictSub["Subject"]==(userInput[1])):
                        print("Can not be deleted. Subject has scores stored in the system")
                        canRemove=False
                        break
                if (canRemove):
                    subID=subList[0]["id"]
                    isSuccess=deleteSubject(subID)
                   
                    subjectList.remove(userInput[1])
    
                    if (isSuccess):
                        print("Subject successfully removed")
                
    elif (len(userInput)>2 and (userInput[1].isalnum() and userInput[2].isalpha())):
        print("Subject name have should have no white spaces")
        
    else:
        print("Invalid syntax press ‘help –‘ to check valid command list")
        
    return;

def show_subject(userInput):

    isSuccess=False
    if len(userInput)==2:
        
        if isValidSubjectName(userInput[1]):

            subList=getSubjectBySubjectName(userInput[1])
            if len(subList)==0 :
                print("Subject with "+userInput[1]+" does not exist")
            else:
                print("Subject details :")
                print("\tSubject Name : "+subList[0]["subjectName"])
                print("\tStream       : "+subList[0]["stream"])

    elif (len(userInput)>2 and (userInput[1].isalnum() and userInput[2].isalpha())):
        print("Subject name have should have no white spaces")
        
    else:
        print("Invalid syntax press ‘help –‘ to check valid command list")
    

    return;
