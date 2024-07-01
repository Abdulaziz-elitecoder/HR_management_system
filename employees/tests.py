from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Attendance, Employee
from datetime import date

class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@ivoiceup.com', password='password', is_hr=True
        )
    
    def test_employee_creation(self):
        employee = Employee.objects.get(username='testuser')
        self.assertEqual(employee.username, 'testuser')
        self.assertEqual(employee.email, 'testuser@ivoiceup.com')
        self.assertTrue(employee.is_hr)

class AttendanceModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@ivoiceup.com', password='password', is_hr=True
        )
        self.employee = Employee.objects.create(
            username='employee1', email='employee1@ivoiceup.com', is_hr=False
        )
        self.attendance = Attendance.objects.create(
            employee=self.employee, date=date.today(), present=True
        )
    
    def test_attendance_creation(self):
        attendance = Attendance.objects.get(employee=self.employee)
        self.assertEqual(attendance.employee.username, 'employee1')
        self.assertEqual(attendance.date, date.today())
        self.assertTrue(attendance.present)
