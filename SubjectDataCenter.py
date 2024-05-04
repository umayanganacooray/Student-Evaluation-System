subjectEntities=[]
id =1
def addSubject(id, subjectName, stream):
    "store the subject inside the subject data list. return True if operation is successful"

    newSubject={}
    newSubject["id"]=id
    newSubject["subjectName"]=subjectName
    newSubject["stream"]=stream
    subjectEntities.append(newSubject)
    id+=1
    return True;

def modifySubject(id, subjectName, stream):
    "modify content of a already stored subject. return True if operation is successful"

    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject

    selectedSubject["subjectName"]=subjectName
    selectedSubject["stream"]=stream
    return True;

def deleteSubject(id):
    "delete a subject from the system. return Tue if operation is successful"

    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject
    subjectEntities.remove(selectedSubject)
    return True;

def getSubjectById(id):
    "return the subjct that has given id. Otherwise return None"

    for subject in subjectEntities:
        if(subject["id"]==id):
            return subject.copy(); 

def getSubjectBySubjectName(subjectName):
    "return the subjct that has given id. Otherwise return None"

    subjectEntityList=[]
   
    for subject in subjectEntities:
        if(subject["subjectName"]==subjectName):
            subjectEntityList.append(subject.copy())
