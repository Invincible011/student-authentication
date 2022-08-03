from faculty import Faculty

fac = Faculty()
print('These are all your Course: ',fac.get_courses())

# print(fac.add_course('gbh231'))
# print('These are all your Course: ',fac.get_courses())

fac.calculate_gpa()
print(fac.show_gpa())
print(fac.show_remark())