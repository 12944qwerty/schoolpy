from .humans import Student, Teacher
from .errors import ClassTypeError

class Subject:
	def __init__(self, name, *, type_='regular', subject, school):
		self.name = name
		self.type = type_
		self.subject = subject
		self.school = school

	@classmethod
	def create(cls, name, *, type_, subject, school):
		valid_types = ('regular', 'ap', 'advanced placement', 'honors')
		if type_.lower() not in valid_types:
			raise ClassTypeError(f"'{type_}' is not a valid school type.\nUse one of the following: {', '.join(valid_types)}")
		return cls(name, type_=type_, subject=subject, school=school)

	def __repr__(self):
		return f"<Class '{self.type} {self.name}' - '{self.subject}'>"

class School(object):
	def __init__(self, name, *, periods=8):
		self.name = name
		self.periods = periods
		self.classes = []
		self.students = []
		self.teachers = []

	def create_class(self, name, *, type_='regular', subject):
		self.classes.append(Subject.create(name, type_=type_, subject=subject, school=self))

	def add_student(self, firstname, lastname, gender, age):
		self.students.append(Student.create(firstname, lastname, gender, age, school=self))

	def add_teacher(self, firstname, lastname, gender, age):
		self.teachers.append(Teacher.create(firstname, lastname, gender, age, school=self))


	def __repr__(self):
		return f"<School '{self.name}'>"