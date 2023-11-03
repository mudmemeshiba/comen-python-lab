class Course:
    def __init__(self, title, course_id, credit):
        self.title = title
        self.course_id = course_id
        self.credit = credit

class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"
    
class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty
    def __str__(self):
        return f"{self.name} {self.faculty} ({self.id})"
    
class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if course.course_id not in self.courses:
            if self.total_credit + course.credit < 25:
                self.courses.append(course.course_id)
                self.total_credit += course.credit
                self.num_course += 1
                return True
            else:
                return False
        return False
    
    def drop_course(self, course):
        if course.course_id in self.courses:
            self.courses.remove(course.course_id)
            self.total_credit -= course.credit
            self.num_course -= 1
            return True
        else:
            return False
        
    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        nl = "\n"
        joinCourseID = ' '.join([i for i in self.courses])
        return f"Student ID: {self.id} {nl}Name: {self.firstname} {self.lastname} {nl}Major: {self.major} {nl}Advisor: {self.advisor} {nl}Courses: {joinCourseID}"

# ------------------------------------------
ske = Major('E17', 'Software & Knowledge Engineering', 'Engineering')
preeda = Teacher('Preeda', 'Lerdpongvipusana', 'E9019')
std1 = Student('5610546231', 'Chinnaporn', 'Soonue')
std1.set_advisor(preeda)
std1.set_major(ske)
print(std1)
oopi = Course('OOPI', '01219111', 3)
oopii = Course('OOPII', '01219113', 3)
isp = Course('Individual Software Development Process', '01219245', 3)
comorg = Course('Computer Organization & Architecture', '01219221', 3)
adt = Course('Abstract Data Types & Problem Solving', '01204212', 3)
commu = Course('Commu.Skills for Software & Knowledge Eng.', '01219213', 3)
labPhyI = Course('Laboratory in Physics I', '01420113', 1)
labPhyII = Course('Laboratory in Physics II', '01420114', 1)
phyI = Course('General Physics I', '01420111', 3)
phyII = Course('General Physics II', '01420112', 3)
print()
if not std1.add_course(oopi):
    print("Can't add course")
    print(f'Total Credit: {std1.total_credit}')
    print(std1)
    print()
if not std1.drop_course(oopi):
    print(f"Can't drop course. {oopi.course_id}")
# Drop non existing course
if not std1.drop_course(oopii):
    print(f"Can't drop course. {oopii.course_id}")
    print()
    print(std1)
    print(f'Total Credit: {std1.total_credit}')
    print()
# Credit more than 25
is_success = True
is_success = is_success and std1.add_course(oopi)
is_success = is_success and std1.add_course(oopii)
is_success = is_success and std1.add_course(isp)
is_success = is_success and std1.add_course(comorg)
is_success = is_success and std1.add_course(adt)
is_success = is_success and std1.add_course(commu)
is_success = is_success and std1.add_course(labPhyI)
is_success = is_success and std1.add_course(labPhyII)
is_success = is_success and std1.add_course(phyI)
is_success = is_success and std1.add_course(phyII)
if not is_success:
    print('Check credit more than 25: Can not add\n')
    print(std1)
    print(f'Total Credit: {std1.total_credit}')
    print(f'Type of advisor is Teacher {type(std1.advisor)}')
    print(f'Type of Major is Major: {type(std1.major)}')