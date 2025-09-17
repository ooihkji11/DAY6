class student:
 def __init__(self,name,id,grades):
  self.name = name
  self.id = id
  self.grades = grades
 def GPA(self):
  return sum(self.grades)/len(self.grades)

 students = {100 : { "name" : "ali" , "grades" : [60 ,70 , 90]} ,120 : {"name" :"khaled" , "grades" : [70 ,90 , 66] } }
open("grades.txt","w")
with open("grades.txt","r") as grades :
 f = open("grades.txt", "r")
 data = f.read()
 print(data)