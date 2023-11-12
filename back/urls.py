from django.urls import path
from . import views
from back.views import StudentListView
from back.views import UserListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('users/', UserListView.as_view(), name='student-list'),
]