#Jacob Breault
#6/27/2021
#Module 6.2 Assignment

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

#Update statement; changes Thorin's last name (1007) to Johnson Jr.
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Johnson Jr."}})

#find the new student doc.
updatedStudent = students.find_one({"student_id": "1007"})

#second display statement.
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

#Output updated student (1007).
print("  Student ID: " + updatedStudent["student_id"] + "\n  First Name: " + updatedStudent["first_name"] + "\n  Last Name: " + updatedStudent["last_name"] + "\n")

#End or program.
input("\n\n  End of program, press any key to continue...")
