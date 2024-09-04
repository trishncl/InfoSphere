def lines():
    print("\t\t\t===================================================================")

num_students = int(input("\t\t\t\t\t  Enter the number of students: "))

students_info = []

for x in range(num_students):
    keys = {
        'Student Name' : str,
        'Age' : int,
        'School' : str,
        'Year Level' : str,
        'Student ID' : str,
        'GWA' : float
    }

    lines()
    info = {}
    for key, datatype in keys.items():
        value = input(f"                               Enter the {key}: ")
        info[key] = datatype(value)
    lines()
    
    students_info.append(info)
    
    lines()
    print("\n\t\t\t\t\t\tSTUDENT INFORMATION\n")
    print(f"\t\t\t\tName\t\t:\t {info['Student Name']}")
    print(f"\t\t\t\tAge\t\t:\t {info['Age']}")
    print(f"\t\t\t\tSchool\t\t:\t {info['School']}")
    print(f"\t\t\t\tYear Level\t:\t {info['Year Level']}")
    print(f"\t\t\t\tStudent ID\t:\t {info['Student ID']}")
    print(f"\t\t\t\tGWA\t\t:\t {info['GWA']}\n")
    lines()

for student in students_info:
    lines()
    print(f"\nCertificate of Recognition is hereby awarded to {student['Student Name']} for being named a CICS Dean's Lister for the 2nd Semester of AY 2023-2024!\n")
