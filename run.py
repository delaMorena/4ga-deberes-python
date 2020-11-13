class Student:

    def __init__(self, name, previous_studies, tech_skills = None, age=0, gender = None):
        self.name = name
        self.previous_studies = previous_studies
        self.tech_skills = tech_skills
        self.age = age
        self.gender = gender

student1 = Student('Marta', 'Biology', 'HTML, CSS, JS', 41,  gender = 'female')
print(student1.tech_skills)
student2 = Student('Tiby', 'Odontology', 'HTML, CSS, JS', 31,'female')
print(student2.gender, student2.name)
student3 = Student('Alex', previous_studies='ingenier', age=32)
print(student3.age)


