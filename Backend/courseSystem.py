import sqlite3 as sql
import hashlib
import os

def createCourse(creator, courseName, courseDescription, coursePrerequisites, courseImage, courseRating):
    connection = sql.connect('courseSystem.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO courses VALUES (?, ?, ?, ?, ?, ?)', (creator, courseName, courseDescription, coursePrerequisites, courseImage, courseRating))
    connection.commit()
    connection.close()
    
def editCourse(courseName, courseDescription, coursePrerequisites, courseImage, courseRating):
    connection = sql.connect('courseSystem.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE courses SET courseDescription=?, coursePrerequisites=?, courseImage=?, courseRating=? WHERE courseName=?', (courseDescription, coursePrerequisites, courseImage, courseRating, courseName))
    connection.commit()
    connection.close()
    
def changeRating(courseName, courseRating):
    connection = sql.connect('courseSystem.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE courses SET courseRating=? WHERE courseName=?', (courseRating, courseName))
    connection.commit()
    connection.close()
    
def getCourse(courseName):
    connection = sql.connect('courseSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses WHERE courseName=?', (courseName,))
    course = cursor.fetchone()
    connection.close()
    return course

