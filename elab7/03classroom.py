class ClassRoom:
    def __init__(self, grade=0, homeRoomTeacher="", studentList=[], numStudents=0):
        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.studentList = studentList
        self.numStudents = numStudents

    def get_grade(self):
        return self.grade
    def set_grade(self,grade):
        self.grade = grade

    def get_homeroom_teacher(self):
        return self.homeRoomTeacher
    def set_homeroom_teacher(self, homeRoomTeacher):
        self.homeRoomTeacher = homeRoomTeacher
    
    def get_student_list(self): 
        return self.studentList
    def set_student_list(self, studentList):
        self.studentList = studentList
        
    def get_num_student(self):
        return self.numStudents
    def set_num_student(self, numStudents):
        self.numStudents = numStudents

    def get_student_no(self, n):
        return self.studentList[n-1]
    
    def add_student(self, student_name):
        if self.numStudents < 10:
            self.studentList.append(student_name)
            self.numStudents += 1
            return True
        else:
            return False
        
    def change_student(self, n, new_name):
        if 0 <= n < self.numStudents:
            self.studentList[n-1] = new_name
            return True
        else:
            return False
        
    def remove_student(self, student_name):
        i = 1
        while i <= self.numStudents and self.studentList[i] != student_name:
            if self.studentList[i] == student_name:
                self.studentList.remove(student_name)
                self.numStudents -= 1
                return True
            i += 1
        return False

    def remove_student_no(self, n):
        if 0 < n < self.numStudents:
            self.studentList.pop(n)
            return True
        else:
            return False

    def __str__(self):
        students = ",".join(self.studentList)
        return f"Grade: {self.grade} + '\n' + Homeroom Teacher: {self.homeRoomTeacher} + '\n' + Students {students}"