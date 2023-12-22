import sqlite3 as sql
import hashlib
import os

def createAccount(username, email, accountType, password):
    salt = os.urandom(32)
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO accounts VALUES (?, ?, ?, ?, ?)', (username, email, accountType, hashedPassword, salt))
    connection.commit()
    connection.close()
    
def checkAccount(username, password):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        return True
    else:
        return False
    
def changePassword(username, oldPassword, newPassword):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', oldPassword.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        salt = os.urandom(32)
        hashedPassword = hashlib.pbkdf2_hmac('sha256', newPassword.encode('utf-8'), salt, 100000)
        connection = sql.connect('accountSystem.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE accounts SET password=?, salt=? WHERE username=?', (hashedPassword, salt, username))
        connection.commit()
        connection.close()
        return True
    else:
        return False
    
def changeEmail(username, password, newEmail):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        connection = sql.connect('accountSystem.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE accounts SET email=? WHERE username=?', (newEmail, username))
        connection.commit()
        connection.close()
        return True
    else:
        return False
    
def deleteAccount(username, password):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        connection = sql.connect('accountSystem.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM accounts WHERE username=?', (username,))
        connection.commit()
        connection.close()
        return True
    else:
        return False

def getAccount(username):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    return account

def changeAccountType(username, newAccountType):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE accounts SET accountType=? WHERE username=?', (newAccountType, username))
    connection.commit()
    connection.close()
    
def enrollInCourse(courseName, username, password):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        connection = sql.connect('accountSystem.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO enrollments VALUES (?, ?)', (courseName, username))
        connection.commit()
        connection.close()
        return True
    else:
        return False
    
def unenrollInCourse(courseName, username, password):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=?', (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if hashedPassword == account[3]:
        connection = sql.connect('accountSystem.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM enrollments WHERE courseName=? AND username=?', (courseName, username))
        connection.commit()
        connection.close()
        return True
    else:
        return False
    
def getEnrolledCourses(username):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM enrollments WHERE username=?', (username,))
    courses = cursor.fetchall()
    connection.close()
    return courses

def getEnrolledUsers(courseName):
    connection = sql.connect('accountSystem.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM enrollments WHERE courseName=?', (courseName,))
    users = cursor.fetchall()
    connection.close()
    return users

