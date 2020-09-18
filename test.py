import Schoolpy as school

metea = school.School("Metea")

metea.create_class("English 1", type_="regular", subject='English')

print(metea.classes)