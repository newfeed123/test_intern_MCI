from django.contrib import admin

from .models import Customer, Product, Employee, Task
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone', 'address')  # Hiển thị tất cả các trường
    search_fields = ['name', 'email', 'phone']  # Tìm kiếm theo tên, email, số điện thoại
    # list_filter = ['status']  # Lọc theo ngày tạo, trạng thái

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ['name', "price", "description"]
    list_filter = ['price', 'name']  # Lọc theo giá

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'phone')
    search_fields = ['name', 'email', 'position']
    # list_filter = ['department', 'status']  # Lọc theo phòng ban, trạng thái nhân viên

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'assigned_to', 'status', 'due_date')
    search_fields = ['title', 'description', 'assigned_to__name']  # Tìm kiếm theo tiêu đề, mô tả, người được giao
    # list_filter = ['status', 'assigned_to']  # Lọc theo trạng thái, nhân sự được giao

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)
