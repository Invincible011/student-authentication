from school import School
import numpy as np

class Faculty(School):
    def __init__(self, sch_type=School.s_type, sch_name=School.name, sch_addr=School.addr, sch_motto=School.motto, faculy=School.fac, department=School.dept, 
                 course:list=School.course, grade=School.grade, level=400):
        super().__init__(sch_type, sch_name, sch_addr, sch_motto)
        self.fac = faculy
        self.dept = department
        self.course = course 
        self.level = level
        self.grade = grade
        self.gpa = 0
        
    # Create a "Add Course" Instance method
    def add_course(self, sub_course):
        if sub_course.upper() in self.course:
            self.course
            return f'{sub_course} is already on your course list.'
        else:
            self.course.append(sub_course)
            return f'{sub_course.upper()} was Added to your course list.'
 
    # Create a "Drop Course" Instance method
    def drop_course(self, del_course):
        del_course = del_course.uppeer()
        if del_course in self.course:
            self.course.upper().remove(del_course)
            return f'Course {del_course} has been dropped'
        
            '''
            Another way to remove a particular in a list.
            
            index = self.course.index(del_course.upper())
            self.course.upper().pop(index)'''
        else:
            return f'{del_course} doesn\'t exit in the List of Courses you want to remove'

    def get_courses(self):
        return self.course
    
    def calculate_gpa(self, name = 'AbdulMumin'):
        '''
        Before Student would be able to calculate his or her gpa, the student must be in the Database
        
        Use Flag for Testing then improve when there's a database inplace
        '''
        
        Flag = True
        
        if Flag == True:
            self.score_point= 0
            self.total = 0
            self.total_unit = 0
            
            # get the student details: Scores and unit
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
            
    def show_gpa(self):
        return f'Your CGPA is: {self.gpa}'
    
    def show_remark(self):
        if (self.gpa >= 4.50) & (self.gpa <= 5.0):
            return f'Hello {self.name}, Your remark: First Class with {self.gpa} points'
        
        elif (self.gpa >= 3.50) & (self.gpa <= 4.49):
            return f'Hello {self.name}, Your remark: Second Class Upper with {self.gpa} points'
            
        elif (self.gpa >= 2.50) & (self.gpa <= 3.49):
            return f'Hello {self.name}, Your remark: Second Class Lower with {self.gpa} points'    
        
        else:
            return f'Hello {self.name}, Your remark: Third Class with {self.gpa} points'
    
    def display_info(self):
        print('THE FACULTY CLASS IS BEING INVOKED!.\n\n')
        super().display_info()
        print(f'The name of the Department is {self.dept}')
        if self.gpa == 0:
            pass
        else:
            print(f'Your GPA is {self.gpa}')
            
        if self.level < 100:
            return 
        else:
            print(f'Your level is {self.level}')