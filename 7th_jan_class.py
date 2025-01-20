students={
    1:{"name": "google", "age": 20},
    2:{"name": "deloite", "age": 22},
    3:{"name": "pwc", "age": 19},
    4:{"name": "aaa", "age": 21},
    5:{"name": "eee", "age": 23},


}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")

