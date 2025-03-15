from django.db import models

# Model Khách hàng (Customer)
class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # ID tự tăng
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# Model Sản phẩm (Product)
class Product(models.Model):
    id = models.AutoField(primary_key=True)  # ID tự tăng
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Model Nhân sự (Employee)
class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # ID tự tăng
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Model Bảng công việc (Task Board)
class Task(models.Model):
    id = models.AutoField(primary_key=True)  # ID tự tăng
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField()

    def __str__(self):
        return self.title
