from school import School
from config import Configure
import numpy as np


class Faculty(School, Configure):

    fac = 'Communication Information Science'
    dept = 'Computer-Science'
    course = ['MAT112', 'CSC112', 'CSC114']

    def __init__(self, sch_type=School.s_type, sch_name=School.name, sch_addr=School.addr, sch_motto=School.motto, faculty=fac, department=dept, 
                 course:list=course, level=400) -> None:
        super().__init__(sch_type, sch_name, sch_addr, sch_motto)
        self.fac = faculty 
        self.dept = department
        self.course = course 
        self.level = level
        self.gpa = 0
        
    def add_stud_course(self, student, database) -> None:
        super.connect_database()
        if student in database:
            pass
        
        else:
            return f"{student} doesn't exit in the database"


        '''
        Each student will be able to select courses 
        from his or her Faculty/Departmental/Borrow-course 
        from a list of COURSES
        '''
        pass
    
    def selected_courses(self) -> list:
        
        '''
        All Courses offered by an individual student would be selected 
        and added to their portal
        '''
        pass

    #This is method for an add and drop course for individual student in a particular session
    def add_course(self, sub_course) -> None:
        if sub_course.upper() in self.course:
            self.course
            return f'{sub_course} is already on your course list.'
        else:
            self.course.append(sub_course.upper())
            return f'{sub_course.upper()} was Added to your course list.'

    '''
        Another way to remove a particular course in a list of courses.
        index = self.course.index(del_course.upper())
        self.course.upper().pop(index)
    '''
    
    #This is method for an add and drop course for individual student in a particular session
    def drop_course(self, del_course) -> None:
        del_course = del_course.upper()
        if del_course in self.course:
            self.course.upper().remove(del_course)
            return f'Course {del_course} has been dropped'
<<<<<<< HEAD
=======
        
            '''
            Another way to remove a particular course in a list of Student Courses.
            
            index = self.course.index(del_course.upper())
            self.course.upper().pop(index)
            '''
>>>>>>> 2375ddf984b0b864539ade3c87da8b951c07bad3
            
        else:
            return f'{del_course} doesn\'t exit in the List of Courses you want to remove'

    def get_courses(self) -> None:
        return self.course
    
    def calculate_gpa(self, s_name = 'AbdulMumin') -> None:

        '''
        Before Student would be able to calculate his or her gpa, the student must be in the Database
        
        Use Flag for Testing then improve when there's a database inplace
        '''
        
        flag = True
        
        if flag == True:
            self.score_point= 0
            self.total = 0
            self.total_unit = 0
            
            # get the student details: Scores and unit.
            for i in np.arange(len(self.course)):
                print(f'Course: {self.course[i]}')
                self.score = int(input(f"Enter the SCORE for \"{self.course[i]}\" -> "))
                if (self.score >= 70) & (self.score <=100):
                    self.score_point = 5
                
                elif (self.score >= 60) & (self.score <=69):
                    self.score_point = 4
                    
                elif (self.score >= 50) & (self.score <= 59):
                    self.score_point = 3
                    
                elif (self.score >= 45) & (self.score <= 49):
                    self.score_point = 2
                    
                else:
                    self.score_point = 0
                    
                self.unit_course = int(input(f"Enter the unit course for \"{self.course[i]}\" -> "))
                print()
                self.total += self.unit_course * self.score_point
                self.total_unit += self.unit_course
        print(f'Total points Earned: \"{self.total}\" \nTotal unit course: "{self.total_unit}"')
        self.gpa = round((self.total / self.total_unit), 2)
            
    def show_gpa(self) -> None:
        return f'Your CGPA is: {self.gpa}'
    
    def show_remark(self, name='AbdulMumin') -> None:
        if (self.gpa >= 4.50) & (self.gpa <= 5.0):
            return f'Hello {name}, Your remark is: First Class with {self.gpa} points'
        
        elif (self.gpa >= 3.50) & (self.gpa <= 4.49):
            return f'Hello {name}, Your remark is: Second Class Upper with {self.gpa} points'
            
        elif (self.gpa >= 2.50) & (self.gpa <= 3.49):
            return f'Hello {name}, Your remark is: Second Class Lower with {self.gpa} points'    
        
        else:
            return f'Hello {name}, Your remark is: Third Class with {self.gpa} points'
    
    def add_student(self):

        '''
        Check through the database if the Student exist, 
        If True:
            return "Student exit"
        Else:
            return "add student to the database"
        '''
        pass
    
    def del_student(self):
        
        '''
        Check through the database if the Student exist, 
        If True:
            return "Remove/Delete Student from the School Database" 
        Else:
            return "The Studdent you want to remove doesn't exit"
        '''
        pass

    def update_session(self):

        '''
        This feature can still be removed later if no effect

        Check through the database if an existing Student session has been updated,

        If True:
            return "Student session already been updated" 
        Else:
            return "Update the Studdent session for the YEAR."
        '''
        pass

    def display_info(self) -> None:
        print('THE FACULTY CLASS IS BEING INVOKED!.\n\n')
        super().display_info()
        print(f'Your Department is: "{self.dept}"')
        if self.gpa == 0:
            print(f'Your grade is low, you are not on a good standing. Check back later')
        else:
            print(f'Your GPA is: "{self.gpa}"')
            
        if self.level < 100:
            return
         
        else:
            print(f'Your level is: "{self.level}"')
