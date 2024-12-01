# Define a Student class with attributes and methods to calculate and print average marks
#Demonstrating class Example
class Student:
    def __init__(self, name, math_score, science_score,english_score):
        self.name = name
        self.math_score = math_score
        self.science_score=science_score
        self.english_score=english_score

    def calculate_average(self):
        return round((self.math_score + self.science_score + self.english_score) / 3,2)
    
    def print_average(self):
        print(f"The average mark of {self.name} is: {self.calculate_average()}")
# Create an instance of the Student class with specific values
student =Student("aman",59,70,98)
student.print_average()
