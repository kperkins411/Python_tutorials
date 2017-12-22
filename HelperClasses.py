class SimpleGradebook(object):
    def __init__(self):
        self._grades={}

    def add_student(self,name):
        if name not in self._grades:
            self._grades[name]={}

    def add_grade(self,name,subject, grade):
        self.add_student(name)
        grade_list = self._grades[name].setdefault(subject,[])
        grade_list.append(grade)

    def print_people(self):
        for key in self._grades.keys():
            print(key)

    def list_people(self):
        return list(self._grades.keys())

    def list_grades(self,name):
        return self._grades[name]

    def average_grade(self, name,subject):
        if name not in self._grades.keys():
            raise ValueError("Name " + name+ " not in grades")
        allgrades = self._grades[name]
        if subject not in allgrades.keys():
            raise ValueError("Subject " + subject + " not in " + name + " subjects")

        numgrades = len(allgrades[subject])
        total = sum(allgrades[subject])
        return total/numgrades



gb = SimpleGradebook()
gb.add_grade("keith","math", 100)
gb.add_grade("keith","math", 90)
gb.add_grade("shirly","calc",99)

print("KP average is " +str(gb.average_grade("keith","math")))
# gb.print_people()

people = gb.list_people()
for person in people:
    print(person)

grades = gb.list_grades("keith")
if len(grades)>0:
    print ("keiths grades are:")
    for grade in grades:
        grade=200
        print(grade)

grades = gb.list_grades("keith")
if len(grades)>0:
    print ("keiths grades are:")
    for grade in grades:
         print(grade)

