# 🎓 Student Data Organizer / Collector Manipulator

A simple **Python-based Student Management System** that allows users to manage student records through a menu-driven interface.

This project demonstrates the use of:

* Lists
* Dictionaries
* Sets
* Tuples
* Loops
* Pattern Matching (`match-case`)
* CRUD Operations (Create, Read, Update, Delete)

---

## 🚀 Features

### ➕ Add Student

* Automatically generates a unique Student ID.
* Stores:

  * Student Name
  * Age
  * Grade
  * Date of Birth
  * Subjects
* Prevents duplicate subjects using Python Sets.

### 📋 Display All Students

* Shows all stored student records.
* Displays:

  * Student ID
  * Name
  * Age
  * Grade
  * Subjects

### ✏️ Update Student Information

* Update:

  * Age
  * Grade
  * Subjects
* Uses Student ID for identification.

### ❌ Delete Student

* Delete a student record by Student ID.
* Includes confirmation before deletion.

### 📚 Display Subjects Offered

* Collects all unique subjects from every student.
* Displays them in sorted order.

### 🚪 Exit Program

* Safely exits the application.

---

## 🏗️ Data Structure Used

Each student record is stored as a dictionary:

```python
{
    "name": "John",
    "age": 16,
    "grade": "10th",
    "ID_DOB": (101, "2008-05-12"),
    "subject": {"Math", "Science", "English"}
}
```

### Structure Explanation

| Key     | Type    | Description                  |
| ------- | ------- | ---------------------------- |
| name    | String  | Student Name                 |
| age     | Integer | Student Age                  |
| grade   | String  | Student Grade                |
| ID_DOB  | Tuple   | Student ID and Date of Birth |
| subject | Set     | Student Subjects             |

---

---

## ▶️ How to Run

### Prerequisites

* Python 3.10 or higher

Check your Python version:

```bash
python --version
```

### Run the Program

```bash
python Collector_manipulator.py
```

---

## 🖥️ Menu Options

```text
1. Adding the Student
2. Display all the Students
3. Update the Student Information
4. Delete Student
5. Display the subjects offered
6. Exit
```

---

## 📸 Example Usage

### Add Student

```text
Enter your choice: 1

The Student ID will be 101

Enter the name of Student : Alice
Enter the age of Student : 16
Enter the grade of Student : 11th
Enter the birth date (YYYY-MM-DD) : 2008-03-15
Enter the Subject (Separated by COMMA) : Math, Science, English
```

### Display Students

```text
Student ID: 101 | Name: Alice | Age: 16 | Grade: 11th | Subjects: English, Math, Science
```

---

## 💡 Concepts Demonstrated

This project is useful for beginners learning:

* Python Lists
* Dictionaries
* Sets
* Tuples
* CRUD Operations
* Data Management
* Loops
* Input Handling
* Pattern Matching (`match-case`)
* Basic Record Management Systems

---
