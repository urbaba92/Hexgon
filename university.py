class Student:
    # Class Attribute (shared 
    # by all instances)
    university_name = "Global 
    University" def 
    __init__(self, name, 
    student_id, major):
        """ Instance Method: 
        Initialize instance 
        attributes. """ 
        self.name = name # 
        Instance Attribute 
        self.student_id = 
        student_id # Instance 
        Attribute self.major = 
        major # Instance 
        Attribute self.courses 
        = [] # Instance 
        Attribute (dynamic 
        list)
    # Instance Method
    def enroll(self, course): 
        """ Adds a course to 
        the student's list of 
        courses. """ 
        self.courses.append(course) 
        print(f"{self.name} has 
        enrolled in {course}.")
    # Class Method
    @classmethod def 
    change_university_name(cls, 
    new_name):
        """ Class Method: 
        Change the university's 
        name (class attribute). 
        """ cls.university_name 
        = new_name 
        print(f"University name 
        updated to 
        {cls.university_name}.")
    # Static Method
    @staticmethod def 
    calculate_gpa(grades):
        """ Static Method: 
        Calculate GPA given a 
        list of grades. """ if 
        not grades:
            return 0 return 
        sum(grades) / 
        len(grades)
    # Instance Method
    def get_details(self): """ 
        Returns student details 
        as a formatted string. 
        """ return (f"Name: 
        {self.name}, ID: 
        {self.student_id}, 
        Major: {self.major}, "
                f"University: 
                {self.university_name}, 
                Courses: 
                {self.courses}")
# Creating an Instance (Object)
student1 = Student("Alice", 
1001, "Computer Science")
# Accessing Instance Attributes
print(student1.name) # Output: 
Alice 
print(student1.student_id) # 
Output: 1001 
print(student1.major) # Output: 
Computer Science
# Accessing Class Attribute
print(Student.university_name) 
# Output: Global University
print(student1.university_name) 
# Output: Global University 
(shared by all)
# Using Instance Method
student1.enroll("Math") # 
Output: Alice has enrolled in 
Math. 
student1.enroll("Physics") # 
Output: Alice has enrolled in 
Physics. 
print(student1.get_details())
# Output: Name: Alice, ID: 
# 1001, Major: Computer 
# Science, University: Global 
# University, Courses: ['Math', 
# 'Physics'] Using Class Method
Student.change_university_name("International 
University") 
print(Student.university_name) 
# Output: International 
University
# Using Static Method
grades = [85, 90, 78, 92] gpa = 
Student.calculate_gpa(grades) 
print(f"GPA: {gpa:.2f}") # 
Output: GPA: 86.25
# Another Instance
student2 = Student("Bob", 1002, 
"Mathematics") 
student2.enroll("Statistics") 
print(student2.get_details())
# Output: Name: Bob, ID: 1002, Major: Mathematics, University: International University, Courses: ['Statistics']
