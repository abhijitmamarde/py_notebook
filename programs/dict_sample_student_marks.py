'''
To get the students and the marks in three subjects and print topper, subject wise topper and the average of each

Input sample:
5
abhi jit, subject 1, 90, subject 2, 92, subject 3, 81
sachin K, subject 2, 91, subject 1, 86, subject 3, 82
varsha u, subject 3, 80, subject 1, 62, subject 2, 83
nilu p,   subject 3, 92, subject 2, 94, subject 1, 84
sunil p,  subject 2, 97, subject 1, 93, subject 3, 85

O/P:
Topper: abhi jit Total: 270/300, Avg: 250
subject 1 Topper: abhi jit Total: 99
subject 2 Topper: sachin K Total: 95
subject 3 Topper: nilu P Total: 93
'''

student_list = [
    {
        'student_name': "abhi jit",
        'marks': 
        {
            "maths": 98,
            "science": 82,
            "english": 81,
            "history": 89,
        }
    },
    {
        'student_name': "sachin k",
        'marks': 
        {
            "history": 84,
            "maths": 92,
            "science": 94,
            "english": 83,
            "bio": 90,
        }
    }
]

subjects = ["maths", "english", "science", "history", "bio"]

# subject_wise_topper = {
#     "maths": { 'student_name': "", 'marks': 0 },
#     "english": { 'student_name': "", 'marks': 0 },
#     "science": { 'student_name': "", 'marks': 0 },
#     "history": { 'student_name': "", 'marks': 0 },
# }

subject_wise_topper = {}
for subject in subjects:
    subject_wise_topper[subject] = { 'student_name': "", 'marks': 0 }

for student in student_list:
    for subject in subjects:
        if subject_wise_topper[subject]['marks'] < student['marks'].get(subject, 0):
            subject_wise_topper[subject]['student_name'] = student['student_name']
            subject_wise_topper[subject]['marks'] = student['marks'][subject]



print(subject_wise_topper)

input_str = "  abhi jit   , subject 1, 90, subject 2, 92, subject 3, 81"
input_data = input_str.split(",")
# print(input_data)
student_name, subjects_marks = input_data[0], input_data[1:]
print(student_name.strip())
print(subjects_marks)

print(",".join(subjects))
