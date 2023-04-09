"""
@class_method()
Transform a method into a class method. A class method receives the class as
a implicit first argument
"""

class TestClass:
    def regular_method(self):
        print(self)

    @classmethod
    def class_method(cls):
        print(cls)

    def __str__(self):
        return "TestClass instance"


t = TestClass()
t.regular_method()
t.class_method()
TestClass.class_method()