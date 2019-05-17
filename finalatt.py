from array import *
import MySQLdb
import smtplib 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from array import *
import time
import schedule
#database= attendance; table=student_attendance
GPIO.setwarnings(False)
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login("kumarikeerthi65@gmail.com", "harsh@143")
reader = SimpleMFRC522()
db = MySQLdb.connect("localhost","pi","deva123456","attendance" )
cursor = db.cursor()
sql = "SELECT * FROM student_attendance"

name=[]
print "Welcome"

for i in range(2):
  
  
  ide = reader.read()
  
  print ide[0]
  a = ide[0] 
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    S_No           = row[0]
    Student_Name   = row[1]
    Tag            = row[2]
    Department     = row[3]
    
    
    if a == Tag:
        d = time.strftime("%c")
        print d
        msg = Student_Name
        name.append(Student_Name+" is present for the class ") 
        print msg
        print "Student with name {} is present".format(Student_Name)
        time.sleep(1)
      
      
  print (name)
  msg = '\n'.join(name)
print msg
s.sendmail("kumarikeerthi65@gmail.com", "pdharsha11@gmail.com", msg)
