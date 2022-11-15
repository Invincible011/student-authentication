class School_t:

    def __init__(self, sch_type):
        self.type = sch_type

class School(School_t):
    
    # Class variables
    s_type = 'University'
    name = 'University of Ilorin'
    addr = 'Ilorin, Kwara-state'
    motto = 'Better by Far'
    
    def __init__(self, sch_type=s_type, sch_name=name, sch_addr=addr, sch_motto=motto, sch_session = None) -> None:
        super().__init__(sch_type)
        
        # Instance Variables
        self.name = sch_name
        self.addr = sch_addr
        self.motto = sch_motto
        self.session = sch_session
            
    def display_info(self) -> None:
        print(f'Your School type is: "{self.type}"')
        print(f'Your School name is: "{self.name}"')
        print(f'Your School address is: "{self.addr}"')
        print(f'Your School motto is: "{self.motto}"')
        if self.session == None:
            pass
        else:
            print(f'Your Session Year is: "{self.session}"')