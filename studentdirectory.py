students =  [{ "name": "Connor", "age": 20, "email": "connor@mail.com", "language": ["Python", "JavaScript"],"mentor":"John" },
 { "name": "James", "age": 22, "email": "james@mail.com","language": ["Python", "C++"],"mentor":"John" },
 { "name": "Mary", "age": 21, "email": "mary@mail.com", "language": ["Python","JavaScript"],"mentor":"Jill" },
 {"name": "Patrick", "age": 19, "email": "Patrick@mail.com", "language": ["C++","JavaScript"],"mentor":"Jill" },
 {"name": "Jenny", "age": 23, "email": "jenny@mail.com", "language": ["Java","C#"],"mentor":"Jill" }]


def youngest():
    count=0
    young=100
    for i in range(1,len(students)+1):
        if students[count]["age"]<young:
            
            young=students[count]["age"]
        count=count+1
    count=0
    print(young)
    for i in students:
        if young ==students[count]["age"]:
            return students[count]["name"]
        count=count+1

print(youngest())

def get_email():
    emailList=students[0]["email"],students[1]["email"],students[2]["email"],students[3]["email"],students[4]["email"]
    return emailList

print(get_email())    



def get_students_by_programming_languages(Languages):
    count=0
    studentlist=[]
    for i in students:
        studentLanguages=students[count]["language"]
        if Languages.lower() in [x.lower() for x in studentLanguages]:
            studentlist.append(students[count]["name"])
        count=count+1

    return studentlist


languages=input("Enter Coding Language: ")
print(get_students_by_programming_languages(languages))




