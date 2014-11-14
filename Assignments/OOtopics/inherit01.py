__author__ = "Sree Nilakanta"
""" Here we will develop a superclass Person
... and inherit its properties into a subclass Student
... and another subclass Employee. We will also set up
... constructors and destructors, getters and setters, 
... and overload methods and illustrate data hiding.
"""
class Person:
	__perCount = 0 # static
	
	def __init__(self, uid, lastName, firstName):
		self.uid = uid
		self.lastName = lastName
		self.firstName = firstName
		__perCount += 1
		
	def showCount(self):
		print ("Total population is ", __perCount)
		
	def __del__(self)
		class_name = self.__class__.__name__
		print (class_name, " destroyed.")
		
class Student(Person):
	def __init__(self): print("called parent Person")
	
	def setAttr(self, major, level):
		self.major = major
		self.level = level # classification level
		
	def getAttr(self):
		return major, level
