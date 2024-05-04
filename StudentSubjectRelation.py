#here stores all the relationship between student and score
studentSubjectRelations=[]

def addStudentSubjectRelation(id, studentId, subjectId, score):
    #todo- check the a relationship with this id already exist in system. If so, return false
    #todo- check the id, studentId, subjectId already exist in system. If so, return false
    #return False;

    #add the new StudentSubjectRelation
    newStudentSubjectRelation={}
    newStudentSubjectRelation["id"]=id
    newStudentSubjectRelation["studentId"]=studentId
    newStudentSubjectRelation["subjectId"]=subjectId
    newStudentSubjectRelation["score"]=score
    studentSubjectRelations.append(newStudentSubjectRelation)
    return True;

def modifyStudentSubjectRelation(id, studentId, subjectId, score):
    #todo- check the a relationship with this id already exist in system. If not, return false
    #return False;

    #choose the StudentSubjectRelation
    for relationship in studentSubjectRelations:
        if(relationship["id"]==id):
            selectedRelationship=relationship
    selectedRelationship["studentId"]=studentId
    selectedRelationship["subjectId"]=subjectId
    selectedRelationship["score"]=score
    return True;

def deleteStudentSubjectRelation(id):
    "delete a Relationship from the system. return True if operation is successful"
    #todo- check the a relationship with this id already exist in system. If not, return false
    #return False;

    #choose the StudentSubjectRelation
    for relationship in studentSubjectRelations:
        if(relationship["id"]==id):
            selectedRelationship=relationship
    studentSubjectRelations.remove(selectedRelationship)
    return True;

def getRelationshipsBySubjectId(subjectId):
    "return the relationship list which has mentioned subjectId"

    selectedRelationships=[]
    for relationship in studentSubjectRelations:
        if(relationship["subjectId"]==subjectId):
            selectedRelationships.append(relationship.copy())
    return selectedRelationships;

def getRelationshipsByStudentId(studentId):
    "return the relationship list which has mentioned studentId"

    selectedRelationships=[]
    for relationship in studentSubjectRelations:
        if(relationship["studentId"]==studentId):
            selectedRelationships.append(relationship.copy())
    return selectedRelationships;
