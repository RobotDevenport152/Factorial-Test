class Student:
    def __init__(self, name, age):
        self.name = name        # public
        self._age = age         # protected
        self.__grade = 'A'      # private

    def get_grade(self):
        return self.__grade

    # New method that uses the private attribute
    def is_passing(self):
        """Determine if the student is passing based on grade"""
        # Encapsulation: we access the private attribute via a method instead of directly
        if self.__grade == 'A' or self.__grade == 'B' or self.__grade == 'C':
            return 'passing'
        return 'failed'

# Demonstration of public and protected attributes in another class
class Course:
    def __init__(self, course_name, student):
        self.course_name = course_name   # public attribute
        self._student = student          # protected attribute

    def course_info(self):
        print(f"Course: {self.course_name}")
        print(f"Student Name (public): {self._student.name}")
        print(f"Student Age (protected, discouraged): {self._student._age}")

# Encapsulation example: accessing private attribute only via method
s = Student('Ali', 20)
print(s.name)               # public: accessible
print(s._age)               # protected: accessible but discouraged
print(s.get_grade())        # private: accessed correctly via method
print(s.is_passing())       # uses private attribute internally

c = Course('Math', s)
c.course_info()
