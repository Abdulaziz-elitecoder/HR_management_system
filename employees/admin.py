from django.contrib import admin
from .models import Employee, Attendance


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_hr')
    search_fields = ('username', 'email')
    list_filter = ('is_hr',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'present')
    search_fields = ('employee__username', 'employee__email')
    list_filter = ('present', 'date')