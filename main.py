from faculty import Faculty

if __name__ == "__main__":
    fac = Faculty()
    print(fac.add_course('Csc224'))
    print(fac.add_course('Csc214'))
    print(fac.add_course('Csc243'))
    print(fac.add_course('gbh231'))
    print('These are all your Course: ',fac.get_courses())

    #fac.calculate_gpa()
    #print(fac.show_gpa())
    print(fac.get_courses())
    print(fac.show_remark())