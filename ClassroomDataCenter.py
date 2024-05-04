#here stores all the classroms
classroomEntities=[]

def addClassroom(id,name,capacity,location):
    "store the classroom inside the classromm data list. return True if operation is successful"
    #todo- check the a classroom with this id already exist in system. If so, return false
    #todo- check the a classroom with this classroom name already exist in system. If so, return false
    #todo- check the capacity is correct. If not, return false
    #return False;

    #add the new classroom
    newClassroom={}
    newClassroom["id"]=id
    newClassroom["name"]=name
    newClassroom["capacity"]=capacity
    newClassroom["location"]=location
    classroomEntities.append(newClassroom)
    print(classroomEntities)
    return True;

def modifyClassroom(id,name,capacity,location):
    "modify content of a already stored classroom. return True if operation is successful"
    #todo- check the a classroom with this id already exist in system. If not, return false
    #todo- check the capacity is correct. If not, return false
    #return False;

    for classroom in classroomEntities:
        if(classroom["id"]==id):
            selectedClass=classroom

    selectedClass["name"]= name
    selectedClass["capacity"]= capacity
    selectedClass["location"]= location
    print(classroomEntities)
    return True;

def removeClassroom(id):
    "remove a classroom from the system. return True if operation is successful"
    #todo- check the a classroom with this id already exist in system. If not, return false
    #return False;

    #choose the classroom
    for classroom in classroomEntities:
        if(classroom["id"]==id):
            selectedClass=classroom
    classroomEntities.remove(selectedClass)
    print(classroomEntities)
    return True;

def getClassroomById(id):
    "return the classroom that has given id. Otherwise return None"

    #choose the classroom
    for classroom in classroomEntities:
        if(classroom["id"]==id):
            return classroom.copy(); # give a copy of the dictionary as returned value.
    return None;
    #we can check this using if statement 'if ret_value is not None'

def getClassroomByName(name):
    "return the classroom that has given name. Otherwise return None"

    classroomEntityList=[]
    #choose the classroom
    for classroom in classroomEntities:
        if(classroom["name"]==name):
            classroomEntityList.append(classroom.copy())# give a copy of the dictionary as returned value.
    return classroomEntityList;
    #we can check this using if statement 'if ret_value is not None'

def getClassroomLocatiobById(id):
    "return the classroom location that has given id. Otherwise return None"

    #choose the classroom
    for classroom in classroomEntities:
        if(classroom["id"]==id):
            return classroom["location"]; # give a copy of the dictionary as returned value.
    return None;

def canAddClassroom(name,location):
    "if can add the classroom return ture"
    canAdd=True
    for dataDic in classroomEntities:
        if (dataDic["name"]==name):
            print("Tow class cannot have same name")
            canAdd=False
            break
        else:
            if (dataDic["location"]==location):
                print("Tow class cannot have same location")
                canAdd=False
                break
       
    return canAdd

