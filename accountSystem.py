import sqlite3 as sql
import hashlib
import os
import string


def createAccount(username, email, password):
    if checkPassword(password)[5] < 3:
        return False
    salt = os.urandom(32)
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO accounts VALUES (?, ?, ?, ?)",
        (username, email, hashedPassword, salt),
    )
    connection.commit()
    connection.close()
    return True


def checkPassword(password):
    minLength = 8
    maxLength = 36
    strength = 0
    lowercaseLetters = string.ascii_lowercase
    uppercaseLetters = string.ascii_uppercase
    numbers = string.digits
    specialCharacters = string.punctuation
    lengthRequirements = False
    lowercaseRequirements = False
    uppercaseRequirements = False
    numberRequirements = False
    specialCharacterRequirements = False
    if len(password) >= minLength and len(password) <= maxLength:
        strength += 1
        lengthRequirements = True
    for char in password:
        if char in lowercaseLetters:
            lowercaseRequirements = True
        if char in uppercaseLetters:
            uppercaseRequirements = True
        if char in numbers:
            numberRequirements = True
        if char in specialCharacters:
            specialCharacterRequirements = True
    if lowercaseRequirements:
        strength += 1
    if uppercaseRequirements:
        strength += 1
    if numberRequirements:
        strength += 1
    if specialCharacterRequirements:
        strength += 1
    return [
        lengthRequirements,
        numberRequirements,
        lowercaseRequirements,
        uppercaseRequirements,
        specialCharacterRequirements,
        strength,
    ]


def login(username, password):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        return True
    else:
        return False


def checkAccount(username, password):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        return True
    else:
        return False


def changePassword(username, oldPassword, newPassword):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", oldPassword.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        salt = os.urandom(32)
        hashedPassword = hashlib.pbkdf2_hmac(
            "sha256", newPassword.encode("utf-8"), salt, 100000
        )
        connection = sql.connect("accountSystem.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE accounts SET password=?, salt=? WHERE username=?",
            (hashedPassword, salt, username),
        )
        connection.commit()
        connection.close()
        return True
    else:
        return False


def changeEmail(username, password, newEmail):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        connection = sql.connect("accountSystem.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE accounts SET email=? WHERE username=?", (newEmail, username)
        )
        connection.commit()
        connection.close()
        return True
    else:
        return False


def deleteAccount(username, password):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[4]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        connection = sql.connect("accountSystem.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM accounts WHERE username=?", (username,))
        connection.commit()
        connection.close()
        return True
    else:
        return False


def getAccount(username):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    return account


def changeAccountType(username, newAccountType):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET accountType=? WHERE username=?", (newAccountType, username)
    )
    connection.commit()
    connection.close()


def enrollInCourse(courseName, username, password):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        connection = sql.connect("accountSystem.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO enrollments VALUES (?, ?)", (courseName, username))
        connection.commit()
        connection.close()
        return True
    else:
        return False


def unenrollInCourse(courseName, username, password):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account = cursor.fetchone()
    connection.close()
    if account == None:
        return False
    salt = account[3]
    hashedPassword = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    if hashedPassword == account[2]:
        connection = sql.connect("accountSystem.db")
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM enrollments WHERE courseName=? AND username=?",
            (courseName, username),
        )
        connection.commit()
        connection.close()
        return True
    else:
        return False


def getEnrolledCourses(username):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM enrollments WHERE username=?", (username,))
    courses = cursor.fetchall()
    connection.close()
    return courses


def getEnrolledUsers(courseName):
    connection = sql.connect("accountSystem.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM enrollments WHERE courseName=?", (courseName,))
    users = cursor.fetchall()
    connection.close()
    return users
