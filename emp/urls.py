from django.urls import path
from .views import DepartmentList, DepartmentDetail, EmployeeList, EmployeeDetail

urlpatterns = [
    path('emp/', EmployeeList.as_view()),
    path('emp/<int:pk>/', EmployeeDetail.as_view()),
    path('dept/', DepartmentList.as_view()),
    path('dept/<int:pk>', DepartmentDetail.as_view()),
]