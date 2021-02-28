# The Student class (you'll edit and expand on this)
import random
import numpy as np
class Student(object):
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name, gpa,year):
        self.name = np.array(name).astype(str)
        self.gpa = np.array(gpa).astype(float)
        self.year = np.array(year).astype(int)
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        

    def years_until_graduation(self):
        
        if (4 - self.year) == 1:
            print(self.name, "has one year left until graduation")
        else:
            print(self.name, "has" ,4 - self.year, " years left until graduation.")
            
            
    def enroll(self,courses):
        i = 0
        course_list = []
        while i < 2:
            i += 1
            course_list.append(courses[random.randint(0,len(courses)-1)])
        self.courses = course_list
    def display_courses(self):
        print("I am enrolled in",self.courses)
class Spartan():
     
    def __init__(self,name = ''):
        self.name = name
    
    def set_motto(self,motto = ''):
        self.motto = motto

    def school_spirit(self):
        print("My name is", self.name)
        print("I am a Spartan. My motto is", self.motto)