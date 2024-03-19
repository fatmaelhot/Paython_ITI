def read_file(pathOfFile, gradeForSuccess):
    try:
        with open(pathOfFile, "r") as file:
            lines = file.readlines()
        
        dataForStudents = {}
        total_grades = 0
        failedStudents = []

        for line in lines:
            data = line.strip().split()
            if len(data) >= 2:  
                name = data[0]
                grade = int(data[1])
                dataForStudents[name] = grade
                total_grades += grade 
                if grade < gradeForSuccess:
                    failedStudents.append(name)
            else:
                print("Skipping invalid line:", line)

        average_grade = total_grades / len(dataForStudents)  

        return dataForStudents, failedStudents, average_grade
    
    except FileNotFoundError:
        print("File not Found")
        return None, None, None


pathOfFile = 'students.txt'
dataForStudents, failedStudents, average_grade = read_file(pathOfFile, 60)

if dataForStudents is not None:
    print("Student Data:")
    for student, grade in dataForStudents.items():
        print(student, ":", grade)

    print("Failed Students:")
    for student in failedStudents:
        print(student)

    print("Average Grade:", average_grade)
