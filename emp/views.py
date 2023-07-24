from django.shortcuts import render
from rest_framework import generics
from .models import Department, Employee
from .serializers import EmployeeSerializer, DepartmentSerializer
# Create your views here.

class EmployeeList(generics.ListCreateAPIView):
    serializer_class=EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        if department is not None:
            queryset = queryset.filter(itemDepartment=department)
        return queryset

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DepartmentList(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
       
 
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
       
