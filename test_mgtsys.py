# test_mgtsys.py

from Mgtsys import StudentManagementSystem

def test_add_student():
    sms = StudentManagementSystem()
    result = sms.add_student("1", "Alice", "20")
    assert result == "Student added successfully."
