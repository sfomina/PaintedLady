import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

#create dictionaries through csv's
student_reader = csv.DictReader(open('peeps.csv'))
course_reader = csv.DictReader(open('courses.csv'))

'''
for row in course_reader:
    print row['code'] 


print "\n\n"

for row in student_reader:
    print row['name']
'''

#create db tables
studentCreate = "CREATE TABLE students (name TEXT,age INTEGER ,id INTEGER);"
courseCreate = "CREATE TABLE courses (code TEXT,mark INTEGER,id INTEGER);"

#fill in tables
def fillStudent():
    for row in student_reader:
        c.execute("INSERT INTO students VALUES (row['name'], row['age'], row['id']);") 

def fillCourses():
    for row in course_reader:
        c.execute("INSERT INTO courses VALUES (row['code'], row['systems'],row['mark']);")
    



#command = studentCreate + courseCreate + fillCourses() + fillStudent() 
c.execute(studentCreate)
c.execute(courseCreate)
#c.execute("INSERT INTO students VALUES (bob, 44, 3);")
fillCourses()
fillStudent()



#run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


