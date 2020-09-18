class Student:
	def __init__(self, firstname, lastname, gender, age, *, school):
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.age = age
		self.classes = []
		self.school = school

	@classmethod
	def create(cls, firstname, lastname, gender, age, *, school):
		return cls(firstname, lastname, gender, age, school=school)

	def __repr(self):
		return f"<Student '{self.firstname} {self.lastname}'>'"

class Teacher:
	def __init__(self, firstname, lastname, gender, age, *, school):
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.age = age
		self.classes = []
		self.school = school

	@classmethod
	def create(cls, firstname, lastname, gender, age, *, school):
		return cls(firstname, lastname, gender, age, school=school)

	def __repr(self):
		return f"<Teacher '{self.firstname} {self.lastname}'>'"