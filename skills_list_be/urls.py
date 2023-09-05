"""
URLs for the Skills List API
API allows anyone access to list, create, update, and delete skills
"""
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.skillsList.as_view()),
    path('api/skillsList/', views.skillsList.as_view()),
    path('api/skills/', views.skillsListCreate.as_view()),
    path('api/skills/<int:pk>',
views.skillRetrieveUpdateDestroy.as_view()),
]