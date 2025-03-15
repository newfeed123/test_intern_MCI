from rest_framework import serializers
from .models import Customer, Product, Employee, Task
from django.contrib.auth.models import User
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), allow_null=True,
        help_text="ID của nhân sự được giao nhiệm vụ."
    )
    status = serializers.ChoiceField(
        choices=Task.STATUS_CHOICES,
        help_text="Trạng thái công việc. Các giá trị hợp lệ: 'todo', 'in_progress', 'done'."
    )
    class Meta:
        model = Task
        fields = '__all__'
 
    def validate(self, data):
        """ Kiểm tra nếu Employee không tồn tại """
        assigned_to = data.get("assigned_to")
        if assigned_to and not Employee.objects.filter(id=assigned_to.id).exists():
            raise serializers.ValidationError({"assigned_to": "Nhân sự không tồn tại."})
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True}  # Không cho phép người dùng tự đặt giá trị
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_staff = True  # Luôn đặt is_staff = True
        user.save()
        return user