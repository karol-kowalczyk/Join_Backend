from django.urls import path
from .views import ContactListView, ContactDetailView, TaskListView, TaskDetailView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
