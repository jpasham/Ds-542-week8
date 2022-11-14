#creating a class with name university
class University:

    #defining a constructor
    def __init__(self,university_name,location,undergraduate_students,graduate_students):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students

    #defining a method to print sum of graduate and undergraduate students in university
    def print_university_size(self):
        size = self.undergraduate_students + self.graduate_students
        print("Size of the University:",size)

    #check if undergraduat students are greater
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students:
            print('There are more undergraduate students than graduate students')

        else:
            print('There are more graduate students than undergraduate students')


#creating a object for University class
SPU = University("Saint Peter’s University","Jersey City, New Jersey",2134,875)

#calling the methods inside the university class
SPU.print_university_size()

SPU.is_undergraduate_greater()

#creating a class for College
class College(University):

    #defining a constructor
    def __init__(self,university_name,location,undergraduate_students,graduate_students):
        self.name = university_name
        super().__init__(university_name,location,undergraduate_students,graduate_students)

    #definging a method to print name of college
    def collegeName(self):
        print("Name of the college is:",self.name)

#creating a object for college class
clg = College("Saint Peter’s University","Jersey City, New Jersey",2134,875)

clg.collegeName()