from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Customer, Product, Employee, Task
from django.contrib.auth.models import User
from .serializers import CustomerSerializer, ProductSerializer, EmployeeSerializer, TaskSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # ✅ Thêm thuộc tính này
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'assigned_to__name']

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        assigned_to = self.request.query_params.get('assigned_to')

        if status:
            queryset = queryset.filter(status=status)
        if assigned_to:
            queryset = queryset.filter(assigned_to_id=assigned_to)

        return queryset

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

