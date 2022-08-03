class School_t:

    def __init__(self, sch_type):
        self.type = sch_type

class School(School_t):
    '''
    Documentation:
    
        Creating class_variables
        Params used: 
            -> School type
            -> School name
            -> School Address, Where it was suited
            -> School Motto
            -> Faculty, Department
            -> Courses (List): this should allow user to add or remove course for a certain semester or session. 
            -> Grade: It collect a string attributes.
    '''
    
    # Class Variables
    
    s_type = 'University'
    name = 'University of Ilorin'
    addr = 'Ilorin, Kwara-state'
    motto = 'Better by Far'
    fac = 'Communication I information Science'
    dept = 'Computer-Science'
    course = ['MAT112', 'CSC112', 'CSC114']
    grade = 'A'
    
    def __init__(self, sch_type=s_type, sch_name=name, sch_addr=addr, sch_motto=motto):
        super().__init__(sch_type)
        
        # Instance Variables
        self.name = sch_name
        self.addr = sch_addr
        self.motto = sch_motto
            
    def display_info(self) -> None:
        print(f'The type of the School choosing is {self.type}')
        print(f'The name of the School is {self.name}')
        print(f'The address of the School is {self.addr}')
        print(f'The mootto of the School is {self.motto}')