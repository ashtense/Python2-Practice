class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def calculate(self):
        temp_average = 0
        for score in scores:
            temp_average = temp_average + score
        temp_average = temp_average / scores.__len__()
        grade = 'None'
        if temp_average < 40:
            grade = 'T'
        elif temp_average >= 40 and temp_average < 55:
            grade = 'D'
        elif temp_average >= 55 and temp_average < 70:
            grade = 'P'
        elif temp_average >= 70 and temp_average < 80:
            grade = 'A'
        elif temp_average >= 80 and temp_average < 90:
            grade = 'E'
        elif temp_average >= 90 and temp_average <= 100:
            grade = 'O'
        return grade.strip()

firstName = "Ashwani"
lastName = "Solanki"
idNum = "007"
scores = [70,70,70,70]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())