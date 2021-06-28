#Jacob Breault
#6/27/2021
#Module 6.3 Assignment

from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.kseok.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

#get the list of students.
students = db.students

#find the students.
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
    


#Test student "Jimmy."
jimmy = { 
    "student_id": "1010",
    "first_name": "Jimmy",
    "last_name": "Johnson",
    "enrollments": [
        {
            "term": "Session 3",
            "gpa": "4.0",
            "start_date": "October 31, 2020",
            "end_date": "December 21, 2020",
            "courses": [
                {
                    "course_id": "ENG101",
                    "description": "Basic English Course",
                    "instructor": "Professor Jameson",
                    "grade": "A+"
                },
                {
                    "course_id": "MATH 201",
                    "description": "Introduction to Calculus",
                    "instructor": "Professor Smith",
                    "grade": "A+"
                }
            ]
        }
    ]
}


#Insert the test student to be deleted.
print("\n -- INSERT STATEMENTS --")
jimmy_student_id = students.insert_one(jimmy).inserted_id
print(" Inserted student record Jimmy Johnson into the students collection with document_id " + str(jimmy_student_id))

#Find the new inserted student.
newTestStudent = students.find_one({"student_id": "1010"})


#Display message.
print("\n --DISPLAYING STUDENT TEST DOC --")



#Output updated student with id 1010.
print("  Student ID: " + newTestStudent["student_id"] + "\n  First Name: " + newTestStudent["first_name"] + "\n  Last Name: " + newTestStudent["last_name"] + "\n")


#Delete the added student previously inserted.
result = students.delete_one({"student_id": "1010"})



# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

updated_list = students.find({})

# loop over the collection and output the results 
for document in updated_list:
    print("  Student ID: " + document["student_id"] + "\n  First Name: " + document["first_name"] + "\n  Last Name: " + document["last_name"] + "\n")
