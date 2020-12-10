class Person:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address=address

    def toString(self):
        return self.name + "(" + self.address+")"

class Teacher(Person):
    #courses = {}
    def __init__(self,name,address, numCourses:int,courses:str):
        Person.__init__(self, name,address)
        self.courses= courses.split(",")
        self.numCourses = numCourses

    def addCourse(self, cour:str):
        course = cour
        if course in self.courses: return False
        elif course not in self.courses:
            self.courses.append(course)
            self.numCourses = self.numCourses - 1

    def removeCourse(self, cour:str):
        course = cour
        if course in self.courses:
            self.courses.pop(course.index(course))
            self.numCourses = self.numCourses -1
        elif course not in self.courses: return False

    def toString(self):
        courses=""
        for i in self.courses: courses=courses+" "+i
        return print("Teacher: "+Person.toString(self)+" Courses: "+courses)

class Student(Person):
    def __init__(self,name,address, numCourses:int,courses:str,grades:int):
        Person.__init__(self,name,address)
        self.courses = courses.split(",")
        self.numCourses = numCourses
        self.grade = grades.split(",")
        self.graded = dict(zip(self.courses,self.grade))

    def addCourse(self, cour: str, grade:int):
        self.numCourses=self.numCourses+1
        course = "," + cour
        if course in self.courses:
            return False
        elif course not in self.courses:
            self.graded[course] = self.graded.get(course, grade)

    def printGrades(self):
        grades = ""
        for i in self.graded:
            gradse = grades +str(self.graded[i] + ",")
        return grades
    def getAvarageGrade(self):
        ave = 0
        for i in self.graded:
            ave = ave + int(self.graded[i])
        return ave/self.numCourses
    def toString(self):
        courses = ""
        for i in self.graded:
            courses= courses +str(i)+":"+str(self.graded[i])+","
        return print("Student: " + Person.toString(self) + " Courses: " + courses)

if __name__ == '__main__':
    Stu = Student("Hassan","Hargeisa",2,"English,Math","45,78")
    Stu.toString()
    Stu.addCourse("Science",98)
    Stu.toString()
    print(Stu.getAvarageGrade())

#This does not follow the chart exactly as I had to add more information for testing, especially for the toString

    Tea = Teacher("Mohamed", "Hargeisa", 2, "English,Math",)
    Tea.toString()
    print(Tea.addCourse("English"))
    Tea.addCourse("Science")
    Tea.toString()
    Tea.removeCourse("Science")
    Tea.toString()

