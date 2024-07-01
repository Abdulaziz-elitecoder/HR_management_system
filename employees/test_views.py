from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Employee, Attendance

class EmployeeViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Employee.objects.create_user(
            username='testuser', email='testuser@ivoiceup.com', password='password', is_hr=True
        )
        self.client.force_authenticate(user=self.user)
        self.employee_data = {'username': 'existingemployee', 'email': 'employee@ivoiceup.com', 'is_hr': False}
        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {
            'username': 'newuser',
            'email': 'newuser@ivoiceup.com',
            'password': 'testpassword',
            'is_hr': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 3)  
        self.assertEqual(Employee.objects.get(username='newuser').username, 'newuser')
    
    def test_get_employees(self):
        response = self.client.get(reverse('employee-list'))
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
        self.assertEqual(response.data[0]['username'], 'testuser')
        
        
    def test_get_employee_detail(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.employee.username)
    
    def test_update_employee(self):
        updated_data = {'username': 'updatedemployee'}
        response = self.client.patch(reverse('employee-detail', kwargs={'pk': self.employee.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], updated_data['username'])
    
    def test_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', kwargs={'pk': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 1)

class AttendanceViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@ivoiceup.com', password='password', is_hr=True
        )
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(username='employee1', email='employee1@ivoiceup.com', is_hr=False)
        self.attendance_data = {'employee': self.employee.id, 'date': '2024-06-15', 'present': True}
        self.attendance = Attendance.objects.create(employee=self.employee, date='2024-06-15', present=True)
    
    def test_create_attendance(self):
        response = self.client.post(reverse('attendance-list'), self.attendance_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_attendance(self):
        response = self.client.get(reverse('attendance-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['employee'], self.attendance.employee.id)
    
    def test_get_attendance_detail(self):
        response = self.client.get(reverse('attendance-detail', kwargs={'pk': self.attendance.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['employee'], self.attendance.employee.id)
    
    def test_update_attendance(self):
        updated_data = {'present': False}
        response = self.client.patch(reverse('attendance-detail', kwargs={'pk': self.attendance.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['present'])
    
    def test_delete_attendance(self):
        response = self.client.delete(reverse('attendance-detail', kwargs={'pk': self.attendance.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Attendance.objects.count(), 0)
